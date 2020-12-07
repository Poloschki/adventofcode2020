with open("puzzle") as f:
    lines= f.read().splitlines()

copy1 = lines
copy2 = lines

for i in range(len(copy1)-1):
    for j in range(len(copy2)-1):
        a = int(copy1[i])
        b = int(copy2[j])

        if ( a+b ) == 2020:
            print (a*b)

