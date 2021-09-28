def LCSLength(X, Y, m, n):
 
    # return if the end of either sequence is reached
    if m == 0 or n == 0:
        return 0
 
    # if the last character of `X` and `Y` matches
    if X[m - 1] == Y[n - 1]:
        return LCSLength(X, Y, m - 1, n - 1) + 1
 
    # otherwise, if the last character of `X` and `Y` don't match
    return max(LCSLength(X, Y, m, n - 1), LCSLength(X, Y, m - 1, n))
 
 
if __name__ == '__main__':
 
    X = input("Input String 1 \n").upper()
    Y = input("Input String 2 \n").upper()
 
    print('The length of the LCS is', LCSLength(X, Y, len(X), len(Y)))
 
