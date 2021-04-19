1. A mathematical proof is a verification of proposition by a chain of logical deductions from a set of axioms.

2. proposition is a statement is either true of false.

3. axioms: is a proposition that is asssumed to be true.

4. proof by contradiction:

    To prove proposition P is true, we assume that P is false, then we use that hypothesis to drive falsehood.

    -prove that radical 2 is irrational: 


    P: radical 2 is irrational

    we assume that P is false, so radical 2 is not irrational:

    sqrt(2) = m/n (fraction in lowest terms)

    2 = m^2 / n^2 => m^2 = 2 * n^2 => m is even (2 | m) => 4 | m^2 => 4 | 2 * n ^ 2

    => 2 | n ^ 2 => m and n are no fraction in the lowest terms

5. proof by induction: 
    
    actually induction is just a axiom:

        let  P(n) be a predicate, if P(0) is true and for every n  P(n) => P(n + 1) is true then for every n P(n) is true.


    - proof that for every n 1+2+3+4+ ... + n = n * n(n + 1) / 2

        first step:    If n is 0 then: 0 = 0 * (1) / 2     so P(0) is true

        second step(inductive step): for n >= 0, show P(n) => P(n + 1) is true (the only case this implication can be false is 
        when we assume that P(n) is true)

        Assume P(n) is true, for purpose of verfiying the inductive hypothesis:

        we assume 1 + 2 + 3 + ... + n = n(n + 1) / 2

        need to show 1 + 2 + 3 + ... + (n+1) = (n+1) (n+2) /2

        = n (n+1) / 2 + n+1 = (n+1)(n+2) / 2
    
    - proof this 3 | (n^3 - n)

        P(n):   3 | (n^3 - n)

        base case: 3 | (0 - 0)

        inductive step: for n >= 0 show P(n) => P(n + 1) is true (to show this we assume P(n) is true, because it is the only case
        that whole implication can be false)

        we assume:      3 | (n^3 - n) is true

        we examine      (n+1)^3 - (n+1) = n^3 + 1 + 3n^2 + 3n - n - 1 = n^3 + 3n^2 + 2n = (n^3 - n) + 3n^2 + 3n

        
    - how to tile the 2^n squares with L shape tiles, that leave one stop for the donnet statue:

        for all n There is a way to tile 2^n * 2^n region with a center square missing

        Pf: proof by induction

        P(n): for all n There is a way to tile 2^n * 2^n region with a center square missing

                

        Base case: P(0): is okay there is only one place for statue

        For n>=0, assume P(n) is true


        2^(n+1) * 2^(n+1) you can divide this square to 4 square with 2^n * 2^n and then if you change the hypothesis to tile with
        L shape with a corner square missing, you can put this corner center of the larger square, and use this to prove the actual 
        proposition,

        but the better approath is to change the predicate to:

                for all n there is a way to tile 2^n 2^n region with --any-- square missing 

6. Problem: find sequence of moves that go

    from    A B C   to      A B C
            D E F           D E F
            H G             G H
    
    Thm: There is no sequence of legal moves to invert G and H, and return other letters to their orginal position.

    invariant: In order to show that your system can never reach a particular state, It is sufficient to show there is some property
                called the invariant, that holds at the initial state, and that is preserved by every legal move
            
    To find the invariant for this system, you have analyze the legal moves, to find the invariant property in the system:

        natural order: 

                1 2 3
                4 5 6
                7 8 9
        

        Lemma 1: A row move does not change the natural order of the items
        Proof: In a row move, we move an item from cell i into adjacent cell i-1 or i+1, Nothing else moves, Hence the order of 
                the letters is preserved.
        

        Lemma 2: A column move changes the relative order of preciesly 2 --pair of items--
        Proof: In a column move, we move item from cell i to a blank cell to a cell i+3 or i-3 when an item move positin, It change order
        changes order with 2 item (i-1,i-2 or i+1, i+2)

        Def: A pair of letters L1 and L2 is an inversion, if L1 preceeds L2 in the alphabet, but L1 is after L2 in the puzzle.

        Lemma 3: during a move it is possible to change the number of inversion by plus 2 or minus 2 or none.
        Proof: Row move: no changes
                Column move: there are three cases:

                        the 2 pairs are in order => so the inversion increase by 2
                        the 2 pairs are inverted => so the inversion decreas by 2
                        there are one of each => so the inversion stay the same
        
        so during a move eveness or odness of the inverted pairs stay the same.


        Lemma 4: In every state reachable from initial condition of this problem, the parity of the number of inversions is odd:
        proof by induction: (all invariant proofs are by induction)
        
        P(n): after any sequence of n moves the parity of the number of inversions is odd
        
        Base case P(0): the number of inversion is 1 (the parity is odd) [check]
        Inductive step: P(n) => P(n+1)

            consider any sequence of n+1 moves (m1 ... mn+1)

            By inductive hypothesis we know that after m1 ... mn the parity is odd

            by lemma 3 we know the parity of number of inversions does not change after one move mn+1
            there for the parity after n+1 moves is odd.

7. Strong induction axiom:
    Let P(n) be the predicate, If P(0) is true, and for every n (P(0)^P(1)^...^P(n)) => P(n+1) is true, for every n P(n) is true.

    
    example: All strategies for the n-block game, produce the same score S(n)

    P(n): All strategies for the n-block game, produce the same score S(n)

    Base case: n=1 => S(1) = 0

    inductive step: Assume P(1), P(2), ... P(n) to prove P(n+1)

    look at n+1 blocks          n+1

                            k       n+1-k               1<=k<=n
            
            total score = k(n+1-k) + P(k) + P(n+1-k)        the last two terms came from string induction

            we can't say that s(n+1) does not depends on k, so we get stuck, so we change the induction theorm:

            new P(n): All strategies for n-block game, produce the same score S(n) = n(n-1)/2

            total score = k(n+1-k) + k(k-1)/2 + (n+1-k)(n-k)/2 = n(n+1)/2 = S(n+1)