with open("puzzle") as f:
    lines= f.read().splitlines()

count = 0 
 

for i in range(len(lines)):
    subcount = 0 
    tmp = lines[i].split("-")
    lower = tmp[0]   
    tmp = tmp[1].split(" ")
    pswd = tmp[2]
    max = tmp[0]
    char = tmp[1][0]

    for j in pswd:
        if char in j : 
            subcount += 1
    if subcount >= int(lower) and subcount <= int(max):
        count += 1

print (count)