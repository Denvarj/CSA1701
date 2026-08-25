% Prolog program for family relationships
male(john).
male(peter).
female(mary).
female(sara).
parent(john, peter).
parent(mary, peter).
parent(john, sara).
parent(mary, sara).
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
% ?- sibling(peter, sara).
    