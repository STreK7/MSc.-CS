from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    #return the N = n1*n2*n3
    prod = reduce(lambda a, b: a*b, n)
    #zip give {n1:a1,n2:a2...}
    for ni, ai in zip(n, a):
        p = prod // ni
        #send 35, 3
        sum += ai * mul_inv(p, ni) * p
    return sum % prod
 

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    #if ni = 1
    if b == 1: return 1
    #else p > 1
    while a > 1:
        q = a // b      #35 // 3
        a, b = b, a%b   #a = 3, b = 2
        print(f"{q} {a} {b}")
        #x0 = 1- (11 *0), x1=1
        x0, x1 = x1 - q * x0, x0
        print(f"{x0} {x1} \n")
    if x1 < 0:
        x1 += b0
    return x1
 
 
 
if __name__ == '__main__':
    n = [3, 5, 7]
    a = [2, 3, 2]
    print(chinese_remainder(n, a))
