data = open('in8').read().strip().split('\n')
coords = [tuple([int(i) for i in l.split(',')]) for l in data]

circuits = [[i] for i in coords] 
dists = dict()
ds = []
c = 0
for idx,p1 in enumerate(coords[:-1]):
    for p2 in coords[idx+1:]:
        c += 1
        d = sum([(a-b)**2 for a,b in zip(p1,p2)])
        dists[d] = (p1,p2)
        ds.append(d)
ds = sorted(ds)

cnt = 0
while len(circuits) > 1:
    p1,p2 = dists[ds[cnt]]
    f=0 
    mem = []
    for circuit in circuits:
        if p1 in circuit or p2 in circuit:
            if p1 not in circuit:circuit.append(p1)
            if p2 not in circuit:circuit.append(p2) 
            mem.append(circuit)
            f = 1
    if f == 0:
        circuits.append([p1,p2])   
    if len(mem) > 1:
        for i in mem:
            circuits.remove(i)
        circuits.append(list(set(sum(mem,[]))))
    cnt += 1
    if cnt == 1000:
        lens = [len(i) for i in circuits]
        ll = sorted(lens)
        print(ll[-1]*ll[-2]*ll[-3])
    if len(circuits) == 1:
        print(p1[0]*p2[0])