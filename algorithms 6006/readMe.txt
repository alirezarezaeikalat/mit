0. O(n) represent the upper bound, omega(n) represent the lower bound, teta(n) average complexity 

1. Peak finder algorithms: 

    one dimensional version: 

        an element is a peak if it is greater than left side, and right side

        peak: b>=a and b>=c

    The problem: find a peak if it exists: 

    Solution:

      a. straight forward algorithm:

          start from the left, and go to the right, and in worst case complexity:

              teta(n)    (in worst case the peak is the last element of the array)

      b. Divide and conquer algorithm:
            (divide the array and check if the left side is bigger than the right side, if the 
            left side is bigger divide the left side in two, and vice versa)


        ARGUE (The algorithms works correctly)

        Complexity: teta(log(n))  because we check for the number that we can divide n by 2

     c. 2D version of this algorithm: 


/////////////// Second section ///////////////////

            program   <->   algorithm
            programming language  <->   pseudo code
            computer  <->   model of computation    (what operation you can do, and the cost of them)

            model of computation is some how style of writing an algorithm, for example in programming we 
            have object oriented programming style,... (model of computation is analoge for writing algorithm
            style)

2. two model of computation: 


        a. random access machine (in computational model world):
            random access memory big array (in computer world)

            in constant time, 
                can load constant words,
                do constant computation,
                store constant words
            have constant registers

            you load some words to registers, you can do some computations on those registers, and 
            store them on locations that specified by registers


        b. pointer machine: 

                dynamically allocated objects
                object has constant number of fields (words or pointer(can point to another object, or null))


    In python world:

        list = arrays in python
        L[i] = L[j] + 5 (this takes constant time based on RAM model, but if it was list, it takes linear time)

        Objects in python ares pointer machine model

        Attention: you can define every operation in python with these two models, but sometimes it is less
            obvious.

        L.append(x): if we make a larger array, and copy all the elements with new one it will take
                        linear time, but python uses table doubling and make it constant time

        L = L1 + L2     (concat two arrays) 

        it is eq to: 
            for x in L1
                L.append(x)     O(L1)
                                            => O(L1 + L2 + 1)   one is for making a L
            for x in L2
                L.append(x)     O(L2)

        x in L (this takes linear because in worst case you have to analyze the whole list)

        len(L)  (this is O(1) because in python length stored)

        L.Sort()    (uses comparison sort, and it takes O(|L|log|L|))   |L| is time to compare

        dict: D[key] = value        (it takes O(1)) it uses hash table
                                    hash tables with high probability are constant times)
                                    w.h.p

3. Document Distance Problem (like canonical):

        d(D1, D2)

    Document: a sequence of words
    word: string of alphanumeric chars

    idea of solution: shared words

    D[W] = #number of ocurrence of words in D

    Algorithm: 

        a. split the documents into words

        b. compute frequency of words

        c. compute D1.D2 / |D1||D2|


4. Sorting algorithms: 

        a. Insertion sort: 

                you walk trough all elements, and swaps by its previous elements
                (use pair wise swap to get to the correct position):

                    in the worst case, you it has O(n^2)

        [Attention]
            in insertion sort, the default assumption is that, comparison and swaps has same cost, but sometimes the comparison has more 
            cost than swap

        [Solution] binary insertion sort
            if the cost of comparison is much more than swap, we can do something to reduce the times that we use comparison, we can use 
            binary search before the comaprison...


5. Merge sort: 

        this algorithm has 3 main steps: 

            a. split the n items array in to two array, L and R

            b. sort the the 2 array with n/2 elements

            c. merge two arrays to get the n sorted elements array (merge subroutie is two finger algorithm)

    [Attention]
    all of the work is done in merge routine, because other than that, it is just recursive call
    complexity of merge sort: 

            T(n) = c1 (constant time for divide) + 2 T(n/2) (recursive part) + c.n (merge sort)


        if you expand a tree, you get a tree with logn + 1 step, and each step takes cn work, so 

        T(n) = (1 + logn) * cn = teta(n logn)

    
    [Attention]
    for merge sort you need teta(n) auxillary space but in insertion sort, you need teta(1) auxillary space

    
    analysis in python and c: 

            merge sort in python: 

                    2.2 logn*n micsec
            
            insertion sort: 

                in python: 

                        0.2n^2 micsec
                in c: 
                        0.01n^2 micsec

