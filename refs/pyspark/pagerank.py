"""
ref: https://github.com/apache/spark/blob/master/examples/src/main/python/pagerank.py
"""

from __future__ import print_function

import re
import sys
from operator import add

from pyspark.sql import SparkSession

def computeContribs(urls, rank):
    """Calculates URL contributions to the rank of other URLs."""
    num_urls = len(urls)
    for url in urls:
        yield(url, rank/num_urls)

def parseHeighbors(urls):
    """Parses a urls pair string into urls pair."""
    parts = re.split(r'\s+', urls)
    return parts[0], parts[1]

print("WARN: This is a naive implementation of PageRank and is given as an example!\n"+
        "Please refer to PageRank implementation provided by graphx", file=sys.stderr)

# Initialize the spark context.
spark = SparkSession.builder.appName("PythonPageRank").getOrCreate()

# Loads in input file, It should be in format of:
#     URL     neighbor URL
#     URL     neighbor URL
#     URL     neighbor URL
#     ...
lines = spark.read.text('testdata/pagerank.data').rdd.map(lambda r:r[0])

# Loads all URLs from input file and initialize their neighbors.
links = lines.map(lambda urls: parseHeighbors(urls)).distinct().groupByKey().cache()

# Loads all URLs from other URL(s) link to from input file and initialize ranks of them to one.
ranks = links.map(lambda url_neighbors: (url_neighbors[0], 1.0))

# Calculates and updates URL ranks continuously using PageRank algorithm.
for iteration in range(50):
    # Calculates URL contributions to the rank of other URLs.
    contribs = links.join(ranks).flatMap(
        lambda url_urls_rank: computeContribs(url_urls_rank[1][0], url_urls_rank[1][1]))

    # Re-calculates URL ranks based on neighbor contributions.
    ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank*0.85+0.15)

for (link,rank) in ranks.collect():
    print("%s has rank: %s." % (link, rank))

spark.stop()