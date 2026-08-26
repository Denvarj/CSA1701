% Prolog program for the 8-Queens problem
                                    solution(Board) :-
                                        length(Board, 8),
                                            maplist(between(1, 8), Board),
                                                safe(Board).
                                                
safe([]).
safe([Q|Rest]) :-
    safe(Rest),
        no_conflict(Q, 1, Rest).
        
no_conflict(_, _, []).
no_conflict(Q, N, [Q1|Rest]) :-
    Q =\= Q1,
        abs(Q - Q1) =\= N,
            N1 is N + 1,
                no_conflict(Q, N1, Rest).
% ?- solution(Board).
                