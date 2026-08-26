% Prolog program to find grade
grade(Score, 'A') :- Score >= 90.
grade(Score, 'B') :- Score >= 75, Score < 90.
grade(Score, 'C') :- Score >= 60, Score < 75.
grade(Score, 'D') :- Score >= 40, Score < 60.
grade(Score, 'F') :- Score < 40.
% ?- grade(85, Grade).
                                                                                    