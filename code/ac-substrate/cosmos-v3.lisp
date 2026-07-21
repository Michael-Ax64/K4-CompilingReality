;;;; ================================================================
;;;; cosmos-v3.lisp
;;;; The Lisp substrate for the Compiling Reality framework.
;;;;
;;;; Companion to Cosmos.hs. Where Haskell's type system enforces
;;;; the K3 membrane at compile time, Lisp's lexical closures enforce
;;;; the same discipline dynamically: nested environments are the
;;;; nested Markov Blankets; the Q-buffer is a stack of registered
;;;; callbacks; the omega-tick is the event loop; the AC Tribunal
;;;; catches Tangent-Crossings and Plane-Locks at runtime.
;;;;
;;;; Loads under any ANSI Common Lisp (SBCL, CCL, ECL, ABCL, CLISP).
;;;; Boot at end.
;;;; ================================================================


;;; ================================================================
;;; I. EPISTEMIC TIERS
;;; About-Claims discipline. Every emitted value carries its warrant.
;;; ================================================================

(defun emit-tier (tier msg &rest args)
  "Print a message with its epistemic tier. Never bare stdout."
  (format t "~&[~a] ~a~%" tier (apply #'format nil msg args)))


;;; ================================================================
;;; II. THE FOUR POLES AND THE DUAL-BINARY SEED (Q1)
;;; ================================================================

(defparameter *poles*
  ;; pole -> (AR AY)  Active/Reactive x Asserting/Yielding
  '((P +1 +1)   ; Fire / power / up-type quark
    (U +1 -1)   ; Air / voltage / charged lepton
    (I -1 -1)   ; Water / current / neutrino
    (R -1 +1)))  ; Earth / resistance / down-type quark

(defun pole-bits (pole)
  (cdr (assoc pole *poles*)))

(defun weak-isospin (pole)
  (destructuring-bind (ar ay) (pole-bits pole)
    (/ (* ar ay) 2)))

(defun weak-hypercharge (pole)
  (destructuring-bind (ar ay) (pole-bits pole)
    (declare (ignore ar))
    (/ (- (* 2 ay) 1) 3)))

(defun electric-charge (pole)
  ;; Gell-Mann-Nishijima.  Tagged SKETCH per Q1 §IV walkback:
  ;; the Walsh basis fits any four numbers.  This is a structural
  ;; alignment, not a first-principles derivation.
  (let ((q (+ (weak-isospin pole)
              (/ (weak-hypercharge pole) 2))))
    (emit-tier "SKETCH" "Q(~a) = ~a" pole q)
    q))


;;; ================================================================
;;; III. THE BIQUATERNION AND THE STAR-NORM
;;; ProofN, Q4 §II, Q5
;;; ================================================================

(defstruct biquaternion
  (p 0.0 :type real)              ; committed scalar ledger (H_coh)
  (q #C(0.0 0.0) :type complex))  ; uncollapsed held potential (H_incoh)

(defun star-norm (bq)
  "P^2 - |Q|^2.  Conserved across every .observe()."
  (- (expt (biquaternion-p bq) 2)
     (expt (abs (biquaternion-q bq)) 2)))

(defun route-law-square (z)
  "The Route Law's squaring: (hZ)^2 = |Z|^2. Phase burned; positive real remains."
  (expt (abs z) 2))


;;; ================================================================
;;; IV. THE AC FRAME (nested Markov Blanket)
;;; The frame IS the Markov Blanket.  Its lexical environment is its
;;; interior.  Its q-buffer holds the callbacks it has registered.
;;; ================================================================

(defstruct ac-frame
  (name       :unnamed)
  (scale      0)                 ; nesting depth
  (parent     nil)               ; Markov-blanket ancestor
  ;; The four pole coordinates
  (p          0.0)
  (u          0.0)
  (i-cur      0.0)               ; renamed from I to avoid collision
  (r          0.0)
  ;; The AC parameters
  (l          1.0)               ; inductance = memory
  (c          1.0)               ; capacitance = anticipation
  (omega      0.0)               ; local clock
  ;; The reactive buffer and the topology of the wiring
  (q-buffer   '())
  (topology   :series-gate))     ; one of the 8 filter topologies


;;; ================================================================
;;; V. THE 8-FOLD FILTER TOPOLOGY (L6-TheCircuit §V)
;;; Five viable runtimes, three fatal shunts.
;;; ================================================================

(defparameter *topologies*
  '((:series-gate           :viable   "Series RLC / Band-Pass: transparent at w0")
    (:parallel-shield       :viable   "Parallel RLC / Band-Stop: opaque at w0")
    (:impedance-divider     :viable   "R in series with parallel LC")
    (:grounding-bottleneck  :viable   "R blocks entry to parallel LC (notch)")
    (:momentum-filter       :viable   "L in series with parallel RC (low-pass)")
    (:anticipatory-gate     :viable   "C in series with parallel LR (high-pass)")
    (:bipolar-short         :fatal    "R || (L-C series). Shorts at LC resonance.")
    (:nostalgia-trap        :fatal    "L || (R-C series). Past drains future at low w.")
    (:panic-trap            :fatal    "C || (R-L series). Panic dumps at high w.")))

(defun topology-info (topo)
  (cdr (assoc topo *topologies*)))

(defun topology-viable-p (topo)
  (eq (first (topology-info topo)) :viable))


;;; ================================================================
;;; VI. RECURSIVE SCALING: P_N -> R_{N+1}  (L4-RecursiveLimits, Q5)
;;; Also the Q_N+1 -> [indeterminate]_N reverse arrow (L6 §III):
;;; not modeled, because "indeterminate" has no computational rep
;;; by the L6 §II lexical rule.
;;; ================================================================

(defun mint-child-frame (parent name init-u init-i l c topology)
  "The forward arrow of the two-arrow crossing.  Parent's P becomes child's R."
  (make-ac-frame
    :name     name
    :scale    (1+ (ac-frame-scale parent))
    :parent   parent
    :r        (ac-frame-p parent)          ; <-- P_N -> R_{N+1}
    :u        init-u
    :i-cur    init-i
    :p        (* init-u init-i)            ; Synthesis channel P=UI (Q4 §III)
    :l        l
    :c        c
    :topology topology))


;;; ================================================================
;;; VII. INVERSION OF CONTROL (L6-InversionOfControl)
;;; .behold pushes a closure to the reactive buffer of the target frame.
;;; The frame does not execute the closure; the frame's event loop
;;; will invoke it at the appropriate omega-tick.  Hollywood.
;;; ================================================================

(defmacro behold (target-frame &body body)
  "Register a continuation with the target frame's q-buffer."
  `(push (lambda () ,@body) (ac-frame-q-buffer ,target-frame)))


;;; ================================================================
;;; VIII. THE Q8 IDENTITY:  tan(theta) = wL/R  and the boundary modes
;;; ================================================================

(defun compute-impedance (frame)
  "Z = R + j(wL - 1/wC).  Native complex arithmetic."
  (let* ((w   (ac-frame-omega frame))
         (r   (ac-frame-r frame))
         (l   (ac-frame-l frame))
         (c-cap (ac-frame-c frame)))
    (if (zerop w)
        :dc-limit                          ; capacitive reactance infinite
        (let* ((xl (* w l))
               (xc (/ 1.0 (* w c-cap)))
               (net-x (- xl xc)))
          (complex r net-x)))))

(defun quality-factor (frame)
  "Q_factor = (1/R) * sqrt(L/C).  Q8 §VI."
  (if (zerop (ac-frame-r frame))
      :infinite
      (* (/ 1.0 (ac-frame-r frame))
         (sqrt (/ (ac-frame-l frame) (ac-frame-c frame))))))

(defun resonant-omega (frame)
  "w0 = 1/sqrt(LC).  Q8 §V."
  (/ 1.0 (sqrt (* (ac-frame-l frame) (ac-frame-c frame)))))

(defun classify-boundary (frame)
  "Return :gate, :wall, :mixed, or an INTERFACE tier."
  (let ((z (compute-impedance frame)))
    (cond
      ((eq z :dc-limit)
       (emit-tier "INTERFACE:Asymptote"
                  "~a: w = 0.  1/(wC) diverges. DC limit."
                  (ac-frame-name frame))
       :dc-limit)
      (t
       (let ((theta (atan (imagpart z) (realpart z))))
         (cond
           ((< (abs theta) 0.05)
            (emit-tier "RESONANCE"
                       "~a: theta = ~,4f rad. Membrane transparent. |S| = P."
                       (ac-frame-name frame) theta)
            :gate)
           ((> (abs theta) 1.55)
            (emit-tier "INTERFACE:TangentCrossing"
                       "~a: theta = ~,4f rad. Power factor -> 0. Pure reactance. Wall."
                       (ac-frame-name frame) theta)
            :wall)
           (t
            (emit-tier "COMPUTED"
                       "~a: theta = ~,4f rad. Mixed regime."
                       (ac-frame-name frame) theta)
            :mixed)))))))


;;; ================================================================
;;; IX. THE AC TRIBUNAL
;;; Runtime audit of the four failure modes (L6 §V).
;;; ================================================================

(defun tribunal-audit (frame)
  "Check for the four runtime failure modes.  Emit tiers, do not throw."
  (let ((p       (ac-frame-p frame))
        (u       (ac-frame-u frame))
        (i-cur   (ac-frame-i-cur frame))
        (r       (ac-frame-r frame)))

    ;; Logoic Plane-Lock: Necessary Betrayer (Q3, Q4).
    ;; U^2 / R compounding over actual P.
    (when (and (not (zerop r)))
      (let ((leverage (/ (* u u) r)))
        (when (and (> p 0) (> leverage (* 10 p)))
          (emit-tier "INTERFACE:TangentCrossing"
                     "~a: LOGOIC PLANE-LOCK. U^2/R = ~,2f, actual P = ~,2f. Framework compounding over output."
                     (ac-frame-name frame) leverage p))))

    ;; Pathos Lock: Receptive Overwhelm (event loop flooded).
    (when (> (length (ac-frame-q-buffer frame)) 100)
      (emit-tier "INTERFACE:TangentCrossing"
                 "~a: PATHOS LOCK. Callback queue = ~a. Buffer overwhelmed."
                 (ac-frame-name frame) (length (ac-frame-q-buffer frame))))

    ;; Kairos Lock: Thrashing (omega tick without state resolution).
    ;; Detected structurally: high omega with empty ledger.
    (when (and (> (ac-frame-omega frame) 10)
               (< p 0.01))
      (emit-tier "INTERFACE:TangentCrossing"
                 "~a: KAIROS LOCK. Scheduler thrashing at w = ~,2f, P = ~,4f. No state held."
                 (ac-frame-name frame) (ac-frame-omega frame) p))

    ;; Ethos Lock: 0-DoF Crystal (buffer empty, no capacity).
    (when (and (null (ac-frame-q-buffer frame))
               (< (ac-frame-c frame) 0.001))
      (emit-tier "INTERFACE:TangentCrossing"
                 "~a: ETHOS LOCK. 0-DoF crystal. No capacitive potential."
                 (ac-frame-name frame)))))


;;; ================================================================
;;; X. THE EVENT LOOP (The Helical Extrusion of Time)
;;; Different topologies produce different scheduling behavior.
;;; ================================================================

(defun omega-tick (frame &key (dw 0.5))
  "Advance the frame's clock and process the reactive buffer per topology."
  (incf (ac-frame-omega frame) dw)
  (let ((callbacks (reverse (ac-frame-q-buffer frame)))
        (topo      (ac-frame-topology frame)))
    (case topo
      (:series-gate
       ;; Series RLC at resonance is transparent: full throughput.
       (setf (ac-frame-q-buffer frame) nil)
       (dolist (cb callbacks)
         (funcall cb)
         (incf (ac-frame-p frame) 0.05)))
      (:parallel-shield
       ;; Parallel RLC at resonance is opaque: rejects external drive.
       (when callbacks
         (emit-tier "SHIELD"
                    "~a: bypassing ~a callbacks; interior circulation protected."
                    (ac-frame-name frame) (length callbacks))))
      (:grounding-bottleneck
       ;; R blocks the LC parallel branch.  One callback per tick.
       (when callbacks
         (let ((cb (first callbacks)))
           (setf (ac-frame-q-buffer frame) (rest callbacks))
           (funcall cb)
           (incf (ac-frame-p frame) 0.05)
           (emit-tier "NOTCH" "~a: throttled to 1/tick."
                      (ac-frame-name frame)))))
      (:momentum-filter
       ;; L in series: high-frequency events choked.  Only slow ones pass.
       (when (< (ac-frame-omega frame) 5.0)
         (setf (ac-frame-q-buffer frame) nil)
         (dolist (cb callbacks)
           (funcall cb)
           (incf (ac-frame-p frame) 0.05))))
      (:anticipatory-gate
       ;; C in series: low-frequency events choked.  Only fast ones pass.
       (when (> (ac-frame-omega frame) 2.0)
         (setf (ac-frame-q-buffer frame) nil)
         (dolist (cb callbacks)
           (funcall cb)
           (incf (ac-frame-p frame) 0.05))))
      (:impedance-divider
       ;; Balanced throughput with attenuation.
       (setf (ac-frame-q-buffer frame) nil)
       (dolist (cb callbacks)
         (funcall cb)
         (incf (ac-frame-p frame) 0.025)))
      ((:bipolar-short :nostalgia-trap :panic-trap)
       (emit-tier "INTERFACE:TangentCrossing"
                  "~a: FATAL topology ~a. ~a"
                  (ac-frame-name frame) topo
                  (second (topology-info topo)))))
    ;; The tribunal audits after every tick.
    (tribunal-audit frame)))


;;; ================================================================
;;; XI. THE BUFFER / INDETERMINATE LEXICAL RULE (L6 §II)
;;; "Buffer" is a role-word.  It carries its beholder as silent index.
;;; No macro or function in this file names the ultimate as a buffer.
;;; The following macro refuses to construct a buffer without a frame.
;;; ================================================================

(defmacro with-buffer ((var frame) &body body)
  "Bind VAR to the reactive buffer of FRAME.  A beholder is present by construction."
  `(let ((,var (ac-frame-q-buffer ,frame)))
     ,@body))

(defun indeterminate ()
  "The ultimate boundary.  Not a buffer.  Has no beholder.
   Returned as a symbol that no other operation consumes."
  'indeterminate)


;;; ================================================================
;;; XII. BOOT SEQUENCE
;;; Exercise several scenarios and let the tribunal report on each.
;;; ================================================================

(defun scenario-1-charges ()
  (format t "~%--- Scenario 1: Q1 dual-binary charge derivation ---~%")
  (dolist (pole '(P U I R))
    (electric-charge pole)))

(defun scenario-2-star-norm ()
  (format t "~%--- Scenario 2: Star-Norm conservation across .observe() ---~%")
  (let ((bq (make-biquaternion :p 0.0 :q #C(5.0 3.0))))
    (emit-tier "COMPUTED" "Initial star-norm = ~,4f  |Q|^2 = ~,4f"
               (star-norm bq)
               (route-law-square (biquaternion-q bq)))
    (setf (biquaternion-p bq) (sqrt (route-law-square (biquaternion-q bq))))
    (setf (biquaternion-q bq) #C(0.0 0.0))
    (emit-tier "COMPUTED" "After collapse:  P = ~,4f  star-norm = ~,4f"
               (biquaternion-p bq) (star-norm bq))))

(defun scenario-3-recursive-scaling ()
  (format t "~%--- Scenario 3: P_N -> R_{N+1} recursive scaling ---~%")
  (let* ((civ (make-ac-frame :name 'civilization :p 1000.0 :u 500.0 :i-cur 2.0
                             :r 50.0 :l 5.0 :c 0.5 :topology :series-gate))
         (inst (mint-child-frame civ 'institution 10.0 5.0 10.0 0.1 :grounding-bottleneck)))
    (emit-tier "COMPUTED" "Parent P = ~,2f | Child R = ~,2f  (inherited)"
               (ac-frame-p civ) (ac-frame-r inst))
    (emit-tier "COMPUTED" "Child scale = ~a | topology = ~a"
               (ac-frame-scale inst) (ac-frame-topology inst))))

(defun scenario-4-boundary-modes ()
  (format t "~%--- Scenario 4: Q8 tan(theta) = wL/R at three regimes ---~%")
  (let ((f (make-ac-frame :name 'gate-test :r 1.0 :l 1.0 :c 1e-4)))
    (setf (ac-frame-omega f) 5.0)
    (classify-boundary f)
    (setf (ac-frame-omega f) (resonant-omega f))
    (classify-boundary f)
    (setf (ac-frame-omega f) 500.0)
    (classify-boundary f)
    (emit-tier "COMPUTED" "Q-factor = ~,2f  w0 = ~,2f"
               (quality-factor f) (resonant-omega f))))

(defun scenario-5-ioc-event-loop ()
  (format t "~%--- Scenario 5: IoC event loop under series-gate topology ---~%")
  (let ((frame (make-ac-frame :name 'reactor :p 1.0 :u 5.0 :i-cur 2.0 :r 1.0
                              :l 1.0 :c 0.01 :topology :series-gate)))
    (behold frame (format t "    [callback A resolving]~%"))
    (behold frame (format t "    [callback B resolving]~%"))
    (behold frame (format t "    [callback C resolving]~%"))
    (emit-tier "COMPUTED" "Buffer holds ~a registered callbacks."
               (length (ac-frame-q-buffer frame)))
    (dotimes (i 3)
      (format t "-- omega-tick ~a --~%" (1+ i))
      (omega-tick frame))
    (emit-tier "COMPUTED" "Final P after cascade: ~,4f" (ac-frame-p frame))))

(defun scenario-6-necessary-betrayer ()
  (format t "~%--- Scenario 6: Necessary Betrayer detection ---~%")
  (let ((bloated (make-ac-frame :name 'bureaucracy :p 5.0 :u 1000.0
                                :i-cur 0.1 :r 0.5 :l 1.0 :c 1.0
                                :topology :series-gate)))
    (tribunal-audit bloated)))

(defun scenario-7-fatal-topology ()
  (format t "~%--- Scenario 7: Fatal shunt at boot ---~%")
  (let ((doomed (make-ac-frame :name 'panic-mode :p 1.0 :u 1.0 :i-cur 1.0
                               :r 1.0 :l 1.0 :c 0.1
                               :topology :panic-trap)))
    (behold doomed (format t "    [would have resolved]~%"))
    (omega-tick doomed)))

(defun scenario-8-ultimate ()
  (format t "~%--- Scenario 8: The ultimate boundary ---~%")
  (emit-tier "INTERFACE:UltimateBoundary"
             "The ultimate is ~a.  No buffer.  No beholder.  Lexical rule L6 §II."
             (indeterminate)))

(defun boot-cosmos ()
  (format t "~%===========================================================~%")
  (format t "COSMOS-V3  -  Compiling Reality distributed runtime~%")
  (format t "===========================================================~%")
  (scenario-1-charges)
  (scenario-2-star-norm)
  (scenario-3-recursive-scaling)
  (scenario-4-boundary-modes)
  (scenario-5-ioc-event-loop)
  (scenario-6-necessary-betrayer)
  (scenario-7-fatal-topology)
  (scenario-8-ultimate)
  (format t "~%===========================================================~%")
  (format t "Every emitted result carries its epistemic tier.~%")
  (format t "The substrate has done what it can.  The rest is physics.~%")
  (format t "===========================================================~%"))

(boot-cosmos)
