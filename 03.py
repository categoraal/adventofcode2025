data = open('in3').read().strip().split('\n')

def solve(n,s):
    res = ''
    nums = [int(i) for i in s]
    b = 0
    while len(res) < n:
        tail = len(s) - n + len(res) + 1
        res += str(max(nums[b:tail]))
        b += nums[b:].index(max(nums[b:tail]))+1
    return int(res)

p1=p2=0
for l in data:
    p1 += solve(2,l)
    p2 += solve(12,l)
print(p1)
print(p2)