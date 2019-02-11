# -*- coding: utf-8 -*-

'''
Clojure for the Brave and True -- Chapter 3
https://www.braveclojure.com/do-things/

"One detail to note is that, in these examples, reduce takes a collection of 
elements, [1 2 3 4], and returns a single number. Although programmers often 
use reduce this way, you can also use reduce to return an even larger 
collection than the one you started with, as we’re trying to do with 
symmetrize-body-parts. reduce abstracts the task “process a collection and 
build a result,” which is agnostic about the type of result returned."
'''

from functools import reduce

z = [0, 1, 2, 0, 9, 2, 2, 1, 2, 8]

# Note that 'collection' is passed by reference, so the original will get
# modified too. However, this doesn't cause any problems in this example
# because 'reduce' discards the originals.
def collect_and_duplicate_twos(collection, item):
    if item == 2:
        collection.extend([item, item])
    else:
        collection.append(item)
    
    return collection

zz = reduce(collect_and_duplicate_twos, z, [])

print(z)
print(zz)
