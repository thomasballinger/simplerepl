import sys
import blessed

term = blessed.Terminal()
line = ''
msg = ''


def write(s):
    sys.stdout.write(s)
    sys.stdout.flush()


def display(current_line, msg):
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
    write(term.cuu(1))
    write('\r')  # cursor to beginning of line
    write(current_line.upper())

if __name__ == '__main__':
    with term.cbreak():
        while True:
            inp = term.inkey()
            if inp == '\n':
                msg = line
                line = ''
            elif inp.code == term.KEY_DELETE:
                line = line[:-1]
            elif inp.is_sequence:
                pass
            else:
                line += inp
            display(line, 'last line: '+msg)
