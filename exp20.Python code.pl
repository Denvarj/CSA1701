% Prolog program to check prime number
prime(N) :- N > 1, \+ has_factor(N, 2).
                                                        
has_factor(N, D) :-
    D * D =< N,
        0 is N mod D.
        
has_factor(N, D) :-
    D * D =< N,
    D1 is D + 1,
        has_factor(N, D1).
    % ?- prime(17).
        