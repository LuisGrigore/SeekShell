import time
import sys

def show_thinking():

    simbolos = ['|', '/', '-', '\\']
    delay = 0.2

    for simbolo in simbolos:
        sys.stdout.write(f'\rThinking... {simbolo}')
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\r' + ' ' * 20 + '\r')
    sys.stdout.flush()

