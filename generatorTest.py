def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b ,a+b
        n = n + 1
    return 'done'
f = fib(5)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
try:
   print(next(f))
except StopIteration as e:
    print('value',e.value)

def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i-1] + L[i] for i in range(len(L))]

n = 0
for m in triangles():
    print(m)
    n = n + 1
    if n == 10:
        break
