import os
import time
from pathlib import Path
from simple_chalk import green, blue, red, yellow

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
user = os.path.basename(os.path.dirname(path))
run = True
print("""   _____           ____   _____ 
  / ____|         / __ \ / ____|
 | |     ___  ___| |  | | (___  
 | |    / _ \/ __| |  | |\___ \ 
 | |___| (_) \__ \ |__| |____) |
  \_____\___/|___/\____/|_____/ 

                                """)
time.sleep(1)
clear()
print("-------------------------------------")
print("Welcome to CosOs, " + user + "!")
print("-------------------------------------")
time.sleep(4)
while run:
    clear()
    command = input(green("\n" + user + "@cosos1.0.0") + blue(" ~ $ "))
    if command == "test":
       print("tested")
