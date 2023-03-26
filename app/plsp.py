#plsp.py
import sys
from repl import repl_main
from file_runner import run_file

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        run_file(filename)
    else:
        repl_main()

if __name__ == '__main__':
    main()
