data = open('in7').read().strip().split('\n')
grid = {}
cnt = 0
for row,l in enumerate(data):
    for col, c in enumerate(l):
        grid[(row,col)] = c
        if c == 'S':start = (row,col)
        if c == '^':cnt += 1
queue = [start]

p1 = 0
sols = set()
for r,c in queue:
    p = grid[(r,c)] 
    if p == '^':
        sols.add((r,c))
        for i in [-1,1]:
            if (r+1,c+i) in queue:continue
            queue.append((r+1,c+i))
    else:
        if (r+1,c) in grid:
            queue.append((r+1,c))

print(len(sols))

data = [[0 if i == '.' else i for i in j] for j in data]
a,b = start
data[a][b] = 1
for idr,line in enumerate(data[1:]):
    idr += 1
    for idc,c in enumerate(line):
        if c == '^':
            data[idr][idc+1] += data[idr-1][idc]
            data[idr][idc-1] += data[idr-1][idc]
        else:
            up = data[idr-1][idc]
            if type(up) == int:
                data[idr][idc] = c+up
print(sum(data[-1]))
