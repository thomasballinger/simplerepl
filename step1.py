import sys
import blessed

term = blessed.Terminal()
line = ''

with term.cbreak():
    while True:
        inp = term.inkey()
        if inp == '\n':
            print('')
            print("you hit enter!")
            print(line.upper())
            line = ''
        else:
            line += inp
            sys.stdout.write('\r')
            sys.stdout.write(line)
            sys.stdout.flush()
