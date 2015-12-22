Want to make a simple interactive REPL in Python?

Get started by

* installing blessed

    pip install blessed

* on keystroke, update the screen:

```
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
```

Now if you want to show other information, you can print it on each keystroke.

(see step2.py and step3.py for this)
