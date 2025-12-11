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
print(max(a1,a2))
vert = {}
hori = {}
edge = [tuple(tiles[-1])]
for t in tiles:
    # print(t)
    x1,y1 = edge[-1]
    x2,y2 = t
    if x1 not in vert:vert[x1] = [y1]
    else: vert[x1].append(y1)
    if y1 not in hori:hori[y1] = [x1]
    else: hori[y1].append(x1)
    # print(x1,y1,x2,y2) 
    if x1 != x2:    
        np = x1
        if x1 < x2:
            while np < x2:
                np += 1             
                edge.append((np,y2))
                # if np == x2: continue
                if np in vert: vert[np].append(y2)
                else: vert[np] = [y2]
        else:
            while np > x2:
                np -= 1
                edge.append((np,y2))
                if np == x2:continue
                if np in vert: vert[np].append(y2)
                else: vert[np] = [y2]
    else:
        np = y1
        if y1 < y2:
            while np < y2:
                np += 1             
                edge.append((x1,np))
                # if np == y2:continue
                if np in hori: hori[np].append(x2)
                else: hori[np] = [x2]
        else:
            while np > y2:
                np -= 1
                edge.append((x1,np)) 
                if np == y2: continue
                if np in hori: hori[np].append(x2)
                else: hori[np] = [x2]

p1,p2 = max(tiles)
queue = [(p1-1,p2)]
seen = set()

print(queue)
# for 
# print(edge)
for i in hori:
    hori[i] = sorted(list(set(hori[i])))
for i in vert:
    vert[i] = sorted(list(set(vert[i])))


p2 = 0
cnt = 0
for idx,t1 in enumerate(tiles[:-1]):
    for t2 in tiles[idx+1:]:
        x1,y1 = t1
        x2,y2 = t2
        v1 = vert[x1] 
        v2 = vert[x2]
        c1 = c2 = 0
        f=1
        for i in v1: 
            # c1 = c1 + 1 if i < y1 else c1 
            if min(y1,y2) <= i <= max(y1,y2) and y1 != y2:f=0
        for i in v2:
            if min(y1,y2) <= i <= max(y1,y2) and y1 != y2:f=0
        # for i in v2: c2 = c2 + 1 if i < y2 else c2
        # if c1%2==1 and c2%2==1: f=1

        area = (abs((t1[0]-t2[0]))+1)*(abs((t1[1]-t2[1]))+1)
        # print(area,x1,y1,x2,y2,f)
        if f:
            p2 = area if area > p2 else p2 
        cnt += 1
print(p2)
# print(vert)
# for a,b in tiles:
plt.plot(coords[0],coords[1])
    # plt.scatter(a,b)
plt.show()
# print(boundary)
# # plt.plot(coords[0],coords[1])
# # for a,b in boundary:
# #     plt.scatter(a,b,c='r')
# # plt.show()
# plt.plot(boundary)
# plt.show()