% Prolog program to reverse a list
reverse_list([], []).
reverse_list([H|T], R) :-
reverse_list(T, R1),
append(R1, [H], R).
% ?- reverse_list([1, 2, 3], Reversed).
                                                