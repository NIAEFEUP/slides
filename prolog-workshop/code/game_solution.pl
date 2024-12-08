% FS 2024

% data

default(empty).

char(o, 'O').
char(x, 'X').
char(empty, 'E').

switch_player(player1, player2).
switch_player(player2, player1).

player(1, player1).
player(2, player2).

piece(player1, o).
piece(player2, x).

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

display_player(Player):-
    write('Current player: '), 
    write(Player), nl.

get_piece(Board, X, Y, Piece):-
    nthX(Board, Y, Line),
    nthX(Line, X, Piece).

valid_move(Board, X-Y):- 
    get_piece(Board, X, Y, empty).

choose_move(Board, X-Y):-
    length(Board, N),
    Max is N - 1,
    repeat,
    get_number(0, Max, 'Coordinate X', X),
    get_number(0, Max, 'Coordinate Y', Y),
    valid_move(Board, X-Y), 
    !.

generate_moves(Board, Moves):-
    length(Board, N),
    Max is N - 1,
    findall(X-Y, (
        between(0, Max, X), 
        between(0, Max, Y), 
        valid_move(Board, X-Y)
    ), Moves).

put_piece(Board, X-Y, Piece, NewBoard):-
    nthX(Board, Y, Line),
    replace(X, Piece, Line, NewLine),
    replace(Y, NewLine, Board, NewBoard).

game_over(Board):-
    generate_moves(Board, Moves),
    length(Moves, 0).

show_winner(CurrentPlayer):-
    switch_player(CurrentPlayer, Winner),
    write('The winner is: '), 
    write(Winner).

game_loop([CurrentBoard, CurrentPlayer]):-

    % Verify if the game is over
    game_over(CurrentBoard),

    % If so, show the winner
    show_winner(CurrentPlayer), !.

game_loop([CurrentBoard, CurrentPlayer]):-

    % Display the current game state
    display_board(CurrentBoard),
    display_player(CurrentPlayer),

    % The current player must select a coordinate
    choose_move(CurrentBoard, X-Y),

    % Apply the move
    piece(CurrentPlayer, Piece),
    put_piece(CurrentBoard, X-Y, Piece, NewBoard),

    % Switch to the next player's turn
    switch_player(CurrentPlayer, NewPlayer),

    % Recursive call to continue the game
    game_loop([NewBoard, NewPlayer]).

% Main function

play:-
    get_game_state(GameState),
    game_loop(GameState).