% Prolog program to find maximum element in a list
max_list([X], X).
max_list([H|T], M) :-
max_list(T, M1),
(H > M1 -> M = H ; M = M1).
% ?- max_list([3, 9, 2, 7], Max).
                                                            