import math

print('\nnomor 1 :')
def a(x):
    return x**2
print(a(5))
#di ubah menjadi lambda:
a=lambda x: (x**2)
print(a(9))


print('\nnomor 2 :')
def b(x,y):
    return math.sqrt(x**2 + y**2)
print(b(8,7))
#di ubah menjadi lambda:
b=lambda x,y: math.sqrt(x**2 + y**2)
print(b(8,7))


print('\nnomor 3 :')
def c(*args):
    return sum(args)/len(args)
print(c(9))
#di ubah menjadi lambda:
c=lambda *args:sum(args)/len(args)
print(c(9))


print('\nnomor 4 :')
def d(s):
    return "".join(set(s))
print(d("starlet car"))
#diubah menjadi lambda:
d=lambda s: "".join(set(s))
print(d("startlet car"))