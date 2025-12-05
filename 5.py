data = open('in5').read().strip().split('\n\n')
r,s = data 
r = [[int(i) for i in l.split('-')] for l in r.split('\n')]
s = s.split('\n')
p1 = 0
for i in s:
    i = int(i)
    for a,b in r:
        if a <= i <= b:
            p1 += 1
            break
print(p1)
       
r.sort(key=lambda x:x[0])  
a1,a2 = r[0]
nr = [[a1,a2]]
for a,b in r:
    f = 0
    for idn,cc in enumerate(nr):
        na,nb=cc
        if na <= a <= nb and nb <= b:
            f = 1
            nr[idn][1] = b
            break
        if na <= a < nb and nb > b:
            f = 1
            break
    if f == 0:
        nr.append([a,b])

p2 = 0
for a,b in nr:
    p2 += b-a+1
print(p2)