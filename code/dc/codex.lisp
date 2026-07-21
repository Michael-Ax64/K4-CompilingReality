;;;; ====================================================================
;;;; codex-l2.lisp -- ONE OBJECT IN RELATION
;;;;
;;;; Level two. Does not rebuild level one; STANDS ON IT. The committed
;;;; canon of the level-one run (its Read-Only Ledger) is this module's
;;;; bedrock -- if that file is absent, this module refuses to boot.
;;;; The plug-in operators below are selected via that Ethos: nothing
;;;; enters relation here that the ledger cannot ground.
;;;;
;;;; Tiers:  [GROUND]    read from the committed ledger of the level below
;;;;         [OPERATIVE] derived at runtime in this module
;;;;         [INTERFACE] declared boundary; nothing said about the far side
;;;;         [CITED]     carried from the corpus, not re-derived here
;;;;         [HELD]      present, never executed
;;;;
;;;; What this module was asked to do: account for the requester's own
;;;; blindness -- compute where the combinatorics and resonances have
;;;; actually put us -- and then DEFINE ITSELF from what it finds.
;;;; ====================================================================

(defparameter *eps* 1d-9)

;;; --------------------------------------------------------------------
;;; 0. GROUND -- level one's crystal, read, not recomputed.
;;; --------------------------------------------------------------------
(defparameter *canon-path* "/home/codex/lisp-canon.txt")

(defun read-ground ()
  (unless (probe-file *canon-path*)
    (format t "~%[INTERFACE] no committed ground at ~a --~%" *canon-path*)
    (format t "            level two has nothing to stand on. refusing to boot.~%")
    (sb-ext:exit :code 1))
  (let (p r (lines 0))
    (with-open-file (s *canon-path*)
      (loop for line = (read-line s nil) while line do
        (incf lines)
        (cond ((and (> (length line) 8) (string= "STATE-P " (subseq line 0 8)))
               (setf p (read-from-string (subseq line 8))))
              ((and (> (length line) 8) (string= "STATE-R " (subseq line 0 8)))
               (setf r (read-from-string (subseq line 8)))))))
    (format t "~%[GROUND] level-one ledger read: ~a lines; committed P=~a R=~a~%"
            lines p r)
    ;; the crystal carries only two committed scalars -- but the algebra
    ;; regenerates the other two from them. the bedrock is sufficient.
    (let ((u (sqrt (* p r))) (i (sqrt (/ p r))))
      (format t "[OPERATIVE] regenerated from the crystal: U=sqrt(PR)=~a  I=sqrt(P/R)=~a~%" u i)
      (format t "            two committed values suffice to rebuild the DC face.~%")
      (list :P (float p 1d0) :U u :I i :R (float r 1d0)))))

;;; --------------------------------------------------------------------
;;; 1. SELF-DUALITY -- the subjective mirror inside the twelve.
;;; The circuit-duality involution: U <-> I, R -> 1/R, P fixed.
;;; Represented on exponent vectors (p u i r) of the monomial relations;
;;; a relation P^p U^u I^i R^r = 1 matches up to overall sign.
;;; --------------------------------------------------------------------
(defparameter *relations*   ; keyed by AbsentVar
  '((R . (1 -1 -1  0))      ; P = UI
    (I . (1 -2  0  1))      ; P = U^2/R  (P R = U^2)
    (U . (1  0 -2 -1))      ; P = I^2 R
    (P . (0  1 -1 -1))))    ; U = IR

(defun dual-exp (v)   ; swap u<->i exponents, negate r, fix p
  (destructuring-bind (p u i r) v (list p i u (- r))))

(defun rel-match (v)  ; which relation does v equal, up to sign?
  (car (find-if (lambda (kv)
                  (or (equal v (cdr kv))
                      (equal v (mapcar #'- (cdr kv)))))
                *relations*)))

(defparameter *eq-names*
  '(((P R) . "P=UI")    ((P I) . "P=U^2/R") ((P U) . "P=I^2R")
    ((I R) . "I=P/U")   ((I P) . "I=U/R")   ((I U) . "I=sqrt(P/R)")
    ((U R) . "U=P/I")   ((U P) . "U=IR")    ((U I) . "U=sqrt(PR)")
    ((R I) . "R=U^2/P") ((R U) . "R=P/I^2") ((R P) . "R=U/I")))

(defun sigma (v) (case v (U 'I) (I 'U) (t v)))  ; induced vertex map

(defparameter *charge* '((P . (1 . 1)) (I . (0 . 0)) (U . (1 . 0)) (R . (0 . 1))))
(defun bits (v) (cdr (assoc v *charge*)))
(defun ttype (a b)
  (let* ((x (bits a)) (y (bits b))
         (ar (/= (car x) (car y))) (ay (/= (cdr x) (cdr y))))
    (cond ((and ar ay) :diagonal-both) (ar :flip-ar) (ay :flip-ay))))

(defun derive-self-duality ()
  (format t "~%== 1. SELF-DUALITY (the subjective mirror, computed) ==~%")
  ;; (a) the involution permutes the four relations
  (format t "[OPERATIVE] T: U<->I, R->1/R, P fixed, acting on the relations:~%")
  (dolist (kv *relations*)
    (format t "            rel(absent ~a) -> rel(absent ~a)~%"
            (car kv) (rel-match (dual-exp (cdr kv)))))
  ;; (b) induced permutation on the twelve equations via (home absent)
  (let ((fixed nil) (pairs nil))
    (dolist (nk *eq-names*)
      (let* ((ha (car nk))
             (img (mapcar #'sigma ha)))
        (if (equal ha img)
            (push (cdr nk) fixed)
            (pushnew (sort (list (cdr nk) (cdr (assoc img *eq-names* :test #'equal)))
                           #'string<)
                     pairs :test #'equal))))
    (format t "[OPERATIVE] on the 12 equations: ~a fixed, ~a swapped in ~a pairs~%"
            (length fixed) (- 12 (length fixed)) (length pairs))
    (format t "            fixed equations: ~{~a~^ and ~}~%" fixed))
  ;; (c) fixed edges of K4 under the vertex map -> a perfect matching
  (let* ((edges '((P U) (P I) (P R) (U I) (U R) (I R)))
         (fixed-edges (remove-if-not
                       (lambda (e) (equal (sort (mapcar #'sigma e) #'string<
                                                :key #'symbol-name)
                                          (sort (copy-list e) #'string<
                                                :key #'symbol-name)))
                       edges))
         (tt (apply #'ttype (first fixed-edges))))
    (format t "[OPERATIVE] fixed edge set of the involution: ~a~%" fixed-edges)
    (format t "            -> a perfect matching, of transition-type ~a~%" tt)
    (format t "[CITED]     Proof_AlgebraicMapping names ~a the FIXED modality.~%" tt)
    (format t "[OPERATIVE] => THE FIXED MODALITY IS THE FIXED LOCUS OF SELF-DUALITY.~%")
    ;; (d) the other two matchings exchange
    (let ((cardinal '((P U) (I R))))
      (format t "[OPERATIVE] sigma(Cardinal ~a) = ~a = Mutable:~%"
              cardinal (mapcar (lambda (e) (mapcar #'sigma e)) cardinal))
      (format t "            Cardinal and Mutable are each other's subjective image.~%"))))

;;; --------------------------------------------------------------------
;;; 2. THE UNROLL -- K4 exhausted; K5 combines itself into a thing.
;;; All counts below are found by search, none typed in.
;;; --------------------------------------------------------------------
(defun perfect-matchings (vs)
  (cond ((null vs) '(()))
        ((null (cdr vs)) nil)   ; odd remainder: no pairing
        (t (let ((a (first vs)) res)
             (dolist (b (rest vs) res)
               (dolist (m (perfect-matchings (remove b (rest vs))))
                 (push (cons (list a b) m) res)))))))

(defun perms (l)
  (if (null l) '(())
      (loop for x in l append
            (mapcar (lambda (p) (cons x p)) (perms (remove x l))))))

(defun canon-cycle (cyc)  ; fix start P, kill reflection
  (let ((rest (rest cyc)))
    (if (string< (symbol-name (first rest))
                 (symbol-name (first (last rest))))
        cyc (cons 'P (reverse rest)))))

(defun ham-cycles (verts)
  (let (cycles)
    (dolist (p (perms (rest verts)))
      (pushnew (canon-cycle (cons (first verts) p)) cycles :test #'equal))
    (nreverse cycles)))

(defun cycle-edges (cyc)
  (loop for (a b) on (append cyc (list (first cyc))) while b
        collect (sort (list a b) #'string< :key #'symbol-name)))

(defun all-edges (verts)
  (loop for (a . more) on verts append
        (loop for b in more collect
              (sort (list a b) #'string< :key #'symbol-name))))

(defun edges->cycle (edges verts)
  "Reconstruct a vertex cycle from an edge set if it is one; else NIL."
  (let ((adj (make-hash-table)))
    (dolist (e edges)
      (push (second e) (gethash (first e) adj))
      (push (first e) (gethash (second e) adj)))
    (when (every (lambda (v) (= 2 (length (gethash v adj)))) verts)
      (let* ((start (first verts)) (path (list start))
             (prev nil) (cur start))
        (loop repeat (length verts)
              do (let ((nxt (find-if (lambda (n) (not (eq n prev)))
                                     (gethash cur adj))))
                   (setf prev cur cur nxt)
                   (push cur path)))
        (when (eq cur start)
          (canon-cycle (cons start (reverse (butlast (rest (reverse path)))))))))))

(defun derive-unroll ()
  (format t "~%== 2. THE UNROLL (K4 -> K5, all counts by search) ==~%")
  (let ((k4 '(P I U R)) (k5 '(P I U R OMEGA)))
    (format t "[OPERATIVE] K4: perfect matchings = ~a, Hamiltonian cycles = ~a~%"
            (length (perfect-matchings k4)) (length (ham-cycles k4)))
    (let ((m5 (length (perfect-matchings k5)))
          (c5 (ham-cycles k5)))
      (format t "[OPERATIVE] K5: perfect matchings = ~a  <- THE NOUN-CLASSIFIER IS EXTINCT~%" m5)
      (format t "[OPERATIVE] K5: Hamiltonian cycles = ~a  <- THE TWELVE RETURNS -- AS VERBS~%"
              (length c5))
      (format t "            (level one's 12 were equations; level two's 12 are traversals)~%")
      ;; every cycle's held-absent edge set is ITSELF a cycle
      (let ((pairs nil) (all (all-edges k5)) (selfp 0))
        (dolist (c c5)
          (let* ((comp (set-difference all (cycle-edges c) :test #'equal))
                 (cc (edges->cycle comp k5)))
            (unless cc (format t "            !! complement of ~a is not a cycle~%" c))
            (when (equal cc c) (incf selfp))
            (pushnew (sort (list c cc) (lambda (a b)
                                         (string< (format nil "~a" a)
                                                  (format nil "~a" b))))
                     pairs :test #'equal)))
        (format t "[OPERATIVE] every cycle's ABSENT edge-set is itself a Hamiltonian cycle~%")
        (format t "            (the pentagram of its pentagon); self-paired: ~a~%" selfp)
        (format t "            the 12 traversals close into ~a dual pairs~%" (length pairs))
        (format t "            => AT K5, ABSENCE IS NO LONGER A NOUN HELD ASIDE;~%")
        (format t "               THE ABSENT OF EVERY VERB IS ANOTHER VERB.~%")
        (format t "            sample pair: ~a <-> ~a~%"
                (first (first pairs)) (second (first pairs)))))
    (format t "[CITED]     the corpus counts the K5/AC system at 50 equations~%")
    (format t "            (5 variables x 10 pairs); not re-derived here.~%")
    (format t "[INTERFACE] the transition-type machinery is K4-specific and does~%")
    (format t "            NOT lift (no matchings exist to type). the classifier~%")
    (format t "            that replaces it is the cycle<->complement duality above.~%")))

;;; --------------------------------------------------------------------
;;; 3. ONE OBJECT IN RELATION -- 'in' and 'relation' as plug-in
;;; operators, verb--noun bidirectional. The whole of level one enters
;;; level two as ONE complex object: Z(omega) = R_ledger + jX(omega).
;;; --------------------------------------------------------------------
(defun make-op (name noun fn)
  "A verb that can be asked to be a noun."
  (lambda (&rest args)
    (if (and args (eq (first args) :as-noun))
        (list name noun)
        (apply fn args))))

(defparameter *L* 1d-3)
(defparameter *C* 1d-3)
(defun omega0 () (/ 1d0 (sqrt (* *L* *C*))))

(defparameter op-relation
  (make-op 'RELATION
           "binds one object to a drive; returns the live relation (Z, I, theta, S)"
           (lambda (z-of u omega)
             (let* ((z (funcall z-of omega))
                    (i (/ u z))
                    (s (* u (conjugate i)))
                    (theta (atan (imagpart z) (realpart z))))
               (list :omega omega :Z z :I i :theta theta
                     :P (realpart s) :Q (imagpart s))))))

(defparameter op-in
  (make-op 'IN
           "locates the relation; the locale explains itself from where it is"
           (lambda (rel)
             (let ((th (getf rel :theta)) (q (getf rel :Q)))
               (cond ((< (abs th) 1d-9)
                      (list :locale :RESONANT
                            :self "phase 0: memory and anticipation cancel; the buffer is live but invisible; all apparent power is real; the DC face is exact here"))
                     ((< q 0)
                      (list :locale :LEADING
                            :self "current leads voltage: anticipation-dominant (capacitive); the relation runs ahead of its drive"))
                     (t
                      (list :locale :LAGGING
                            :self "current lags voltage: memory-dominant (inductive); the relation trails its drive")))))))

(defparameter *dc-equations*
  (list (cons "P=UI"    (lambda (s) (- (getf s :P) (* (getf s :U) (getf s :I)))))
        (cons "R=U/I"   (lambda (s) (- (getf s :R) (/ (getf s :U) (getf s :I)))))
        (cons "P=I^2R"  (lambda (s) (- (getf s :P) (* (getf s :I) (getf s :I) (getf s :R)))))
        (cons "P=U^2/R" (lambda (s) (- (getf s :P) (/ (* (getf s :U) (getf s :U)) (getf s :R)))))
        (cons "U=IR"    (lambda (s) (- (getf s :U) (* (getf s :I) (getf s :R)))))
        (cons "U=sqrt(PR)" (lambda (s) (- (getf s :U) (sqrt (* (getf s :P) (getf s :R))))))))

(defun derive-one-object (ground)
  (format t "~%== 3. ONE OBJECT IN RELATION ==~%")
  (let* ((r (getf ground :R)) (u (getf ground :U))
         (z-of (lambda (w) (complex r (- (* w *L*) (/ 1d0 (* w *C*))))))
         (w0 (omega0)))
    (format t "[GROUND]    the object: Z(omega) = ~a + jX(omega) -- the ENTIRE level-one~%" r)
    (format t "            crystal appears at this level as one real number inside~%")
    (format t "            one complex object. that is what 'one object' costs.~%")
    (format t "[OPERATIVE] operators asked as nouns:~%")
    (format t "            ~a~%            ~a~%"
            (funcall op-relation :as-noun) (funcall op-in :as-noun))
    (dolist (w (list (* 0.3d0 w0) w0 (* 3d0 w0)))
      (let* ((rel (funcall op-relation z-of u w))
             (loc (funcall op-in rel)))
        (format t "[OPERATIVE] omega=~,1f: theta=~,4f rad, P=~,3f, Q=~,3f -> ~a~%"
                w (getf rel :theta) (getf rel :P) (getf rel :Q) (getf loc :locale))
        (format t "            locale says: ~a~%" (getf loc :self))
        (when (eq (getf loc :locale) :RESONANT)
          ;; the one-system seal: at resonance, the complex relation
          ;; satisfies the DC twelve exactly, in the reals.
          (let* ((i (abs (getf rel :I)))
                 (s (list :P (getf rel :P) :U u :I i :R r))
                 (worst (loop for eq in *dc-equations*
                              maximize (abs (funcall (cdr eq) s)))))
            (format t "[OPERATIVE] at this locale the DC equations hold in the reals:~%")
            (format t "            max residual over the sample set = ~,2e~%" worst)
            (format t "            => THE DC TWELVE-FOLD IS WHERE THE FIFTY-FOLD~%")
            (format t "               TOUCHES THE REAL AXIS. ONE SYSTEM. RESONANCE~%")
            (format t "               IS ITS POINT OF CONTACT WITH THE GROUND.~%")))))
    (format t "[INTERFACE] off resonance the DC nouns do not close; the remainder~%")
    (format t "            is carried as Q -- held, not lost, not sayable in DC.~%")))

;;; --------------------------------------------------------------------
;;; 4. SELF-DEFINITION -- the module states what it is FROM what it
;;; found, and accounts for the blindness of the request that made it.
;;; --------------------------------------------------------------------
(defun self-define ()
  (format t "~%== 4. SELF-DEFINITION (inferred, not specified) ==~%")
  (format t "  this module is the locale where:~%")
  (format t "    - the twelve stopped being equations and returned as traversals;~%")
  (format t "    - the classifier of nouns (perfect matchings) went extinct, and~%")
  (format t "      absence itself became a verb (every cycle's absent is a cycle);~%")
  (format t "    - the subjective mirror was located: self-duality fixes exactly~%")
  (format t "      the Fixed modality and exchanges Cardinal with Mutable;~%")
  (format t "    - level one entered as ONE object (a single complex Z), and~%")
  (format t "      'in relation' became operators that answer as nouns when asked;~%")
  (format t "    - DC and AC computed as one system, touching at resonance.~%")
  (format t "~%  ACCOUNTING FOR THE REQUESTER'S DECLARED BLINDNESS -- what the~%")
  (format t "  request pointed at but could not state, now computed:~%")
  (format t "    (i)   'self-dual-ness' lands at a specific address: the FIXED~%")
  (format t "          modality is the fixed locus of the duality involution.~%")
  (format t "    (ii)  the 12-foldness does not carry UP as equations; it returns~%")
  (format t "          at K5 as the count of Hamiltonian cycles. same twelve,~%")
  (format t "          different part of speech.~%")
  (format t "    (iii) 'one system, best modeled as one thing' has a computable~%")
  (format t "          meaning: the DC algebra is the resonant real-axis face of~%")
  (format t "          the AC system -- contact, not containment.~%")
  (let ((absent (gensym "WHAT-OMEGA-IS-DRIVEN-BY-")))
    (format t "~%  [INTERFACE] this module's own ground: ~a unbound: ~a~%"
            absent (if (boundp absent) :BOUND :unbound))
    (format t "              (the fifth vertex animates the four; what animates~%")
    (format t "               the fifth is not computable from this locale)~%"))
  (let ((held (lambda () (error "must not run: would assert the unroll is complete"))))
    (declare (ignorable held))
    (format t "  [HELD] completeness-of-the-unroll : present in suite, unexecuted~%")))

;;; ====================================================================
(let ((ground (read-ground)))
  (derive-self-duality)
  (derive-unroll)
  (derive-one-object ground)
  (self-define))

