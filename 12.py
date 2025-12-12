data = open('in12').read().strip().split('\n\n')
presents = [i.split('\n')[1:] for i in data[:-1]]
shapes = [[j for j in i.split(' ')] for i in data[-1].split('\n')]

p1 = 0
for line in shapes:
    size = [int(i) for i in line[0][:-1].split('x')]
    size = size[0]*size[1]
    idxs = line[1:]
    sp = 0
    for idx,c in enumerate(idxs):
        a = presents[idx]
        sa = ''.join(a).count('#')
        sp += int(c)*sa
    diff = size-sp
    if diff > 0:
        p1 += 1
print(p1)