import sys
import time
a = 0
b = 0
guessed = []
point = 0
file1 = open(sys.argv[1], "r", encoding="utf8")
file2 = open(sys.argv[2],"r", encoding="utf8")
dict1 = {line.split(":")[0]: line.split(":")[1:] for line in file1.readlines()}
dict2 = {letter.split(":")[0]: letter.split(":")[1] for letter in file2.readlines()}
listdict1 = list(dict1.keys())
valdict = list(dict1.values())
listdict2 = list(dict2.keys())
valdict2 = list(dict2.values())
for key in dict1.keys():
    print("Shuffled letters are:\t", listdict1[a].lower().replace("İ","i").replace("Ü","ü").replace("Ş","ş"),
          "\tPlease guess words for these letters with minimum three letters")
    now = time.time()
    time_limit = 30
    end_time = now + time_limit
    while time.time() < end_time:
        time_remaining = end_time - time.time()
        print("You have {:.0f} seconds remaining".format(time_remaining))
        inp = input("Guessed Word: ")
        if inp.upper() not in guessed and inp.upper() in valdict[b][0].split(","):
            guessed.append(inp)
            for let in inp.upper():
                point += int(dict2[let])
        elif inp.upper() not in valdict:
            print("your guessed word is not a valid word")
        elif inp in guessed:
            print("This word is guessed before")
    a += 1
    b += 1
    print("Score for " + key.lower() + " is " + str(point) + " and guessed words are:", end="")
    print('-'.join(guessed))
    guessed = []

file1.close()
file2.close()

#python ass3.py correct_words.txt letter_values.txt