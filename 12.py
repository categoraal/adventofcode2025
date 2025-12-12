d = open('in12').read().split('\n\n')
p = [i.count('#') for i in d[:-1]]
sh = [[j for j in i.split(' ')] for i in d[-1].split('\n')]

p1 = 0
for l in sh:
    s = [int(i) for i in l[0][:-1].split('x')]
    s = s[0]*s[1]
    if s-sum([p[idx]*int(c) for idx,c in enumerate(l[1:])])>0:p1 += 1
print(p1)