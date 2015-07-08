(defmacro with-answer (query &body body)
  (let ((binds (gensym)))
    `(dolist (,binds (prove `,query))
       (let ,(mapcar #`(lambda (v)
                         `(,v (binding `,v ,binds)))
                     (vars-in query))
         ,@body))))
