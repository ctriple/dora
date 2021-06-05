# Prometheus Architecture

```
+-------------------------------------------------------------------------------------------------------------------------------+
|                                +------------------+                                                                           |
|                                | EC2, Kubernetes, |                                                                           |
|                                | Consul, etc.     |                                                                           |
|                                +------------------+                                                                           |
|                                        ^                                                                                      |
|                                        |                                                                                      |
|                                +--------------------------------------------+                                                 |
| +-------------------+          | +-----------+       P.R.O.M.E.T.H.E.U.S.   |                                                 |
| | Application       |          | | Service   |                              |                                                 |
| |           +-------+          | | Discovery |                              |                                                 |
| |           |Client |<---+     | +-----------+                              |                                                 |
| |           |Library|    |     |       |                                    |                                                 |
| +-----------+-------+    |     |       v                                    |                                                 |
|                          |     | +-----------+      +------------------+    |      +--------------+    +-------------------+  |
| +-------------------+    +-----+-|  Scraping |      | Rules and Alerts |----+----->| Alertmanager |--->| Email, PagerDuty, |  |
| |     Exporter      |<---+     | +-----------+      +------------------+    |      +--------------+    | Chat, etc.        |  |
| +-------------------+          |       |                    ^ |             |                          +-------------------+  |
|          |                     |       v                    | v             |                                                 |
|          v                     | +-------------------------------------+    |      +------------+                             |
| +-------------------+          | |               Storage               |<---+------| Dashboards |                             |
| |     3rd Party     |          | +-------------------------------------+    |      +------------+                             |
| |    Application    |          +--------------------------------------------+                                                 |
| +-------------------+                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------+
```