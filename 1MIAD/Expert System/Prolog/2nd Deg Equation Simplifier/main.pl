%%%%%%%%%%%%%%% A %%%%%%%%%%%%%%%%%%%%%%%%%
% Regle 1 
rA(A,'','','',''):-
    A==0.

% Regle 2
rA(A,'','',x,'²'):-
    A==1.

% Regle 3
rA(A,'',A,x,'²'):-
    A>1.

% Regle 4
rA(A,-,'',x,'²'):-
    A== -1.

% Regle 5
rA(A,-,AA,x,'²'):-
    A < -1,
    abs(A,AA).

%%%%%%%%%%%%%%% B %%%%%%%%%%%%%%%%%%%%%%%%%
% Regle 6
rB(B,_,'','',''):-
    B==0.

% Regle 7
rB(B,A,'','',x):-
    B==1,
    A==0.

% Regle 8
rB(B,A,+,'',x):-
    B== 1,
    A=\=0.

% Regle 9
rB(B,A,'',B,x):-
    B>1,
    A==0.

% Regle 10
rB(B,A,+,B,x):-
    B>1,
    A=\=0.

% Regle 11
rB(B,_,-,'',x):-
    B== -1.

% Regle 12
rB(B,_,-,BB,x):-
    B< -1,
    abs(B,BB).

%%%%%%%%%%%%%%% C %%%%%%%%%%%%%%%%%%%%%%%%%
% Regle 13
rC(C,A,B,'',0):-
    C==0,
    abs(A,AA),
    abs(B,BB),
    Abso is AA+BB,
    Abso ==0.

% Regle 14
rC(C,A,B,'',''):-
    C==0,
    abs(A,AA),
    abs(B,BB),
    Abso is AA+BB,
    Abso=\=0.

% Regle 15
rC(C,A,B,'',C):-
    C > 0,
    abs(A,AA),
    abs(B,BB),
    Abso is AA+BB,
    Abso == 0.

% Regle 16
rC(C,A,B,+,C):-
    C > 0,
    abs(A,AA),
    abs(B,BB),
    Abso is AA+BB,
    Abso =\=0.

% Regle 17
rC(C,_,_,-,CC):-
    C < 0,
    abs(C,CC).

run :-
    write('Entre A:'),
    read(A),
    write('Entre B:'),
    read(B),
    write('Entre C:'),
    read(C),
    rA(A, Sg2, Coef2, Var2, Expo2),
    rB(B, A, Sg1, Coef1, Var1),
    rC(C, A, B, Sg0, Coef0),
    format(atom(PolyString), '~w~w~w~w~w~w~w~w~w', [Sg2, Coef2, Var2, Expo2, Sg1, Coef1, Var1, Sg0, Coef0]),
    write(PolyString).

%%%%%%%%%%%%%%% BONUS %%%%%%%%%%%%%%%%%%%%%%%%%
polynome(A, B, C, PolyString) :-
    rA(A, Sg2, Coef2, Var2, Expo2),
    rB(B, A, Sg1, Coef1, Var1),
    rC(C, A, B, Sg0, Coef0),
    format(atom(PolyString), '~w~w~w~w~w~w~w~w~w', [Sg2, Coef2, Var2, Expo2, Sg1, Coef1, Var1, Sg0, Coef0]).

%%%%%%%%%%%%%%% TEST %%%%%%%%%%%%%%%%%%%%%%%%%
% Define the test cases
test_cases([    [-3, -4, 5, '-3x²-4x+5'],
    [0, 0, 0, '0'],
    [0, 2, 0, '2x'],
    [0, 0, -7, '-7'],
    [1, 0, 0, 'x²'],
    [-1, 0, 0, '-x²'],
    [1, 2, 3, 'x²+2x+3'],
    [-1, -2, -3, '-x²-2x-3'],
    [1, -2, 1, 'x²-2x+1'],
    [2, 3, 4, '2x²+3x+4'],
    [-2, -3, -4, '-2x²-3x-4'],
    [-2, 3, -4, '-2x²+3x-4'],
    [2, -3, 4, '2x²-3x+4'],
    [0, 1, 0, 'x'],
    [0, -1, 0, '-x'],
    [0, 0, 1, '1'],
    [0, 0, -1, '-1'],
    [1, 1, 0, 'x²+x'],
    [-1, -1, 0, '-x²-x'],
    [1, 0, 1, 'x²+1'],
    [-1, 0, -1, '-x²-1'],
    [0, 1, 1, 'x+1'],
    [0, -1, -1, '-x-1']
]).

% Define a predicate to run the test cases
run_test_cases :-
    test_cases(TestCases),
    run_test_cases(TestCases, 1, 0, 0).

run_test_cases([], Total, Passed, Failed) :-
    format('Finished running test cases.~n'),
    format('Total test cases: ~w. Passed: ~w. Failed: ~w.~n', [Total, Passed, Failed]).
run_test_cases([[A, B, C, ExpectedString] | Rest], Total, Passed, Failed) :-
    polynome(A, B, C, ResultString),
    (ResultString = ExpectedString ->
        format('Test case ~w: Passed.~n', [Total]),
        NewPassed is Passed + 1
    ;
        format('Test case ~w: Failed. Expected: ~w. Got: ~w.~n', [Total, ExpectedString, ResultString]),
        NewFailed is Failed + 1
    ),
    NewTotal is Total + 1,
    run_test_cases(Rest, NewTotal, NewPassed, NewFailed).
