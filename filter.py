inList = open(r"in.txt","r")
outList = open(r"clean.txt", "w+")
swears = open(r"swears.txt","r")

wordsArray = inList.readlines()
swearsArray = swears.readlines()

for a in range(len(swearsArray)):
    swearsArray[a] = swearsArray[a].strip("\n")
for n in range(len(wordsArray)):
    wordsArray[n] = wordsArray[n].strip("\n")

for i in range(len(swearsArray)):
    try:
        wordsArray.remove(swearsArray[i])
    except ValueError:
        pass

outList.write("\n".join(wordsArray))

inList.close()
outList.close()
swears.close()
