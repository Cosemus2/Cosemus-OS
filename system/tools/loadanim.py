import time
from system.defaultcmds.clear import clear


def load(text):
    print(text + ".")
    time.sleep(0.5)
    clear()
    print(text + "..")
    time.sleep(0.5)
    clear()
    print(text + "...")
    time.sleep(2)
    clear()
