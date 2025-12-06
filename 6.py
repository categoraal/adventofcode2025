data = open('in6').read().split('\n')
parsed = []
for line in data:
    line+=' '
    l = []
    s = ''
    for c in line:
        if c != ' ':
            s += c
        elif c == ' ':
            if s != '':
                l.append(s)
                s = ''
    parsed.append([i for i in l])

nums = parsed[:-1]
operations = parsed[-1]

sols = parsed[0]
for line in nums[1:]:
    ns = []
    for op,a,b in zip(operations,line,sols):
        a = int(a);b = int(b)
        if op == '*':
            ns.append(a*b)
        else:
            ns.append(a+b)
    sols = ns
print(sum(sols))

data = [[i for i in l] for l in data[:-1]]
data = list(zip(*data))
data = [''.join(i) for i in data]
data.append(' ')

p2 = 0
sols = []
tp = 0 
cnt = 0
for c in data:
    c = c.strip()
    if tp == 0 and c != '':
        tp = int(c)
    elif c != '': #and tp > 0:
        if operations[cnt] == '+':
            tp += int(c)
        else:
            tp *= int(c)
    else:
        p2 += tp
        sols.append(tp)
        tp = 0
        cnt += 1

print(p2)
