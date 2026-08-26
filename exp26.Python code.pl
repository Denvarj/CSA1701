% Prolog program to find the sum of list elements
                                                                    sum_list([], 0).
                                                                    sum_list([H|T], S) :-
                                                                        sum_list(T, S1),
                                                                            S is S1 + H.
% ?- sum_list([1, 2, 3, 4, 5], Sum).
                                                                            