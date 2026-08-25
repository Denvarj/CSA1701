% Prolog program to find GCD
gcd(X, 0, X) :- !.
gcd(X, Y, G) :-
Y > 0,
R is X mod Y,
gcd(Y, R, G).
% ?- gcd(48, 18, G).
                        