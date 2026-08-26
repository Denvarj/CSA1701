% Prolog program to print numbers from 1 to 10
                    print_numbers :-
                        between(1, 10, N),
                            write(N), nl,
                                fail.
                                print_numbers.
% ?- print_numbers.
                                