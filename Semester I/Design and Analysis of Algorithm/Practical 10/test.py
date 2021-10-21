b = [3,1,6]
y = [5,7,8]
t = 1

def reminder(i ,j):
    x = i%j
    print(f'{x} {i} {j}')
    if x == i:
        return reminder(x,j)
    return x
    

for i in y:
    t *= i

Ni = [ t/i for i in y]
xi = [ reminder(Ni[i], y[i]) for i in range(0,len(y))]
print(Ni)
print(y)
print(xi)

total = [b[i]*Ni[i]*xi[i] for i in range(0,len(y))]
total = sum(total)
print(total)
x = total % t
print(vars())

