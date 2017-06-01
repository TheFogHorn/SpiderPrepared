from functools import reduce
def f(x):
    return x*x
r = map(f,[1,2,3])
print(r)
print(list(r))
def fa(x,y):
    return x*10+y
a = reduce(fa,[1,5,7,9])
print(a)
def str2float(s):
    a = s.find('.')
    times = len(s)-a-1
    c = s.replace('.','')
    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
    def fn(x,y):
        return 10*x+y
    s = reduce(fn,map(char2num,c))
    return s/(10**times)
print('str2float(\'123.456\') =', str2float('123.456'))

def cha(dd):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[dd]
b = cha('3')
print(type(b))
