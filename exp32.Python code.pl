% Prolog program to implement pattern matching
match_pattern([a, b, c], [a, b, c]).
match_pattern([a, _, c], [a, b, c]).
match_pattern([H|T], [H|T]).
% ?- match_pattern(X, [a, b, c]).
                    