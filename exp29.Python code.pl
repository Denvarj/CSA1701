% Prolog program to generate EB bill
                                                                                        bill(Units, Amount) :-
                                                                                            Units =< 100,
                                                                                                Amount is Units * 2.
                                                                                                
bill(Units, Amount) :-
    Units > 100,
        Units =< 250,
            Base is 200,
                Extra is Units - 100,
                    Amount is Base + (Extra * 3).
                    
bill(Units, Amount) :-
    Units > 250,
        Base is 200 + 450,
            Extra is Units - 250,
                Amount is Base + (Extra * 5).
% ?- bill(150, Amount).
                