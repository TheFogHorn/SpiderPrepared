L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]

def by_score(t):
    return t[1]
L1 = sorted(L, key=by_name)
L2 = sorted(L, key=by_score)
#print(L1,L2)
def count():
    def f():
        print(i)
        return i*i
    fs = []
    for i in range(1, 4):
        fs.append(f)
        print(i)
   
    print(fs)
    return fs
f1, f2, f3 = count()
print(f1)
