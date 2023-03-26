from lparser import parse
from evaluator import evaluate, initial_env
from utils import schemestr

def count_parentheses(s):
    return s.count('(') - s.count(')')

def repl(prompt='plsp> '):
    global_env = initial_env()
    while True:
        try:
            user_input = ""
            parentheses_count = 0
            while True:
                line = input(prompt if parentheses_count == 0 else "... ")
                user_input += line + "\n"
                parentheses_count += count_parentheses(line)
                if parentheses_count == 0 and line.strip() != '':
                    break
            if user_input.strip() == '':
                continue
            val = evaluate(parse(user_input), global_env)
            if val is not None:
                print(schemestr(val))
        except Exception as e:
            print(f"{type(e).__name__}: {e}")

if __name__ == '__main__':
    repl()