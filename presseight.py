import sys
import blessed


def get8chars():
    term = blessed.Terminal()
    line = ''

    with term.cbreak():
        while len(line) < 8:
            inp = term.inkey()
            if inp == '\n':
                sys.stdout.write('\n')
                sys.stdout.write('\r')
                sys.stdout.write('need more characters first!')
                sys.stdout.write(term.cuu(1))
            elif inp.code == term.KEY_DELETE:
                line = line[:-1]
            elif inp.is_sequence:
                pass
            else:
                line += inp
            sys.stdout.write('\r')
            sys.stdout.write(term.clear_eol())
            sys.stdout.write('.'*len(line))
            sys.stdout.flush()
    sys.stdout.write('\n')
    sys.stdout.flush()
    return line

if __name__ == '__main__':
    print('type eight characters for good luck')
    pw = get8chars()
    print('you typed', pw)
