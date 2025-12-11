data = open('in10').read().strip().split('\n')

diagrams = []
for l in data:
    l = l.split(' ')
    light = [i for i in l[0][1:-1] ]
    button = [[int(i) for i in j[1:-1].split(',')] for j in l[1:-1]]
    joltage = [int(i) for i in l[-1][1:-1].split(',')]
    diagrams.append([light,button,joltage])

p1 = 0
for l,b,j in diagrams:
    on = ['.' for i in l]
    cnt = 0
    queue = [(on,cnt)]
    for s,d in queue:
        if s == l:
            p1 += d
            break
        for knop in b:
            ns = []
            for idx,o_f in enumerate(s):
                if idx in knop:
                   if s[idx] == '#':ns.append('.') 
                   else: ns.append('#')
                else: ns.append(s[idx])
            queue.append((ns,d+1))
print(p1)

from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

def solve(bs,volt):
    n_bs = len(bs)
    n_v = len(volt)
    M = np.zeros((n_v,n_bs))
    # print(M)
    for i, b in enumerate(bs):
        for idx,n in enumerate(b):
            if n == 1: M[idx,i] = 1
    b = np.array(volt) 
    c = np.ones(n_bs)
    constraints = LinearConstraint(M,b,b)
    bounds = Bounds(lb=0,ub=np.inf)
    integrality = np.ones(n_bs)

    res = milp(c,constraints=constraints,bounds=bounds,integrality=integrality).fun
    return int(res)

p2 = 0
cnt = 0
for l,bs,j in diagrams:

    state = tuple([0 for i in j])
    bs = tuple([tuple([1 if (idx in b) else 0 for idx,i in enumerate(j)]) for b in bs]) 
    j = tuple(j)
    cnt = 0
    a = (solve(bs,j))
    p2 += a

print(p2)