with open("puzzle") as f:
    lines= f.read().splitlines()

count = 0 
 

for i in range(len(lines)):
    subcount = 0 
    tmp = lines[i].split("-")
    lower = tmp[0]   
    tmp = tmp[1].split(" ")
    pswd = tmp[2]
    higher = tmp[0]
    char = tmp[1][0]

    if char in pswd[int(lower)-1]:
        subcount +=1 
    if char in pswd[int(higher)-1]:
        subcount +=1

    if subcount == 1:
        count += 1        

print (count)