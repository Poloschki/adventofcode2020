with open("puzzle") as f:
    lines= f.read().splitlines()

copy1 = lines
copy2 = lines
copy3 = lines

for i in range(len(copy1)-1):
    for j in range(len(copy2)-1):
        for k in range(len(copy3)-1):
            c = int(copy3[k])
            a = int(copy1[i])
            b = int(copy2[j])

            if ( a+b+c ) == 2020:
                print (a*b*c)

