import math
def warshall(a):
    assert (len(row) == len(a) for row in a)
    n = len(a)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j] = a[i][j] or (a[i][k] and a[k][j])
    return a

grammer = [["Z","bMb"],["M","(L"],['M',"a"],["L","Ma)"]]

lhs = [i[0] for i in grammer]
rhs = [i[1] for i in grammer]

#--------------------------------#
##symbol = lhs + rhs
##symbols = []
##for i in symbol:
##    for x in range(0,len(i)):
##        if  i[x] not in symbols:
##            symbols.append(i[x])

symbols = ["Z","M","L","a","b","(",")"]
#--------------------------------#

#making empty matrix
firstMatrix = []
firstStar = []
I = []

for i in range(0,len(symbols)):
    x = []
    for i in range(0,len(symbols)):
        x.append(0)
    firstMatrix.append(x)
    firstStar.append(x)

#making identity matrix
identityX=0
for i in range(0,len(symbols)):
    x = []
    for j in range(0,len(symbols)):
        if j == identityX:
            x.append(1)
        else:
            x.append(0)
    identityX += 1  
    I.append(x)
#making empty matrix -end


#first matrix
i = 0    
for j in range(0, len(I)):
        I[i][j] = 1
        i = i+1
        
for i in range(0,len(lhs)):
    left = lhs[i]
    right = rhs[i]
    #first
    right = right[0]
    for i in range(0,len(symbols)):
        if symbols[i] == left:
            findL = i
            break
    for i in range(0,len(symbols)):
        if symbols[i] == right:
            findR = i
            break
    firstMatrix[findL][findR] = 1
#first matrix end

#first+ = warshal(first)
firstPlus = warshall(firstMatrix)


#--------------------------------------------------------------#

#last matrix
lastMatrix = []
lastPlus = []

for i in range(0,len(symbols)):
    x = []
    for i in range(0,len(symbols)):
        x.append(0)
    lastMatrix.append(x)
    lastPlus.append(x)

    
for i in range(0,len(rhs)):
    left = lhs[i]
    right = rhs[i]
    right = right[-1]
    for i in range(0,len(symbols)):
        if symbols[i] == left:
            findL = i
            break
    for i in range(0,len(symbols)):
        if symbols[i] == right:
            findR = i
            break
    lastMatrix[findL][findR] = 1


#last+ = warshal(last)
lastPlus = warshall(lastMatrix)


#last+ transpose
lastPlusT = []
for i in range(0,len(symbols)):
    x = []
    for i in range(0,len(symbols)):
        x.append(0)
    lastPlusT.append(x)

for i in range(len(lastPlus)):
   # iterate through columns
   for j in range(len(lastPlus[0])):
       lastPlusT[j][i] = lastPlus[i][j]


#-----------------------------------------------------------------#

#bug equal matrix inherits values from previos matrix if not created
equal =[]
for i in range(0,len(symbols)):
    x = []
    for i in range(0,len(symbols)):
        x.append(0)
    equal.append(x)
    
#eq matrix
#equal = resultant matrix
print("")
eqSet=[]
for i in rhs:
    if len(i) > 1:
        items = math.ceil(len(i)/2)
        x = 0
        y = 1
        for j in range(0,items):
            temp = i[x] + i [y]
            eqSet.append(temp)
            x += 1
            y += 1

for i in eqSet:
    left = i[0]
    right = i[1]
    #print(f"left = {left}  right={right}")
    for j in range(0,len(symbols)):
        if symbols[j] == left:
            findL = j
            break

    for j in range(0,len(symbols)):
        if symbols[j] == right:
            findR = j
            break
    equal[findL][findR] = 1



#------------------------------------------------------------------#
#less then
# = eq * first+
# lessThen resultant matrix

lessThen = []
for i in range(0,len(symbols)):
    x = []
    for i in range(0,len(symbols)):
        x.append(0)
    lessThen.append(x)

for i in range(len(equal)):
    for j in range(len(firstPlus[0])):
        for k in range(len(firstPlus)):
            lessThen[i][j] += equal[i][k] * firstPlus[k][j]
            


#---------------------------------------------------------#

#first* = first+ * Identity
for i in range(0,len(firstPlus)):    
    for j in range(0,len(firstPlus[0])):
        #print(f"i={i}  j={j}")
        firstStar[i][j] = firstPlus[i][j] or  I[i][j]        

#--------------------------------------------------------#

#Greater then
# = last+T * eq * first*
# greaterThen resultant matrix

greaterThen = []
for i in range(0,len(symbols)):
    x = []
    for i in range(0,len(symbols)):
        x.append(0)
    greaterThen.append(x)

eqSfp = []
for i in range(0,len(symbols)):
    x = []
    for i in range(0,len(symbols)):
        x.append(0)
    eqSfp.append(x)


for i in range(len(equal)):
    for j in range(len(firstStar[0])):
         for k in range(len(firstStar)):
            eqSfp[i][j] += equal[i][k] * firstStar[k][j]
            
for i in range(len(lastPlusT)):
    for j in range(len(eqSfp[0])):
         for k in range(len(eqSfp)):
            greaterThen[i][j] += lastPlusT[i][k] * eqSfp[k][j]
            
#greaterThen = np.dot(lastPlusT , np.dot(equal,firstPlus))


#--------------------------------------#

spm = []
for i in range(0,len(symbols)+1):
    x = []
    for i in range(0,len(symbols)+1):
        x.append(0)
    spm.append(x)
spm[0][0] = "`"

for i in range(1,len(spm)):
    spm[0][i] = symbols[i-1]
    spm[i][0] = symbols[i-1]

for i in range(1, len(lessThen)+1):
    for j in range(1, len(lessThen)+1):
        if(equal[i-1][j-1]==1):
            spm[i][j] = "="
        elif(lessThen[i-1][j-1]==1):
            spm[i][j] = "<"
        elif(greaterThen[i-1][j-1]==1):
            spm[i][j] = ">"

for i in spm:
    print ('  '.join(map(str, i)))
