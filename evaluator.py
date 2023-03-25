def evaluate(x, env):
    if isinstance(x, str):
        return env[x]
    elif not isinstance(x, list):
        return x
    op, *args = x
    if op == 'quote':
        return args[0]
    elif op == 'if':
        (test, conseq, alt) = args
        exp = (conseq if evaluate(test, env) else alt)
        return evaluate(exp, env)
    elif op == 'define':
        (symbol, exp) = args
        env[symbol] = evaluate(exp, env)
    elif op == 'lambda':
        (params, body) = args
        return lambda *arg_values: evaluate(body, extend_env(env, params, arg_values))
    elif op == 'defunc':
        (symbol, params, body) = args
        env[symbol] = evaluate(['lambda', params, body], env)
    else:
        proc = evaluate(op, env)
        vals = [evaluate(arg, env) for arg in args]
        return proc(*vals)

def extend_env(env, params, arg_values):
    new_env = env.copy()
    for param, value in zip(params, arg_values):
        new_env[param] = value
    return new_env

def initial_env():
    env = {
        '+': lambda *args: sum(args),
        '-': lambda a, b: a - b,
        '*': lambda *args: 1 if len(args) == 0 else args[0] * args[1],
        '/': lambda a, b: a / b,
        '>': lambda a, b: a > b,
        '<': lambda a,b: a < b,
        '>=': lambda a, b: a >= b,
        '<=': lambda a, b: a <= b,
        '=': lambda a, b: a == b,
        'abs': abs,
        'append': lambda x, y: x + y,
        'begin': lambda *x: x[-1],
        'car': lambda x: x[0],
        'cdr': lambda x: x[1:],
        'cons': lambda x, y: [x] + y,
        'eq?': lambda x, y: x == y,
        'expt': pow,
        'equal?': lambda x, y: x == y,
        'length': len,
        'list': lambda *args: list(args),
        'list?': lambda x: isinstance(x, list),
        'map': lambda *args: list(map(*args)),
        'max': max,
        'min': min,
        'not': lambda x: not x,
        'null?': lambda x: x == [],
        'number?': lambda x: isinstance(x, (int, float)),
        'procedure?': callable,
        'round': round,
        'symbol?': lambda x: isinstance(x, str),
    }
    return env
