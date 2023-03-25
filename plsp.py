#plsp.py
import sys
from repl import repl
from file_runner import run_file

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        run_file(filename)
    else:
        repl()