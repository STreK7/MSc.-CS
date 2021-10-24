def reminder(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b      #35 // 3
        a, b = b, a%b   #a = 3, b = 2
        #x0 = 1- (11 *0), x1=1
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1



if __name__ == '__main__':
    from functools import reduce
    
    a = [2, 3, 2]
    #a(mod n)
    n = [3, 5, 7]

        
    #return the N = n1*n2*n3
    t = reduce(lambda a, b: a*b, n)
    Ni = [ t//i for i in n]
    xi = [ reminder(Ni[i], n[i]) for i in range(0,len(a))]

    total = [a[i]*Ni[i]*xi[i] for i in range(0,len(a))]
    total = sum(total)
    x = total % t
    print(x)

