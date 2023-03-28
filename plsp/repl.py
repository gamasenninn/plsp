from plsp.lparser import parse
from plsp.evaluator import evaluate, initial_env
from plsp.utils import schemestr

def count_parentheses(s):
    return s.count('(') - s.count(')')

def repl_main(prompt='plsp> '):
    global_env = initial_env()
    while True:
        try:
            user_input = ""
            parentheses_count = 0
            while True:
                try:
                    line = input(prompt if parentheses_count == 0 else "... ")
                except EOFError:  #Ctrl-D
                    print()
                    return
                except KeyboardInterrupt:  #Ctrl-C
                    print('\nKeyboardInterrupt')
                    return
                user_input += line + "\n"
                parentheses_count += count_parentheses(line)
                if parentheses_count == 0 and line.strip() != '':
                    break
            if user_input.strip() == '':
                continue
            if user_input.strip() == 'quit':
                return
            val = evaluate(parse(user_input), global_env)
            if val is not None:
                print(schemestr(val))
        except Exception as e:
            print(f"{type(e).__name__}: {e}")

#if __name__ == '__main__':
#    repl()