import os
import time
from pathlib import Path

def clear():
  os.system("cls" if os.name == "nt" else "clear")

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

path = Path(__file__)
user = os.path.basename(path).parent
print("""   _____           ____   _____ 
  / ____|         / __ \ / ____|
 | |     ___  ___| |  | | (___  
 | |    / _ \/ __| |  | |\___ \ 
 | |___| (_) \__ \ |__| |____) |
  \_____\___/|___/\____/|_____/ 

                                """)
print("-------------------------------------")
print("Welcome to CosOs, " + user + "!")
print("-------------------------------------")
