% father/2
% father(a, b), the father of a is b
father(manel, joaquim).
father(aberto, joao).
father(pedro, manel).

% is_grandchild(?X, ?Y)
% This rule checks if X is a grandchild of Y
is_grandchild(X, Y):-
    father(Y, _Z),
    father(_Z, X).
