import time
import tty
import sys
import Queue
from threading import Thread


q = Queue.Queue()
running_thread = None


def read_forever():
    tty.setcbreak(sys.stdin)
    while True:
        q.put(sys.stdin.read(1))


def read_nonblocking():
    """Returns a byte read from stdin or an empty string"""
    global running_thread
    if not running_thread:
        running_thread = Thread(target=read_forever)
        running_thread.daemon = True
        running_thread.start()
    inp = []
    try:
        while True:
            inp.append(q.get_nowait())
    except Queue.Empty:
        return ''.join(inp)


if __name__ == '__main__':
    print('got', read_nonblocking())
    time.sleep(1)
    print('got', read_nonblocking())
    time.sleep(1)
    print('got', read_nonblocking())
