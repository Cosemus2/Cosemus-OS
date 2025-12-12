# Necessary Imports
import os
import time
import random
from pathlib import Path
from simple_chalk import green, blue, red, yellow

# Word Correction Imports
import nltk
import re
import pattern
from nltk.stem import WordNetLemmatizer

# Time and Date Setup
from datetime import datetime
infotime = str(datetime.now())[11:16]
starttime = time.time()
date = str(datetime.now())[5:10]
uptime = 0  # in minutes

#Information
path = Path(__file__)
user = os.path.basename(os.path.dirname(path))

# Normal Messages
messages = [
    f"Welcome to CosOs, {user}!",
    f"Current time is {infotime}.",
    "Type 'help' for a list of commands.",
    "Remember to take breaks and stretch!",
    "Did you know? You can create directories with 'mkdir <dirname>'.",
    "System initialization complete.",
    "Access granted.",
    "All systems operational.",
    "Ready when you are.",
    "Standing by for your command.",
    "Welcome! System uptime: 0 minutes. Let’s change that.",
    "Hello there! Did you know you can clear the screen with the 'clear' command?",
    "Greetings! Remember, you can always type 'help' if you need assistance.",
    "Salutations! Fun fact: The first computer bug was an actual moth found in a computer.",
    "Hi! Pro tip: Use 'mkdir <dirname>' to create a new directory.",
    "Hey! Did you know? The first 1GB hard drive was announced in 1980, weighed over 500 pounds, and cost $40,000.",
    "Welcome aboard!",
]
# Holiday Messages
holidays = [["Christmas Eve", "12-24"], ["Christmas", "12-25"], ["Hallow's Eve", "10-30"], ["Halloween", "10-31"], ["New Year's Eve", "12-31"], ["New Year's Day", "01-01"], ["Valentine's Day", "02-14"]]
for sublist in holidays:
    if date in sublist:
        holiday = sublist[0]
    else:
        holiday = None

try:
    if holiday == "Christmas Eve":
        hMessages = [
            "The stockings look suspiciously full tonight...",
            "Hope you double-checked the chimney clearance.",
            "Santa is doing his pre-flight stretches right now.",
            "Only hours left until wrapping paper chaos.",
            "The calm before the *jingling* storm.",
            "Don't fall asleep… he’s watching."
        ]

    elif holiday == "Christmas":
        hMessages = [
            "Merry Christmas, you magnificent creature!",
            "Did the gift you wanted actually show up?",
            "Time to eat until movement becomes optional.",
            "May your batteries be included and your assembly be minimal.",
            "The tree looks proud of you today."
        ]

    elif holiday == "Hallow's Eve":
        hMessages = [
            "The night is thinner than usual… listen closely.",
            "Something just moved behind you. Probably.",
            "Candy is bait. Don’t fall for it.",
            "Whispers travel farther tonight.",
            "If a shadow steps out of line… don’t mention it."
        ]

    elif holiday == "Halloween":
        hMessages = [
            "BOO! …Too early? Too late?",
            "Monsters get today off, so I’m filling in.",
            "Pumpkins are judging you silently.",
            "Hope your costume is scarier than your Wi-Fi connection."
        ]

    elif holiday == "New Year's Eve":
        hMessages = [
            "The countdown to questionable resolutions begins.",
            "Last chance to pretend you'll change tomorrow.",
            "Hope you're ready to shout numbers loudly!",
            "The clock is plotting something."
        ]

    elif holiday == "New Year's Day":
        hMessages = [
            "Behold: a perfectly fresh day with absolutely no mistakes yet.",
            "Happy New Year! Time to accidentally write the wrong date.",
            "This year is going to be legendary. Probably.",
            "You survived last year—impressive."
        ]

    elif holiday == "Valentine's Day":
        hMessages = [
            "Love is in the air… or maybe that’s just scented candles.",
            "So… who’s the lucky human?",
            "May your chocolates be high-quality and your dates punctual.",
            "It’s the perfect day to panic-buy flowers."
        ]

except:
    None

try:
    if holiday != None:
        message = random.choice(hMessages)
    else:
        message = random.choice(messages)
except:
    None

w = []

with open(str(Path(__file__).parent) + "/final.txt", 'r', encoding="utf8") as f:
    file_name_data = f.read()
    file_name_data = file_name_data.lower()
    w = re.findall('\w+', file_name_data)
main_set = set(w)

def counting_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
def prob_cal(word_count_dict):
    probs = {}
    m = sum(word_count_dict.values())
    for key in word_count_dict.keys():
        probs[key] = word_count_dict[key] / m
    return probs
def LemmWord(word):
    return list(lexeme(wd) for wd in word.split())[0]
def DeleteLetter(word):
    delete_list = []
    split_list = []
    for i in range(len(word)):
        split_list.append((word[0:i], word[i:]))

    for a, b in split_list:
        delete_list.append(a + b[1:])
    return delete_list
def Switch_(word):
    split_list = []
    switch_l = []

    for i in range(len(word)):
        split_list.append((word[0:i], word[i:]))

    switch_l = [a + b[1] + b[0] + b[2:] for a, b in split_list if len(b) >= 2]
    return switch_l
def Replace_(word):
    split_l = []
    replace_list = []

    for i in range(len(word)):
        split_l.append((word[0:i], word[i:]))
    alphs = 'abcdefghijklmnopqrstuvwxyz'
    replace_list = [a + l + (b[1:] if len(b) > 1 else '')
                    for a, b in split_l if b for l in alphs]
    return replace_list
def insert_(word):
    split_l = []
    insert_list = []

    for i in range(len(word) + 1):
        split_l.append((word[0:i], word[i:]))

    alphs = 'abcdefghijklmnopqrstuvwxyz'
    insert_list = [a + l + b for a, b in split_l for l in alphs]
    return insert_list
def colab_1(word, allow_switches=True):
    colab_1 = set()
    colab_1.update(DeleteLetter(word))
    if allow_switches:
        colab_1.update(Switch_(word))
    colab_1.update(Replace_(word))
    colab_1.update(insert_(word))
    return colab_1

def colab_2(word, allow_switches=True):
    colab_2 = set()
    edit_one = colab_1(word, allow_switches=allow_switches)
    for w in edit_one:
        if w:
            edit_two = colab_1(w, allow_switches=allow_switches)
            colab_2.update(edit_two)
    return colab_2
def get_corrections(word, probs, vocab, n=2):
    suggested_word = []
    best_suggestion = []
    suggested_word = list(
        (word in vocab and word) or colab_1(word).intersection(vocab)
        or colab_2(word).intersection(
            vocab))

    best_suggestion = [[s, probs[s]] for s in list(reversed(suggested_word))]
    return best_suggestion

def probab_cal(word_count):
    total_words = sum(word_count.values())
    probs = {word: count/total_words for word, count in word_count.items()}
    return probs

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
run = True
clear()
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
print(message)
print("-------------------------------------")
time.sleep(1)

# Command Line Loop
while run:
    command = input(green("\n" + user + "@cosos1.0.0") + blue(" ~ $ "))
    # Command Handling
    if command == "help":
       print("helped")
       continue
    elif command.startswith("mkdir "):
      w = 2
      dirname = command.split(" ")[w - 1]
      os.mkdir(__file__ + "/../" + dirname)
      continue
    elif command == "clear":
      clear()
      continue
    elif command == "uptime":
        print("Uptime: " + str(round(time.time() - starttime) // 60) + " minutes, " + str(round(time.time() - starttime)) + " seconds.")
        continue
    else:
        word_count = counting_words(main_set)
        probs = probab_cal(word_count)
        tmp_corrections = get_corrections(command, probs, main_set, 2)
        for i, word_prob in enumerate(tmp_corrections):
            if(i < 1):
                word = word_prob[0]
            else:
                break
        try:
            word
        except NameError:
            print("Command not found and no similiar command found.")
        else:
            print('Command not found. Did you mean: "' + word + '"?')
        time.sleep(1)
        continue