x,y=[int(x) for x in input().strip().split()]
count=256*256
while(count!=0):
    print(x,y)
    x += 1
    if x == 256:
        y -= 1
        if y == -1 and x== 256:
            y= 255
        x = 0
