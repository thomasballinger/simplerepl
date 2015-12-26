Want to make a simple interactive REPL in Python?

The first step might be:

    while True:
        i = raw_input('enter a command: ')
        print(i.upper())

But if you want to create a richer experience, one that might update the
screen after each keystroke the user types, then you might need to go deeper.

Get started by installing blessed

    pip install blessed

Now let's update the screen after each keystroke:

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

what do you want to do next?

* [ask the user for a limited number of characters](presseight.py)

* [update the screen with more information](step2.py)

* [update on keystroke whether the current line is valid](step3.py)


(see step2.py and step3.py for this)
