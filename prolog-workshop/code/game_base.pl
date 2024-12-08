% FS 2024

% data

default(empty).

char(o, 'O').
char(x, 'X').
char(empty, 'E').

player(1, player1).
player(2, player2).

board(2, [[empty, empty], [empty, empty]]).
board(3, [[empty, empty, empty], [empty, empty, empty], [empty, empty, empty]]).

% Create dynamic board

create_list(_, 0, []).
create_list(Element, Size, [Element|Sublist]):-
    Size > 0,
    Size1 is Size - 1,
    create_list(Element, Size1, Sublist).

create_board(Element, Size, Board):-
    create_list(Element, Size, List),
    create_list(List, Size, Board).

% Display board content

display_item(Item):- 
    char(Item, C), 
    write(C).

display_row([]).
display_row([Item|RemainingItems]):-
    display_item(Item),
    display_row(RemainingItems).

display_board([]).
display_board([Row|RemainingRows]):-
    display_row(Row), nl,
    display_board(RemainingRows).

% Utils

between(Min, Max, Min):- Min =< Max.
between(Min, Max, Value):-
    Min < Max,
    NextMin is Min + 1,
    between(NextMin, Max, Value).

nthX([Head|_], 0, Head):- !.
nthX([_|Tail], Index, Value):-
    Index > 0,
    NextIndex is Index - 1,
    nthX(Tail, NextIndex, Value).

replace(0, Value, [_|Tail], [Value|Tail]).
replace(Index, Value, [Head|Tail], [Head|NewTail]):-
    Index > 0,
    NewIndex is Index - 1,
    replace(NewIndex, Value, Tail, NewTail).

% Inputs

read_number(X):-
    read_number_aux(X, 0).
read_number_aux(X, Acc) :- 
    get_code(C),
    between(48, 57, C), !,
    Acc1 is 10 * Acc + (C - 48),
    read_number_aux(X, Acc1).
read_number_aux(X, X).

get_number(Min, Max, Context, Value):-
    format('~a between ~d and ~d: ', [Context, Min, Max]),
    repeat,
    read_number(Value),
    between(Min, Max, Value), !.

% Init game state

get_board(N, Board):-
    default(Element),
    create_board(Element, N, Board).

choose_board(Board):-
    get_number(1, 4, 'Board size', N),
    get_board(N, Board).

choose_player(Player):-
    get_number(1, 2, 'Choose the first player', N),
    player(N, Player).

get_game_state([CurrentBoard, CurrentPlayer]):-
    choose_board(CurrentBoard),
    choose_player(CurrentPlayer).

% Game loop

% game_loop(GameState):- TODO

% Main function

play:- 
    get_game_state(GameState),
    write(GameState).