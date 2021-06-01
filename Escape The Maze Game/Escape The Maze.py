import sys
file1 = open(sys.argv[1], "r")
file2 = open(sys.argv[2], "r")
mazhe = int(sys.argv[3])
maze=[]
mazeh=[]
for line in file1.readlines():
    lislin = list(line.rstrip('\n'))
    maze.append(lislin)
print(maze)
for ele in maze:
    try:
        start= ele.index("S")
        roww= maze.index(ele)
        break
    except:
        continue

noe = len(maze)

def findpath(x, y):
    if maze[x][y] == "F":
        return True
    elif maze[x][y] == "W":
        return False
    elif maze[x][y] == 3:
        return False
    if maze[x][y] != "S" and maze[x][y] != "F":
        maze[x][y] = 3
    if ((x < noe - 1 and findpath(x + 1, y)) or (y > 0 and findpath(x, y-1)) or (x > 0 and findpath(x-1, y)) or (y < noe-1 and findpath(x, y+1))):
        if maze[x][y] != "S" and maze[x][y] != "F":
            maze[x][y] = 1
        return True
    return False

findpath(roww, start)

for sub in maze:
    for char in sub:
        if char != "S" and char != "F" and char != 1:
            sub[sub.index(char)]=0
output = open(sys.argv[4], "w")
for i in maze:
    output.write(",".join(map(str,i)) + "\n")

for line in file2.readlines():
    lislinh = list(line.rstrip('\n'))
    mazeh.append(lislinh)
print(mazeh)
for ele in mazeh:
    try:
        starth = ele.index("S")
        rowwh = mazeh.index(ele)
        break
    except:
        continue
health = mazhe
noeh = len(mazeh)
def findpath1(x, y):
    global health
    if mazeh[x][y] == "F":
        return True
    elif mazeh[x][y] == "W":
        return False
    elif mazeh[x][y] == 3:
        return False
    if mazeh[x][y] != "S" and mazeh[x][y] != "F" and mazeh[x][y] != "H":
        mazeh[x][y] = 3
    if ((x < noeh - 1 and findpath1(x + 1, y)) or (y > 0 and findpath1(x, y - 1)) or (x > 0 and findpath1(x - 1, y)) or (
            y < noeh - 1 and findpath1(x, y + 1))):
        if mazeh[x][y] != "S" and mazeh[x][y] != "F" and mazeh[x][y] != "H":
            mazeh[x][y] = 1
        health -= 1
        if mazeh[x][y] == "H":
            health = mazhe
        if health <= 0:
            print("Not enough health")

        return True
    return False

findpath1(rowwh, starth)
for sub in mazeh:
    for char in sub:
        if char != "S" and char != "F" and char != 1 and char != "H":
            sub[sub.index(char)] = 0
output = open(sys.argv[4], "a")
output.write("\n")
for i in mazeh:
    output.write(",".join(map(str, i)) + "\n")

file1.close()
file2.close()
output.close()
#python assignment4.py maze.txt mazehealth.txt health time output.txt
