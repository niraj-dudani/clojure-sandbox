; Clojure for the Brave and True -- Chapter 3
; https://www.braveclojure.com/do-things/
;
; "One detail to note is that, in these examples, reduce takes a collection of 
; elements, [1 2 3 4], and returns a single number. Although programmers often 
; use reduce this way, you can also use reduce to return an even larger 
; collection than the one you started with, as we’re trying to do with 
; symmetrize-body-parts. reduce abstracts the task “process a collection and 
; build a result,” which is agnostic about the type of result returned."

(def z '(0 1 2 0 9 2 2 1 2 8))

(defn collect-and-duplicate-twos
    [z a]
    (if
        (= a 2)
        (into z [a a])
        (conj z a)))

(def zz (reduce collect-and-duplicate-twos [] z))

(println z)
(println zz)
