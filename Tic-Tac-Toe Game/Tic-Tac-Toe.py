gamesize=0
def Player1():
    ipt1 = int(input("Player 1 turn--> "))
    if 0>ipt1 or gamesize**2 <= ipt1 :
        print("Please enter a valid number")
    elif B[ipt1] == "X":
        print("You have made this choice before")
    elif B[ipt1] == "O":
        print("The other player select this cell before.")
    else:
        B[ipt1] = "X"
    for l in range(gamesize ** 2):
        print(str(B[l]).rjust(3), end=" ")
        if (l+1)% gamesize == 0:
            print()

def Player2():
    ipt2 = int(input("Player 2 turn--> "))
    if 0>ipt2 or gamesize**2 <= ipt2 :
        print("Please enter a valid number")
    elif B[ipt2] == "O":
        print("You have made this choice before")
    elif B[ipt2] == "X":
        print("The other player select this cell before.")
    else:
        B[ipt2] = "O"
    for l in range(gamesize ** 2):
        print(str(B[l]).rjust(3), end=" ")
        if (l+1)% gamesize == 0:
            print()
def draw():
    if not any(isinstance(x, int) for x in B): return True
winner=""
tot=0
def wincond():
    global winner, tot
    while 1:
        Player1()
        for k in range(gamesize):
            for n in range(gamesize):
                n*=gamesize
                if B[k::gamesize].count("X") == gamesize or B[k::gamesize+1].count("X") == gamesize or B[n:n+gamesize].count("X") == gamesize or B[gamesize-1:(gamesize**2)-1:gamesize-1].count("X") == gamesize:
                    winner = "X"
                    tot=1
                elif B[k::gamesize].count("O") == gamesize or B[k::gamesize+1].count("O") == gamesize or B[n:n+gamesize].count("O") == gamesize or B[gamesize:(gamesize**2)-1:gamesize-1].count("O") == gamesize:
                    winner = "O"
                    tot=1

        if tot==1:
            break
        elif draw()==True:
            print("no winner")
            break
        Player2()
        for k in range(gamesize):
            for n in range(gamesize):
                n*=gamesize
                if B[k::gamesize].count("X") == gamesize or B[k::gamesize+1].count("X") == gamesize or B[n:n+gamesize].count("X") == gamesize or B[gamesize-1:(gamesize**2)-1:gamesize-1].count("X") == gamesize:
                    winner = "X"
                    tot=1
                elif B[k::gamesize].count("O") == gamesize or B[k::gamesize+1].count("O") == gamesize or B[n:n+gamesize].count("O") == gamesize or B[gamesize:(gamesize**2)-1:gamesize-1].count("O") == gamesize:
                    winner = "O"
                    tot=1

        if tot==1:
            break
        elif draw()==True:
            print("no winner")
            break

def valid():
    global gamesize
    try:
        gamesize = int(input("What Size Game GoPy?"))
        if gamesize<3:
           print("Please give an integer more than 2")
        if gamesize<0:
            print("Please give a positive number")
    except TypeError:
        print("Please give an integer")
valid()
B = list(range(gamesize**2))
for l in range(gamesize**2):
    print(str(B[l]).rjust(3),end=" ")
    if (l+1)% gamesize==0:
        print()
wincond()
print("Winner:", winner)