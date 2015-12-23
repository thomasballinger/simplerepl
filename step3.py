import sys
import blessed
import ast

term = blessed.Terminal()


def write(s):
    sys.stdout.write(s)
    sys.stdout.flush()


def display(current_line, msg, lines):
    """Paints a simple scene after clearing screen:

    +===================+
    |CURRENT LINE| <- cursor goes here
    |last message       |
    |                   |
    |                   |
    +===================+"""
    write(term.clear)  # also moves cursor to top left
    write('\n')
    write(msg)
    write('\n')
    for line in lines[-20:]:
        print line
    write(term.cuu(1000))
    write('\r')  # cursor to beginning of line
    write(current_line.upper())


def is_valid_python(s):
    try:
        ast.parse(s)
    except SyntaxError:
        return False
    else:
        return True


def run_code(s):
    try:
        return '>>> ' + s + '\n' + repr(eval(s))
    except:
        exec(s)
        return '>>> ' + s


if __name__ == '__main__':
    line = ''
    valid_lines = []

    with term.cbreak():
        while True:
            inp = term.inkey()
            if inp == '\n':
                if is_valid_python(line):
                    valid_lines.append(run_code(line))
                    line = ''
            elif inp.code == term.KEY_DELETE:
                line = line[:-1]
            elif inp.is_sequence:
                pass
            else:
                line += inp

            msg = '(^.^)' if is_valid_python(line) else '*_*'
            display(line, msg, valid_lines)
