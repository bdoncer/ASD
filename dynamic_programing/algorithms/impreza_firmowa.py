class pracownik:
    def __init__(self,fun):
        self.fun = fun
        self.emp = []
        self.g = -1
        self.f = -1

def impreza_firmowa(A,root):
    return f(A[root])

def f(x):
    if x.f != -1:
        return x.f
    res = x.fun
    for i in range(len(x.emp)):
        res += g(A[x.emp[i]])
    return max(res,g(x))

def g(x):
    if x.g != -1:
        return x.g
    res = 0
    for i in range(len(x.emp)):
        res += f(A[x.emp[i]])
    return res

a = pracownik(3)
a.emp = [3,4]
b = pracownik(2)
b.emp = []
c = pracownik(5)
c.emp = [0,1]
d = pracownik(1)
d.emp = []
e = pracownik(1)
e.emp = []
A = [a,b,c,d,e]
print(impreza_firmowa(A,2))
