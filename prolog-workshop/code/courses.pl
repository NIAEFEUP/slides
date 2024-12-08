% test/2
% test(Course, Month)
% Describes the month in which a test is scheduled for the given course
test(ipc, 'December').
test(pfl, 'January').
test(fsi, 'January').

% project/1
% project(Course)
% Indicates that the specified course involves a project
project(ipc).
project(rcom).
project(lbaw).
project(pfl).

% exam/2
% exam(Course, Month)
% Describes the month in which an exam is scheduled for the given course
exam(rcom, 'January').
exam(lbaw, 'January').

% study(?Course)
% Determines whether a course involves either a test or an exam.
study(C) :- test(C, _).
study(C) :- exam(C, _).

% on_fire_1(?Course)
% Determines whether a course is both a project course and involves studying (i.e., has a test or an exam).
on_fire_1(C) :- 
    project(C),
    study(C).

% on_fire_2(?Course)
% Determines whether a course is both a project course and involves studying (i.e., has a test or an exam).
on_fire_2(C) :- 
    study(C),
    project(C).

% Cut, version 1
on_fire_cut_1(C):- 
    project(C), !,
    study(C).

% Cut, version 2
on_fire_cut_2(C):- 
    project(C),
    study(C), !.