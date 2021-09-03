1. Optimizational models

What is an optimization model:
  
  a. An objective function that is to be maximized or minimized

  b. Set of constrains that must be honored

2. knapsack optimization problem:

  Problem statement: There is a limited space to carry objects, but you want to get the most valuable objects, 
    How do you choose which object to carry?
  
  There are two variant of this problem:

    a. 0/1 knapsack prblem: you either take the object or not

    b. Continous or fractional knapsack problem

  
3. 0/1 knapsack problem formalized:

    - Each item represented by a pair <value: weight>

    - The knapsack can acccommodate items with weight of no more than w

    - A vector L, of length n, represent the set of available items. Each element of the vector is an item

    - A vector V, of length n, is used to indicate wheather or not items are taken.

    problem: 
      - Maximize: 

          sigma<0, n-1>(V[i]*L[i].value)
      
      - Constrain:

          sigma<0, n-1>(V[i]*L[i].weight) <= w
      
    Solution:

      a. Brute force algorithm:

          - Enumerate all possible combination of items. That is to say to generate all subsets of the set of items. This is 
            called power set.

          - Remove all of the combinations whose total units exceeds the allowed weight

          - From the remaining combinations choose any one whoose value is the largest.
      
      [ATTENTION]
      Actually there is no perfect answer for knapsack problem, because it is exponential intrinsicly. This means there is no
      --exact-- solution to this problem that is not exponential.

      b. --Greedy algorithm--:

          while the knapsack not full:
            put --best-- available item in the knapsack
          
      The question here is what --best-- means, maybe it is the highest value, lowest weight, or highest value/weight ratio

        The code in Lecture1 is using greedy algorithm.

        If you look at the code, we use sorted function in python.

        [ATTENTION]
        python uses --timsort--, which is a variant of something called --quick sort--, which has the same worst case complexity of 
        --merge sort--