file = open("people.txt", "r")
lines = file.readlines()
for line in lines:
    print(line)