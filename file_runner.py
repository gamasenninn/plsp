from repl import evaluate, parse, initial_env, schemestr

def run_file(filename):
    with open(filename, 'r') as file:
        program = file.read()
        global_env = initial_env()
        print("p:",parse(program))
        try:
            val = evaluate(parse(program), global_env)
            if val is not None:
                print(schemestr(val))
        except Exception as e:
            print(f"{type(e).__name__}: {e}")