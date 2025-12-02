data = open('in1').read().strip().split('\n')

p = 50
p1 = p2 = 0
for l in data:
    r = 1 if l[0] == 'R' else -1
    n = int(l[1:])
    for i in range(n):
        p += r
        if p == -1: p = 99 
        if p == 100: p = 0
        if p == 0:p2+=1
    if p == 0: p1 += 1
    
print(p1,p2)