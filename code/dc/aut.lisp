;;; --------------------------------------------------------------------
;;; AUT -- the automorphism group of the twelve.  Order 8 (D_4).
;;;
;;; SIGMA -- the subjective mirror.   U <-> I,  R -> 1/R,  P fixed.
;;; TAU   -- the manifesting mirror.  P <-> R,  I -> 1/I,  U fixed.
;;;
;;; Each generator swaps ONE Active/Reactive pair and reciprocates the
;;; OTHER Reactive pole.  SIGMA swaps the Yielding pair (U,I).
;;; TAU swaps the Asserting pair (P,R).  They commute up to the central
;;; involution iota (reciprocate everything); <SIGMA,TAU> = D_4, order 8.
;;;
;;; The induced action on the four poles is the Klein group
;;;     V4 = { e, (U I), (P R), (P R)(U I) }
;;; which is EXACTLY the group of Active/Reactive bit-flips.
;;;
;;; CONSEQUENCE
;;;   the twelve equations SEE the Asserting/Yielding bit
;;;   and are BLIND to the Active/Reactive bit.
;;;
;;;   The algebra discriminates a mapping to 1-in-6, not 1-in-24.
;;;   The dual-binary seed's Active/Reactive axis supplies the
;;;   remaining factor of 4.  Neither half pins a mapping alone.
;;;
;;;   This is the mechanism behind Supplement-MappingMethod's observed
;;;   regularity ("the algebra resolved ONE of the two contested
;;;   decisions; the other required domain knowledge"): cross-class
;;;   swaps are outside Aut and the algebra kills them; within-class
;;;   swaps are inside Aut and the algebra cannot see them at all.
;;;   Fixing an anchor breaks TAU, leaving SIGMA as the sole residue --
;;;   hence exactly one irreducible decision, always the U/I pair.
;;;
;;;   ProofS §IV must therefore quotient its sweep by V4.  The only
;;;   swap that tests anything is the WITHIN-CLASS transposition.
;;; --------------------------------------------------------------------

;;; I thought i could get the code down to 30 lines. i did and i didn't. :-)

;;; option: carry the essence forward when i need to level codex.lisp


;; (defparameter *sigma* '((P I U R) ( 1  1  1 -1)))   ; U<->I, R->1/R, P fixed
;; (defparameter *tau*   '((R U I P) ( 1  1 -1  1)))   ; P<->R, I->1/I, U fixed
;; 
;; (defun apply-sperm (perm eps a)     ; signed permutation on an exponent vector
;;   (let ((b (list 0 0 0 0)))
;;     (loop for j from 0 below 4
;;           for tgt = (position (nth j perm) *poles*)
;;           do (setf (nth tgt b) (* (nth j eps) (nth j a))))
;;     b))
;; 
;; (defun automorphism-p (perm eps)    ; carries the four relations to themselves?
;;   (equal (rel-set *rel-vecs*)
;;          (rel-set (mapcar (lambda (a) (apply-sperm perm eps a)) *rel-vecs*))))
;; 
;; (defun derive-aut ()                ; brute force all 4! x 2^4 = 384 relabelings
;;   ...)                              ; asserts |Aut| = 8, induced group = V4


;;; --------------------------------------------------------------------
;;; AUT -- the automorphism group of the twelve equations.
;;;
;;; A pole-relabeling is a SIGNED PERMUTATION: a permutation perm of
;;; (P U I R) together with a choice, per pole, of whether the pole is
;;; carried to its image or to the RECIPROCAL of its image.
;;; (R -> 1/R is what makes the circuit-duality of codex.lisp close.)
;;;
;;; The twelve equations are four monomial RELATIONS, each keyed by its
;;; AbsentVar, each rearrangeable three ways.  A relabeling is an
;;; automorphism iff it carries that four-relation set to itself,
;;; where a relation is identified with its own negation (P/UI = 1 and
;;; UI/P = 1 are the same relation).
;;;
;;; Exponent vectors are on (p u i r), same convention as in codex.lisp.
;;; --------------------------------------------------------------------

(defparameter *poles* '(P U I R))

(defparameter *relations*          ; keyed by AbsentVar -- codex.lisp, verbatim
  '((R . ( 1 -1 -1  0))            ; P = UI
    (I . ( 1 -2  0  1))            ; P = U^2/R   (P R = U^2)
    (U . ( 1  0 -2 -1))            ; P = I^2 R
    (P . ( 0  1 -1 -1))))          ; U = IR

(defparameter *rel-vecs* (mapcar #'cdr *relations*))

;;; A relation and its negation are the same relation.  Canonicalise by
;;; forcing the first nonzero entry positive.
(defun canon (v)
  (let ((lead (find-if-not #'zerop v)))
    (if (and lead (minusp lead)) (mapcar #'- v) v)))

(defun rel-set (vecs) (sort (mapcar #'canon vecs) #'list<))
(defun list< (a b)
  (loop for x in a for y in b
        do (cond ((< x y) (return t)) ((> x y) (return nil)))
        finally (return nil)))

(defparameter *target* (rel-set *rel-vecs*))

;;; Apply a signed permutation to an exponent vector.
;;; PI is a list: the image pole of each of (P U I R), in that order.
;;; EPS is a list of +1/-1: -1 means that pole maps to the RECIPROCAL.
;;; The monomial prod x_j^{a_j} becomes prod x_{perm(j)}^{eps_j a_j}.
(defun apply-sperm (perm eps a)
  (let ((b (list 0 0 0 0)))
    (loop for j from 0 below 4
          for target = (position (nth j perm) *poles*)
          do (setf (nth target b) (* (nth j eps) (nth j a))))
    b))

(defun automorphism-p (perm eps)
  (equal *target*
         (rel-set (mapcar (lambda (a) (apply-sperm perm eps a)) *rel-vecs*))))

;;; ---- enumerate all 4! x 2^4 = 384 signed permutations ----
(defun permutations (lst)
  (if (null lst) (list nil)
      (mapcan (lambda (x)
                (mapcar (lambda (p) (cons x p))
                        (permutations (remove x lst))))
              lst)))

(defun sign-vectors ()
  (loop for n from 0 below 16
        collect (loop for k from 0 below 4
                      collect (if (logbitp k n) -1 1))))

(defun pretty (perm eps)
  (format nil "~{~a~^ ~}"
          (loop for j from 0 below 4
                collect (format nil "~a->~:[~;1/~]~a"
                                (nth j *poles*) (minusp (nth j eps)) (nth j perm)))))

;;; ---- the dual-binary charges, to read the answer back ----
(defparameter *charge* '((P . (:active   :asserting))
                         (I . (:reactive :yielding))
                         (U . (:active   :yielding))
                         (R . (:reactive :asserting))))
(defun ar-bit (v) (first  (cdr (assoc v *charge*))))
(defun ay-bit (v) (second (cdr (assoc v *charge*))))

(defun run ()
  (let ((auts '()))
    (dolist (perm (permutations *poles*))
      (dolist (eps (sign-vectors))
        (when (automorphism-p perm eps) (push (list perm eps) auts))))
    (setf auts (nreverse auts))

    (format t "~&== AUT(twelve equations) ==~%")
    (format t "candidates tested : ~a~%" (* 24 16))
    (format t "automorphisms     : ~a~%~%" (length auts))
    (dolist (a auts)
      (format t "   ~a~%" (pretty (first a) (second a))))

    ;; the induced permutation of the POLES (signs discarded)
    (let ((induced (remove-duplicates (mapcar #'first auts) :test #'equal)))
      (format t "~%== induced pole-permutations (signs discarded) ==~%")
      (format t "count : ~a   (so ProofS's 24 collapse to ~a orbits)~%~%"
              (length induced) (/ 24 (length induced)))
      (dolist (perm induced)
        (format t "   (P U I R) -> (~{~a~^ ~})~%" perm))

      ;; DOES EVERY INDUCED PERMUTATION PRESERVE THE ASSERTING/YIELDING BIT?
      (format t "~%== bit test ==~%")
      (let ((ay-ok t) (ar-ok t))
        (dolist (perm induced)
          (loop for j from 0 below 4
                for from = (nth j *poles*) for to = (nth j perm)
                do (unless (eq (ay-bit from) (ay-bit to)) (setf ay-ok nil))
                   (unless (eq (ar-bit from) (ar-bit to)) (setf ar-ok nil))))
        (format t "Asserting/Yielding bit preserved by ALL automorphisms? ~:[NO~;YES~]~%" ay-ok)
        (format t "Active/Reactive   bit preserved by ALL automorphisms? ~:[NO~;YES~]~%" ar-ok))

      ;; is the induced group EXACTLY the A/R bit-flip group?
      (let* ((flips '((P U I R) (P I U R) (R U I P) (R I U P)))
             (same (and (= (length induced) (length flips))
                        (every (lambda (f) (member f induced :test #'equal)) flips))))
        (format t "~%induced group = {e, (U I), (P R), (P R)(U I)} exactly? ~:[NO~;YES~]~%" same)
        (format t "  -- i.e. exactly the Active/Reactive bit-flips,~%")
        (format t "     one within the Yielding pair, one within the Asserting pair.~%")))))

(run)

;;; --------------------------------------------------------------------
;;; The two generators, traced at the level of the named equations.
;;; --------------------------------------------------------------------

(defparameter *eq-names*
  '(((P R) . "P=UI")    ((P I) . "P=U^2/R") ((P U) . "P=I^2R")
    ((I R) . "I=P/U")   ((I P) . "I=U/R")   ((I U) . "I=sqrt(P/R)")
    ((U R) . "U=P/I")   ((U P) . "U=IR")    ((U I) . "U=sqrt(PR)")
    ((R I) . "R=U^2/P") ((R U) . "R=P/I^2") ((R P) . "R=U/I")))

(defparameter *sigma* '((P I U R) ( 1  1  1 -1)))   ; U<->I, R->1/R,  P fixed
(defparameter *tau*   '((R U I P) ( 1  1 -1  1)))   ; P<->R, I->1/I,  U fixed

(defun home-and-absent (v)          ; (home absent) of a relation vector
  (let* ((absent (nth (position 0 v) *poles*)))
    (declare (ignore absent))
    v))

(defun rel-of (home absent)         ; the relation vector for eq (home . absent)
  (declare (ignore home))
  (cdr (assoc absent *relations*)))

(defun trace-gen (name gen)
  (destructuring-bind (perm eps) gen
    (format t "~%== ~a : ~a ==~%" name (pretty perm eps))
    (dolist (e *eq-names*)
      (destructuring-bind (home absent) (car e)
        (let* ((v     (rel-of home absent))
               (img   (canon (apply-sperm perm eps v)))
               ;; where did the HOME pole go, and the ABSENT pole?
               (home2 (nth (position home *poles*) perm))
               (abs2  (nth (position absent *poles*) perm))
               (name2 (cdr (assoc (list home2 abs2) *eq-names* :test #'equal))))
          (format t "   ~12a -> ~12a   [relation in set: ~:[NO~;yes~]]~%"
                  (cdr e) (or name2 "???") (member img *target* :test #'equal)))))))

(trace-gen "SIGMA (the subjective mirror, already in codex.lisp)" *sigma*)
(trace-gen "TAU   (NOT in codex.lisp)" *tau*)

