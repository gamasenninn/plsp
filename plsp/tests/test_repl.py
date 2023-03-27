import sys
import os
import pytest
#from plsp.repl import *


if True:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    import repl

def test_lisp_program_square():
    env = repl.initial_env()
    # lambda を使う場合
    program = "(define square (lambda (x) (* x x)))"
    parsed = repl.parse(program)
    _ = repl.evaluate(parsed, env)  # 定義を環境に登録

    # square関数の評価
    program = "(square 4)"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == 16

    # defunc を使う場合
    program = "(defunc square2 (x) (* x x))"
    parsed = repl.parse(program)
    _ = repl.evaluate(parsed, env)  # 定義を環境に登録

    # square関数の評価
    program = "(square2 4)"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == 16

def test_lisp_program_sum():
    env = repl.initial_env()

    # lambda を使う場合
    program =  "(define sum (lambda (a b) (+ a b)))"
    parsed = repl.parse(program)
    _ = repl.evaluate(parsed, env)  

    # sum関数の評価
    program = "(sum 3 5)"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == 8

    # defunc を使う場合
    program =  "(defunc sum2 (a b) (+ a b))"
    parsed = repl.parse(program)
    _ = repl.evaluate(parsed, env)  

    # sum関数の評価
    program = "(sum2 3 5)"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == 8

def test_lisp_numeric_calc():
    env = repl.initial_env()

    # + 
    program = "(+ 3 5)"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == 8

    # -
    program = "(- 5 2)"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == 3

    # *
    program = "(* 5 2)"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == 10

    # *
    program = "(/ 10 2)"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == 5

def test_lisp_compare_formula():
    env = repl.initial_env()
    # <
    program = "(< 2 10 )"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == True

    program = "(< 10 2 )"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == False

    program = "(< 10 10 )"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == False

    program = "(<= 10 10 )"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == True

    # >
    program = "(> 10 2 )"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == True

    program = "(> 2 10 )"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == False

    program = "(< 10 10 )"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == False

    program = "(<= 10 10 )"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == True

def test_lisp_define_var():
    env = repl.initial_env()

    program =  "(define x 10)"
    parsed = repl.parse(program)
    _ = repl.evaluate(parsed, env)  

    program =  "(define y 20)"
    parsed = repl.parse(program)
    _ = repl.evaluate(parsed, env)  

    program = "(+ x y )"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == 30

def test_lisp_if_op():
    env = repl.initial_env()

    program = "(if (< 3 4) 1 0)"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == 1

    program = "(if (> 10 20) 1 0)"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == 0

def test_lisp_list_op():
    env = repl.initial_env()

    program = "(car (list 1 2 3))"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == 1

    program = "(cdr (list 1 2 3))"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == [2,3]

    program = "(cons 1 (list 2 3))"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == [1,2,3]

    program = "(append (list 1 2 3) (list 4 5 6))"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == [1,2,3,4,5,6]

    program = "(length (list 1 2 3))"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == 3
    
    program = "(map (lambda (x) (* x 2)) (list 1 2 3))"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == [2,4,6]

def test_lisp_recursive_func():
    env = repl.initial_env()

    program =  "(defunc factorial (n) (if (<= n 1) 1 (* n (factorial (- n 1)))))"
    parsed = repl.parse(program)
    _ = repl.evaluate(parsed, env)  

    program = "(factorial 10)"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == 3628800 


    program =  "(defunc fibonacci (n) (if (< n 2) n (+ (fibonacci (- n 1)) (fibonacci (- n 2)))))"
    parsed = repl.parse(program)
    _ = repl.evaluate(parsed, env)  

    program = "(fibonacci 10)"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == 55

def test_lisp_check_op():
    env = repl.initial_env()

    # procedur?
    program =  "(defunc factorial (n) (if (<= n 1) 1 (* n (factorial (- n 1)))))"
    parsed = repl.parse(program)
    _ = repl.evaluate(parsed, env)  

    program = "(procedure? factorial)"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == True

    program = "(procedure? +)"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == True

    program = "(procedure? 42)"
    parsed = repl.parse(program)
    result = repl.evaluate(parsed, env)
    assert result == False

