data = open('in2').read().strip().split(',')

def invalid(a,b):
    r1 = 0
    res2 = [] 
    primes = {0:[1]}
    for i in range(a,b+1):
        t = str(i)
        if t[:int(len(t)/2)] == t[int(len(t)/2):]:
            if len(t)%2==1:continue
            r1 +=int(t)
        l = len(t)
        if l == 1:continue
        if l in primes:p = primes[l]
        else:
            p = [1]
            for n in range(2,l+1):
                if l%n==0 and l >= 2*n:
                    p.append(n)
            primes[l] = p
        for n in p:
            splits = []
            for s in range(0,l,n):
                splits.append(t[s:s+n])
            if len(set(splits)) == 1:
                res2.append(i)
    r2 = sum(list(set(res2)))
    return r1,r2 


p1 = p2 = 0
for line in data:
    a,b = line.split('-')
    r1,r2 = invalid(int(a),int(b))
    p1+=r1;p2+=r2

print(p1)
print(p2)