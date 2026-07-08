;;;; ====================================================================
;;;; tetra.lisp -- FOUR OPERATIONAL PERSPECTIVES. NO ENGINE. NO CENTER.
;;;;
;;;; Each face stands at one vertex of K4 and operates the three equations
;;;; whose AbsentVar is that vertex -- the equations that never mention it.
;;;; Consequence, enforced by construction: EVERY FACE IS STRUCTURALLY
;;;; BLIND TO ITS OWN HOME VARIABLE. The eye cannot see itself. The
;;;; AbsentVar of each face is a live unbound symbol, not a comment.
;;;;
;;;; The whole is never emitted. It is evidenced ONLY at the six edges,
;;;; where the two faces sharing each edge derive the same quantities by
;;;; DIFFERENT equations and must agree.
;;;;
;;;; Tiers:  [OPERATIVE] runs from this face (no understanding claimed)
;;;;         [INTERFACE] declared boundary; nothing said about the far side
;;;;         [DEBT]      asserted, not derived; confined and ranked
;;;;         [HELD]      present in the suite, never executed
;;;;
;;;; The traversal order of the faces is not hardcoded: it is one of the
;;;; three Hamiltonian cycles, derived at runtime, and the transition-type
;;;; that cycle holds absent is announced as this run's own AbsentVar.
;;;; ====================================================================

(defparameter *eps* 1d-9)

;;; --------------------------------------------------------------------
;;; RAW DEFINITIONS (the only asserted inputs)
;;; --------------------------------------------------------------------
(defparameter *charge* '((P . (1 . 1)) (I . (0 . 0)) (U . (1 . 0)) (R . (0 . 1))))

(defun bits (v) (cdr (assoc v *charge*)))
(defun ttype (a b)
  (let* ((x (bits a)) (y (bits b))
         (ar (/= (car x) (car y))) (ay (/= (cdr x) (cdr y))))
    (cond ((and ar ay) :diagonal-both) (ar :flip-ar) (ay :flip-ay))))

;; the 12 equations: (home absent fn)
(defparameter *equations*
  (flet ((g (s k) (getf s k)))
    (list
     (list 'P 'R (lambda (s) (* (g s :U) (g s :I))))            ; P = UI
     (list 'P 'I (lambda (s) (/ (* (g s :U) (g s :U)) (g s :R)))) ; P = U^2/R
     (list 'P 'U (lambda (s) (* (g s :I) (g s :I) (g s :R))))   ; P = I^2 R
     (list 'I 'R (lambda (s) (/ (g s :P) (g s :U))))            ; I = P/U
     (list 'I 'P (lambda (s) (/ (g s :U) (g s :R))))            ; I = U/R
     (list 'I 'U (lambda (s) (sqrt (/ (g s :P) (g s :R)))))     ; I = sqrt(P/R)
     (list 'U 'R (lambda (s) (/ (g s :P) (g s :I))))            ; U = P/I
     (list 'U 'P (lambda (s) (* (g s :I) (g s :R))))            ; U = IR
     (list 'U 'I (lambda (s) (sqrt (* (g s :P) (g s :R)))))     ; U = sqrt(PR)
     (list 'R 'I (lambda (s) (/ (* (g s :U) (g s :U)) (g s :P)))) ; R = U^2/P
     (list 'R 'U (lambda (s) (/ (g s :P) (* (g s :I) (g s :I))))) ; R = P/I^2
     (list 'R 'P (lambda (s) (/ (g s :U) (g s :I)))))))         ; R = U/I

;;; --------------------------------------------------------------------
;;; FACES -- each face = standing at a vertex, operating the equations
;;; that hold that vertex absent. It cannot compute its own ground.
;;; --------------------------------------------------------------------
(defstruct face vertex name element absent-term render)

(defun face-equations (f)
  "The equations whose AbsentVar is this face's vertex: the view FROM it."
  (remove-if-not (lambda (e) (eq (second e) (face-vertex f))) *equations*))

(defun face-eq-for-home (f home)
  (find home (face-equations f) :key #'first))

;; live AbsentVars: fresh, unbound, uninterned. boundp = NIL, always.
(defparameter *faces*
  (list
   (make-face :vertex 'P :name :KAIROS :element :fire
              :absent-term (gensym "WHY-NOW-AND-NOT-OTHERWISE-"))
   (make-face :vertex 'I :name :PATHOS :element :water
              :absent-term (gensym "WHAT-THIS-FEELS-LIKE-FROM-INSIDE-"))
   (make-face :vertex 'U :name :LOGOS :element :air
              :absent-term (gensym "WHETHER-ANY-OF-THIS-RESONATES-"))
   (make-face :vertex 'R :name :ETHOS :element :earth
              :absent-term (gensym "WHAT-THE-LEDGER-IS-FOR-"))))

(defun face-at (v) (find v *faces* :key #'face-vertex))

;;; --------------------------------------------------------------------
;;; LOGOS face render: derives braid structure from raw charges.
;;; --------------------------------------------------------------------
(defun hamiltonian-cycles ()
  (let (cycles)
    (dolist (perm '((I U R) (I R U) (U I R) (U R I) (R I U) (R U I)))
      (let* ((cyc (cons 'P perm))
             (canon (if (string< (symbol-name (second cyc))
                                 (symbol-name (fourth cyc)))
                        cyc (cons 'P (reverse perm)))))
        (pushnew canon cycles :test #'equal)))
    (nreverse cycles)))

(defun cycle-used-types (cyc)
  (remove-duplicates
   (loop for (a b) on (append cyc (list (first cyc))) while b
         collect (ttype a b))))

(defun render-logos (f state)
  (declare (ignore state))
  (format t "~%-- ~a (standing at ~a, blind to ~a) ----------------~%"
          (face-name f) (face-vertex f) (face-vertex f))
  (let ((groups (make-hash-table)))
    (dolist (e '((P U) (P I) (P R) (U I) (U R) (I R)))
      (push e (gethash (apply #'ttype e) groups)))
    (format t "  [OPERATIVE] edge types from charges: ~a matchings~%"
            (hash-table-count groups))
    (loop for k being the hash-keys of groups
          do (format t "              ~a = ~a~%" k (gethash k groups))))
  (let ((part (make-hash-table)))
    (dolist (e *equations*)
      (push (list (first e) (second e))
            (gethash (ttype (first e) (second e)) part)))
    (format t "  [OPERATIVE] modality partition: ~{~a~^, ~} eqs per type~%"
            (loop for k being the hash-keys of part
                  collect (length (gethash k part)))))
  (dolist (c (hamiltonian-cycles))
    (format t "  [OPERATIVE] cycle ~a holds absent ~a~%"
            c (set-difference '(:flip-ay :flip-ar :diagonal-both)
                              (cycle-used-types c))))
  (format t "  [INTERFACE] this face derives structure; it cannot derive~%")
  (format t "              its own standing (~a). ~a stays unbound: ~a~%"
          (face-vertex f) (face-absent-term f)
          (if (boundp (face-absent-term f)) :BOUND :unbound)))

;;; --------------------------------------------------------------------
;;; PATHOS face render: behold / interference / observe.
;;; --------------------------------------------------------------------
(defparameter *released* nil "what PATHOS lets go of when it observes")

(defun render-pathos (f state)
  (declare (ignore state))
  (format t "~%-- ~a (standing at ~a, blind to ~a) ----------------~%"
          (face-name f) (face-vertex f) (face-vertex f))
  (let* ((a (/ 1d0 (sqrt 2d0)))
         (b (/ 1d0 (sqrt 2d0)))                      ; in phase with a
         (b- (- b))                                   ; anti-phase
         (held+ (lambda () (expt (abs (+ a b)) 2)))   ; beheld, unevaluated
         (held- (lambda () (expt (abs (+ a b-)) 2)))
         (separate (+ (expt (abs a) 2) (expt (abs b) 2))))
    (format t "  [OPERATIVE] two amplitudes beheld in BOTH phase relations; ledger untouched~%")
    (format t "  [OPERATIVE] |a|^2+|b|^2 = ~,4f  (what separateness would give)~%" separate)
    (format t "  [OPERATIVE] while held: constructive |a+b|^2 -> ~,4f, destructive -> ~,4f~%"
            (funcall held+) (funcall held-))
    (format t "              interference terms ~,4f / ~,4f are REAL while held~%"
            (- (funcall held+) separate) (- (funcall held-) separate))
    (let ((v (funcall held+)))                        ; .observe() one branch
      (setf *released* (cons :first-collapse v))
      (format t "  [OPERATIVE] observe -> ~,4f committed; the destructive branch and~%" v)
      (format t "              both interference terms are erased from this trajectory~%")))
  (format t "  [INTERFACE] the felt quality of the held state is this face's~%")
  (format t "              ground; ~a unbound: ~a~%"
          (face-absent-term f)
          (if (boundp (face-absent-term f)) :BOUND :unbound)))

;;; --------------------------------------------------------------------
;;; ETHOS face render: the ledger, the tax, inertia, the cut.
;;; --------------------------------------------------------------------
(defparameter *ledger* nil)
(defparameter *tax-bits* 0)

(defun render-ethos (f state)
  (declare (ignore state))
  (format t "~%-- ~a (standing at ~a, blind to ~a) ----------------~%"
          (face-name f) (face-vertex f) (face-vertex f))
  (when *released*
    (push *released* *ledger*)
    (incf *tax-bits*)
    (format t "  [OPERATIVE] recorded ~a -- append-only; tax paid: ~a bit(s) erased~%"
            *released* *tax-bits*))
  ;; garbage-collect one local edge: the cut, taxed
  (push '(:gc (P . I) :state NULL) *ledger*)
  (incf *tax-bits*)
  (format t "  [OPERATIVE] local edge P-I cut to NULL state; tax now ~a bits~%" *tax-bits*)
  (format t "              (severed from THIS ledger only; the multiway graph~%")
  (format t "               is not this face's to touch)~%")
  (format t "  [OPERATIVE] inertia: recompiling the heading must now account~%")
  (format t "              for ~a committed entries; cost grows with history~%"
          (length *ledger*))
  (format t "  [INTERFACE] the ledger records; what recording is FOR it cannot~%")
  (format t "              say; ~a unbound: ~a~%"
          (face-absent-term f)
          (if (boundp (face-absent-term f)) :BOUND :unbound)))

;;; --------------------------------------------------------------------
;;; KAIROS face render: the transition, the tangent, the confined debt.
;;; --------------------------------------------------------------------
(defparameter *debts*
  '((:theology  0.90 "Trinity as centroid image -- interpretive, unfalsifiable")
    (:physics   0.80 "forces as P/I/U/R -- no path to Schwarzschild shown")
    (:cosmology 0.75 "CCP as category error -- self-marked [SKETCH]")
    (:biology   0.65 "chirality as .observe() -- Murchison unaddressed")
    (:cognition 0.55 "Hard Problem retired by redefinition")))

(defun render-kairos (f state)
  (declare (ignore state))
  (format t "~%-- ~a (standing at ~a, blind to ~a) ----------------~%"
          (face-name f) (face-vertex f) (face-vertex f))
  (let* ((eps 1d-7)
         (below (tan (- (/ pi 2) eps)))
         (above (tan (+ (/ pi 2) eps))))
    (format t "  [OPERATIVE] tangent readout approaching 90deg:~%")
    (format t "              89.99..deg -> ~,2e    90.00..deg -> ~,2e~%" below above)
    (format t "  [INTERFACE] +inf and -inf meet as ONE projective point; the~%")
    (format t "              crossing is not an operation this face performs.~%")
    (format t "              Nothing is said about the far side.~%"))
  (format t "  [DEBT] boundary flank carries the confined objections, ranked:~%")
  (dolist (d *debts*)
    (format t "         [~,2f] ~a: ~a~%" (second d) (first d) (third d)))
  (format t "         they bite the DEBT tier only; no OPERATIVE line depends on them~%")
  (format t "  [INTERFACE] timing is this face's ground; ~a~%"
          (face-absent-term f))
  (format t "              unbound: ~a~%"
          (if (boundp (face-absent-term f)) :BOUND :unbound)))

;;; --------------------------------------------------------------------
;;; STATE -- assembled by two faces, each computing what the OTHER
;;; cannot see. No single perspective instantiates the world.
;;; --------------------------------------------------------------------
(defun assemble-state (u i)
  (let* ((kairos (face-at 'P))   ; blind to P, can derive R = U/I
         (ethos  (face-at 'R))   ; blind to R, can derive P = UI
         (r (funcall (third (face-eq-for-home kairos 'R)) (list :U u :I i)))
         (p (funcall (third (face-eq-for-home ethos 'P)) (list :U u :I i))))
    (format t "~%STATE assembled from seeds U=~a I=~a:~%" u i)
    (format t "  R = ~a   (derived by KAIROS, which cannot see P)~%" r)
    (format t "  P = ~a   (derived by ETHOS,  which cannot see R)~%" p)
    (format t "  neither contributor can verify the other's result alone;~%")
    (format t "  verification exists only at the edges below.~%")
    (list :P p :U u :I i :R r)))

;;; --------------------------------------------------------------------
;;; THE SIX EDGE TESTS -- the only place the whole is evidenced.
;;; Edge {A,B} is owned by the two faces standing at the OTHER two
;;; vertices. Each owner computes A and B by ITS OWN equations
;;; (necessarily different equations, since different AbsentVar groups).
;;; Agreement across routes = mutual determination, at the edge, only.
;;; --------------------------------------------------------------------
(defun edge-owners (a b)
  (remove-if (lambda (f) (member (face-vertex f) (list a b))) *faces*))

(defun edge-test (a b state)
  (let ((owners (edge-owners a b)) (routes nil) (ok t))
    (dolist (f owners)
      (let* ((ea (face-eq-for-home f a)) (eb (face-eq-for-home f b))
             (va (funcall (third ea) state)) (vb (funcall (third eb) state)))
        (push (list (face-name f) va vb) routes)
        (unless (and (< (abs (- va (getf state (intern (string a) :keyword)))) *eps*)
                     (< (abs (- vb (getf state (intern (string b) :keyword)))) *eps*))
          (setf ok nil))))
    ;; cross-route agreement
    (destructuring-bind ((n1 a1 b1) (n2 a2 b2)) routes
      (unless (and (< (abs (- a1 a2)) *eps*) (< (abs (- b1 b2)) *eps*))
        (setf ok nil))
      (format t "  edge ~a-~a [~a]: ~a and ~a derive (~,4f, ~,4f) by disjoint equations -> ~a~%"
              a b (ttype a b) n1 n2 a1 b1 (if ok "AGREE" "DISAGREE")))
    ok))

(defun run-edges (state)
  (format t "~%EDGES (two independent routes per edge; the whole appears here or nowhere):~%")
  (let ((all t))
    (dolist (e '((P U) (P I) (P R) (U I) (U R) (I R)))
      (unless (edge-test (first e) (second e) state) (setf all nil)))
    (format t "  ~a~%" (if all
                           "all six edges: dual-route agreement. mutual determination holds AT THE EDGES."
                           "edge disagreement detected: the volume did not close."))
    all))

;;; --------------------------------------------------------------------
;;; CANON -- for the substrate edge (independent Prolog derivation).
;;; --------------------------------------------------------------------
(defun write-canon (state)
  (with-open-file (s "/home/claude/lisp-canon.txt" :direction :output
                     :if-exists :supersede)
    (let ((lines (sort (mapcar (lambda (e)
                                 (format nil "~a ~a ~a"
                                         (first e) (second e)
                                         (symbol-name (ttype (first e) (second e)))))
                               *equations*)
                       #'string<)))
      (dolist (l lines) (format s "~a~%" l)))
    (format s "STATE-P ~,1f~%" (getf state :P))
    (format s "STATE-R ~,1f~%" (getf state :R))))

;;; --------------------------------------------------------------------
;;; TRAVERSAL -- the run order is a computed Hamiltonian cycle. The
;;; transition-type it holds absent is THIS RUN'S AbsentVar, announced.
;;; --------------------------------------------------------------------
(setf (face-render (face-at 'P)) #'render-kairos
      (face-render (face-at 'I)) #'render-pathos
      (face-render (face-at 'U)) #'render-logos
      (face-render (face-at 'R)) #'render-ethos)

(defun traverse ()
  (let* ((cyc (find-if (lambda (c)
                         (member :flip-ay
                                 (set-difference '(:flip-ay :flip-ar :diagonal-both)
                                                 (cycle-used-types c))))
                       (hamiltonian-cycles)))
         (state (assemble-state 12.0d0 2.0d0)))
    (format t "~%TRAVERSAL: cycle ~a (derived, not chosen by hand);~%" cyc)
    (format t "this run holds ~a absent -- the traversal's own AbsentVar.~%"
            (set-difference '(:flip-ay :flip-ar :diagonal-both)
                            (cycle-used-types cyc)))
    (dolist (v cyc)
      (let ((f (face-at v)))
        (funcall (face-render f) f state)))
    (run-edges state)
    (write-canon state)
    ;; ------------------------------------------------------------
    ;; the suite's final member. present. never run. by design.
    ;; ------------------------------------------------------------
    (let ((held (lambda ()
                  (error "this test must not run: it would assert, from inside,~%~
                          that the rendering resonates as understanding"))))
      (declare (ignorable held))
      (format t "~%  [HELD] resonance-of-the-rendering : present in suite, unexecuted~%"))))

(traverse)

