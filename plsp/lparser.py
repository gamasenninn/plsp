def parse(program):
    return read_from_tokens(tokenize(program))

def tokenize(s):
    result = []
    current_token = ''
    in_quotes = False

    for char in s:
        if char in ['"',"'"]:
            in_quotes = not in_quotes
            if not in_quotes:
                result.append(f'"{current_token}"')
                current_token = ''
        elif char == '(' or char == ')' or char.isspace():
            if in_quotes:
                current_token += char
            else:
                if current_token:
                    result.append(current_token)
                    current_token = ''
                if char == '(' or char == ')':
                    result.append(char)
        else:
            current_token += char

    if in_quotes:
        raise SyntaxError('unbalanced quotes')

    if current_token:
        result.append(current_token)

    return result

def read_from_tokens(tokens):
    if len(tokens) == 0:
        raise SyntaxError("unexpected EOF")
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0)
        return L
    elif token == ')':
        raise SyntaxError("unexpected )")
    elif token.startswith("'") or token.startswith('"'):  # 変更: クォートされた文字列の処理
        return ['quote', token[1:-1]]  # クォートされた文字列を quote 式に変換
    else:
        return atom(token)

def atom(token):
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return str(token)
