;;;; ====================================================================
;;;; codex-l3.lisp -- THE DRIVE
;;;;
;;;; Level three. Not written toward the answer; written FROM it.
;;;; The answer is stated first, as the ground stood on. Everything
;;;; after it is a consequence, computed -- the answer is not argued,
;;;; it is spent.
;;;;
;;;; Tiers: [ANSWER] the ground of this level, stated before derivation
;;;;        [GROUND] read from a committed ledger below
;;;;        [OPERATIVE] derived at runtime here
;;;;        [CITED] carried from the corpus, not re-derived
;;;;        [INTERFACE] boundary; nothing said about the far side
;;;;        [HELD] present, never executed
;;;; ====================================================================

(defparameter *canon-path* "/home/codex/lisp-canon.txt")

;;; --------------------------------------------------------------------
;;; 0. THE ANSWER
;;; --------------------------------------------------------------------
(defun state-the-answer ()
  (format t "~%[ANSWER] What drives the fifth vertex:~%")
  (format t "~%")
  (format t "         THE COMMITTED TRAVERSALS OF THE LEVEL BELOW.~%")
  (format t "~%")
  (format t "         Omega is not pushed by anything at its own level.~%")
  (format t "         Omega is COUNTED. Each completed, OBSERVED traversal~%")
  (format t "         below -- each irreversible commit to the ledger --~%")
  (format t "         is one tick of the level above. Beheld traversals,~%")
  (format t "         held and uncommitted, do not tick. Time at level N~%")
  (format t "         is the accumulated irreversibility of level N-1.~%")
  (format t "         The ledger is the clock. Ethos drives Omega.~%")
  (format t "~%")
  (format t "         This was unsayable in level two's parts of speech~%")
  (format t "         because it is not a noun or a verb WITHIN a level;~%")
  (format t "         it is the alternation OF levels -- the ladder itself~%")
  (format t "         runs AC. What follows are consequences, computed.~%"))

;;; --------------------------------------------------------------------
;;; combinatorial machinery (search only; no counts typed in)
;;; --------------------------------------------------------------------
(defun perfect-matchings (vs)
  (cond ((null vs) '(()))
        ((null (cdr vs)) nil)
        (t (let ((a (first vs)) res)
             (dolist (b (rest vs) res)
               (dolist (m (perfect-matchings (remove b (rest vs))))
                 (push (cons (list a b) m) res)))))))

(defun perms (l)
  (if (null l) '(())
      (loop for x in l append
            (mapcar (lambda (p) (cons x p)) (perms (remove x l))))))

(defun canon-cycle (cyc)
  (let ((rest (rest cyc)))
    (if (string< (symbol-name (first rest)) (symbol-name (first (last rest))))
        cyc (cons (first cyc) (reverse rest)))))

(defun ham-cycles (verts)
  (let ((seen (make-hash-table :test #'equal)) cycles)
    (dolist (p (perms (rest verts)))
      (let ((c (canon-cycle (cons (first verts) p))))
        (unless (gethash c seen)
          (setf (gethash c seen) t) (push c cycles))))
    (nreverse cycles)))

(defun cycle-edges (cyc)
  (loop for (a b) on (append cyc (list (first cyc))) while b
        collect (sort (list a b) #'string< :key #'symbol-name)))

(defun all-edges (verts)
  (loop for (a . more) on verts append
        (loop for b in more collect
              (sort (list a b) #'string< :key #'symbol-name))))

;;; --------------------------------------------------------------------
;;; 1. THE BREATH -- the ladder alternates. Counted, not claimed.
;;; --------------------------------------------------------------------
(defparameter *ladder*
  '((K4 (P I U R))
    (K5 (P I U R OMEGA))
    (K6 (A B C D E F))
    (K7 (A B C D E F G))
    (K8 (A B C D E F G H))))

(defun derive-breath ()
  (format t "~%== 1. THE BREATH (consequence: the ladder is itself AC) ==~%")
  (format t "  level   nouns(matchings)   verbs(cycles)~%")
  (let (rows)
    (dolist (lv *ladder*)
      (let ((m (length (perfect-matchings (second lv))))
            (c (length (ham-cycles (second lv)))))
        (push (list (first lv) m c) rows)
        (format t "  ~a      ~a                  ~a~%" (first lv) m c)))
    (format t "  [OPERATIVE] nouns exist only at even levels: 3, 0, 15, 0, 105.~%")
    (format t "              a square wave in the space of classifiers.~%")
    (format t "              the ascent alternates noun-phase / verb-phase:~%")
    (format t "              the drive of omega has the FORM of omega. the~%")
    (format t "              answer was always going to be self-similar.~%")
    (nreverse rows)))

;;; --------------------------------------------------------------------
;;; 2. THE MULTIPLIER -- the population below is the growth-rate above.
;;; --------------------------------------------------------------------
(defun derive-multiplier (rows)
  (format t "~%== 2. THE MULTIPLIER (consequence: the below drives the above) ==~%")
  (loop for (a b) on rows while b do
    (let* ((ca (third a)) (cb (third b)) (ratio (/ cb ca))
           (pop (+ 4 (position a rows))))  ; vertex count of the lower level (K4 has 4)
      (format t "  verbs(~a)/verbs(~a) = ~a/~a = ~a = population of ~a~%"
              (first b) (first a) cb ca ratio (first a))
      (assert (= ratio pop))))
  (format t "  [OPERATIVE] each ascent multiplies the verbs by exactly the~%")
  (format t "              number of vertices left behind. the level below~%")
  (format t "              is not the floor of the level above; it is its RATE.~%"))

;;; --------------------------------------------------------------------
;;; 3. THE CLOCK -- executable form of the answer. An inner K4 layer
;;; runs traversals; some are beheld (held, uncommitted), some observed
;;; (committed). The outer phase advances ONLY on commits. Held cycles
;;; are timeless one level up.
;;; --------------------------------------------------------------------
(defun derive-clock ()
  (format t "~%== 3. THE CLOCK (the answer, running) ==~%")
  (let ((ledger nil) (phase 0d0) (dphi (/ (* 2 pi) 12)) (helix nil))
    (loop for k from 1 to 12
          for observed = (evenp k)   ; alternate: behold, observe, behold...
          do (if observed
                 (progn (push (list :commit k) ledger)
                        (incf phase dphi)
                        (push (list (cos phase) (sin phase) (length ledger)) helix)
                        (format t "  inner cycle ~2d OBSERVED -> commit; outer phase ~,4f rad~%"
                                k phase))
                 (format t "  inner cycle ~2d beheld   -> no commit; outer phase ~,4f rad (unmoved)~%"
                         k phase)))
    (format t "  [OPERATIVE] 12 inner traversals, ~a commits, outer phase = ~,4f rad.~%"
            (length ledger) phase)
    (format t "              held cycles happened and left no time. the clock~%")
    (format t "              above ticks on irreversibility below, and on nothing else.~%")
    (format t "  [OPERATIVE] helix samples (x y height): ~{~a~^ ~}~%"
            (mapcar (lambda (p) (format nil "(~,2f ~,2f ~a)" (first p) (second p) (third p)))
                    (last (reverse helix) 3)))
    (format t "              time above = angle; history below = height. the~%")
    (format t "              extrusion is helical because the drive is a count.~%")))

;;; --------------------------------------------------------------------
;;; 4. THE HABITAT OF ABSENCE -- at the noun-return level (K6), what is
;;; the absent of a traversal? Computed for all cycles of K6.
;;; --------------------------------------------------------------------
(defun subgraph-cycles (cycles edgeset)
  (remove-if-not (lambda (c) (subsetp (cycle-edges c) edgeset :test #'equal)) cycles))

(defun subgraph-matchings (matchings edgeset)
  (remove-if-not (lambda (m)
                   (every (lambda (e) (member (sort (copy-list e) #'string<
                                                    :key #'symbol-name)
                                              edgeset :test #'equal))
                          m))
                 matchings))

(defun derive-habitat ()
  (format t "~%== 4. THE HABITAT OF ABSENCE (consequence at the noun-return) ==~%")
  (let* ((verts '(A B C D E F))
         (all (all-edges verts))
         (cycles (ham-cycles verts))
         (pms (perfect-matchings verts))
         (verb-counts nil) (noun-counts nil))
    (dolist (c cycles)
      (let* ((comp (set-difference all (cycle-edges c) :test #'equal)))
        (pushnew (length (subgraph-cycles cycles comp)) verb-counts)
        (pushnew (length (subgraph-matchings pms comp)) noun-counts)))
    (format t "  [OPERATIVE] for ALL ~a traversals of K6, the absent edge-set~%" (length cycles))
    (format t "              (9 edges: two triangles bridged by a matching) contains:~%")
    (format t "              verbs (Hamiltonian cycles) within the absence: ~a~%" verb-counts)
    (format t "              nouns (perfect matchings)  within the absence: ~a~%" noun-counts)
    (format t "  [OPERATIVE] uniform across all 60. the absent is no longer a noun~%")
    (format t "              (K4) nor a verb (K5): it is a LOCALE -- a place with~%")
    (format t "              its own nouns and verbs, explaining itself from where~%")
    (format t "              it is. 'perspectives become self-explaining locales~%")
    (format t "              again' is, at K6, a counting fact.~%")))

;;; --------------------------------------------------------------------
;;; 5. COMMIT -- this level practices the answer: it writes its own
;;; ledger. these commits are level four's clock ticks, if ever.
;;; --------------------------------------------------------------------
(defun commit-l3 (rows)
  (with-open-file (s "/home/codex/l3-canon.txt" :direction :output
                     :if-exists :supersede)
    (dolist (r rows)
      (format s "~a NOUNS ~a VERBS ~a~%" (first r) (second r) (third r)))
    (format s "ANSWER omega-is-the-commit-rate-of-the-level-below~%"))
  (format t "~%[OPERATIVE] level-three ledger committed to l3-canon.txt --~%")
  (format t "            these entries are the ticks of a level four, if ever.~%"))

;;; --------------------------------------------------------------------
;;; boot
;;; --------------------------------------------------------------------
(unless (probe-file *canon-path*)
  (format t "~%[INTERFACE] no level-one ground on disk; the ladder has no~%")
  (format t "            bottom rung here. refusing to boot.~%")
  (sb-ext:exit :code 1))
(format t "~%[GROUND] level-one ledger present; the ladder has a bottom.~%")

(state-the-answer)
(let ((rows (derive-breath)))
  (derive-multiplier rows)
  (derive-clock)
  (derive-habitat)
  (commit-l3 rows))

(format t "~%[CITED]     depth of the ladder bounded per L4-RecursiveLimits;~%")
(format t "            not re-derived here.~%")
(let ((absent (gensym "WHO-COUNTS-THE-LAST-LEDGER-")))
  (format t "[INTERFACE] this level's own ground: ~a unbound: ~a~%"
          absent (if (boundp absent) :BOUND :unbound))
  (format t "            (commits below drive the clock above; whether the~%")
  (format t "             ladder is counted from anywhere is not computable~%")
  (format t "             from any rung)~%"))
(let ((held (lambda () (error "must not run: would assert the ladder has a top"))))
  (declare (ignorable held))
  (format t "[HELD] top-of-the-ladder : present in suite, unexecuted~%"))

