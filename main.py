from system.tools.loadanim import load
from system.defaultcmds.clear import clear
import time
import os
import nltk
print("Please wait while we get stuff ready.")
time.sleep(2)
nltk.download('all')
os.system("python -m pip install windows-curses")
os.system("python -m pip install pattern")
os.system("python -m pip install simple-chalk")
clear()
for i in range(1):
  load("Booting CosOs - 1.0.0")
time.sleep(1)
clear()
os.system("python system/tools/loginscreen.py")
