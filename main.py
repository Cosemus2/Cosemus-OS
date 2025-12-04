from system.tools.loadanim import load
from system.defaultcmds.clear import clear
from system.tools.wait import wait
for i in range(1):
  load("Booting CosOs - 1.0.0")
wait(1)
clear()
wait(0.1)
exec(open("system/tools/loginscreen.py").read())