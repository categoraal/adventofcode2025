import matplotlib.pyplot as plt

data = open('in9').read().strip().split('\n')
tiles = [[int(i) for i in j.split(',')] for j in data]
coords = list(zip(*tiles))
p1 = 0
p2 = 0
for idx,t1 in enumerate(tiles[:-1]):
    for t2 in tiles[idx+1:]:
        x1,y1 = t1
        x2,y2 = t2
        area = (abs((t1[0]-t2[0]))+1)*(abs((t1[1]-t2[1]))+1)
        p1 = area if area > p1 else p1 


print(p1)
# plt.plot(coords[0],coords[1])
# plt.show()
# By inspection check the coords. 

a1 = (67420-50319+1)*(94651-5467+1)#up
a2 = (48450-34172+1)*(94651-3843+1)#down
print(print(max(a1,a2)))