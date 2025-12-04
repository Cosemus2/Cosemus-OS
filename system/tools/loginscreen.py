import curses
import time
import os
import shutil
import importlib.util

path = "system/tools/encryption.py"
mname = "encryption"

spec = importlib.util.spec_from_file_location(mname, path)
encryption = importlib.util.module_from_spec(spec)
spec.loader.exec_module(encryption)

def encrypt(text, s):
    text = encryption.encrypt(text, s)
    return text
def decrypt(text, s):
    text = encryption.decrypt(text,s)
    return text

def my_raw_input(stdscr, r, c, prompt_string):
  curses.echo() 
  stdscr.addstr(r, c, prompt_string)
  stdscr.refresh()
  input = stdscr.getstr(r + 1, c, 20)
  return input

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Welcome to CosOs! Please create an account, or login to an existing one.")
    options = ["Login", "Sign Up"]
    selected_option = 0

    while True:
        for i, option in enumerate(options):
            if i == selected_option:
                stdscr.addstr(i + 2, 0, option, curses.A_REVERSE)
            else:
                stdscr.addstr(i + 2, 0, option)

        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected_option = max(0, selected_option - 1)
        elif key == curses.KEY_DOWN:
            selected_option = min(len(options) - 1, selected_option + 1)
        elif key == ord('\n'): # Enter key
            break

        stdscr.refresh()
    if selected_option == 0:
        stdscr.erase()
        stdscr.addstr(0, 0, "Please enter your username and password.")
        enteredusername = my_raw_input(stdscr, 1, 0, "Username: ").decode('utf-8')
        
        with open('system/Users/USERNAMES.txt') as f:
            AllUsernames = f.read().splitlines()

        with open('system/Users/PASSWORDS.txt') as g:
            AllPasswords = g.read().splitlines()
            
        other = []
        other2 = []
        for Key in AllUsernames:
            other.append(decrypt(Key, -7))
        for Key2 in AllPasswords:
          other2.append(decrypt(Key2, -7))

        if enteredusername in other:
            indextofind = other.index(enteredusername)
            stdscr.erase()
            stdscr.refresh()
            enteredpassword = my_raw_input(stdscr, 0, 0, "Password: ").decode('utf-8')
            if enteredpassword == other2[indextofind]:
                stdscr.erase()
                stdscr.refresh()
                time.sleep(2)
                stdscr.addstr("Press any key to continue.")
                stdscr.refresh()
                stdscr.getch()
                curses.endwin()
                os.system("python system/Users/" + enteredusername + "/cmdline.py")

            else:
                stdscr.erase()
                stdscr.refresh()
                stdscr.addstr(0, 0, "Incorrect password, please try again.")
                stdscr.refresh()
                time.sleep(2)
        else:
            stdscr.erase()
            stdscr.refresh()
            stdscr.addstr(0, 0, "Username not found, please sign up or try again.")
            stdscr.refresh()
            time.sleep(2)


    if selected_option == 1:
        stdscr.erase()
        stdscr.addstr(0, 0, "Please enter your desired username and password.")
        newusername = my_raw_input(stdscr, 1, 0, "Username: ").decode('utf-8')

        with open('system/Users/USERNAMES.txt') as f:
            AllUsernames = f.read().splitlines()

        with open('system/Users/PASSWORDS.txt') as g:
            AllPasswords = g.read().splitlines()

        other = []
        other2 = []
        for Key in AllUsernames:
            other.append(decrypt(Key, -7))
        for Key2 in AllPasswords:
          other2.append(decrypt(Key2, -7))

        if newusername in other:
            stdscr.erase()
            stdscr.refresh()
            stdscr.addstr(0, 0, "Username already exists, please try again.")
            stdscr.refresh()
            time.sleep(2)
        else:
            stdscr.erase()
            stdscr.refresh()
            newpassword = my_raw_input(stdscr, 0, 0, "Password: ").decode('utf-8')
            stdscr.erase()
            stdscr.refresh()
            with open('system/Users/USERNAMES.txt', 'a') as f:
                f.write(encrypt(newusername, 7) + "\n")

            with open('system/Users/PASSWORDS.txt', 'a') as g:
                g.write(encrypt(newpassword, 7) + "\n")
            os.mkdir("system/Users/" + newusername)
            os.mkdir("system/Users/" + newusername + "/Programs")
            os.mkdir("system/Users/" + newusername + "/Documents")
            os.mkdir("system/Users/" + newusername + "/Data")
            open("system/Users/" + newusername + "/cmdline.py", "w")
            shutil.copyfile("system/cmdlinetemplate.py", "system/Users/" + newusername + 
            "/cmdline.py")
curses.wrapper(main)