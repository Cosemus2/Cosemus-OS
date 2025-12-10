from system.tools.loadanim import load
from system.defaultcmds.clear import clear
import time
import os

print("Please wait while we get stuff ready.")
time.sleep(3)
clear()
import nltk
nltk.download('all')
clear()
for i in range(1):
  load("Booting CosOs - 1.0.0")
time.sleep(1)
clear()
os.system("python system/tools/loginscreen.py")
