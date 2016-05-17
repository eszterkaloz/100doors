doors = [0]*101

for x_open in range (1,101):
    for y_time in range (0,101,x_open):
        doors[y_time]+=1

for x_open in range (len(doors)):
    if doors[x_open]%2 == 1:
        print(x_open)
