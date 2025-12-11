data = open('in4').read().strip().split('\n')
data = [[i for i in l] for l in data]

mx = len(data[0])
my = len(data)
def solve(grid):
    p1 = 0
    rem = []
    for idy,row in enumerate(grid):
        for idx,c in enumerate(row):
            if c == '@':
                cnt = 0
                for dy in [-1,0,1]:
                    for dx in [-1,0,1]:
                        if 0 <= idy+dy < my and 0 <= idx+dx < mx:
                            if  dy == 0 and dx == 0: continue
                            ny = idy + dy;nx=idx+dx
                            if data[ny][nx] == '@': cnt += 1
                if cnt < 4:
                    p1 += 1
                    rem.append((idy,idx))
    for y,x in rem:
        data[y][x] = '.'
    return p1
                
p2 = p1 = solve(data)
p = 1
print(p1)
while 0 != p:
    p = solve(data) 
    p2 += p 

print(p2)