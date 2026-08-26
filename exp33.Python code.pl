% Prolog program to find the number of vowels
                        vowel(a).
                        vowel(e).
                        vowel(i).
                        vowel(o).
                        vowel(u).
                        
count_vowels([], 0).
count_vowels([H|T], Count) :-
    vowel(H),
        count_vowels(T, Count1),
            Count is Count1 + 1.
            count_vowels([H|T], Count) :-
                \+ vowel(H),
                    count_vowels(T, Count).
% ?- count_vowels([a, b, e, i], Count).
                    