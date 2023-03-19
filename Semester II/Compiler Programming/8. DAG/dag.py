import re
grammer = ["D=B*C", "E=A+B", "B=B*C", "A=E-D"]
x=[]

opr = []
left =[]
right =[]
temp=[]
val =[]
tempNew=[]
valNew =[]

for i in grammer:
    a = i.split("=")
    val.append(a[0])
    temp.append(a[1])


loopTime = len(temp)
i = 0;
j = 0;
while i < loopTime:
    while j < loopTime:
        if i == j:
            j=j+1
        if temp[j] == temp[i]:
            x= val[i] + " " + val[j]
            val.pop(j)
            temp.pop(j)
            val[i] = x
            j+=1
        j+=1
    i+=1


count = 0
for i in temp:
    if len(i) == 3:
        re.split('[+-]{1}', i)
        opr.append(i[1])
        left.append(i[0])
        right.append(i[2])
        count += 1
        continue

    if len(i) == 2:
        i.split("+")
        opr.append(i[0])
        left.append("-")
        right.append(i[1])
        count += 1
        continue
    if len(i) == 1:
        x = val[count]
        x = x + " " + i
        for k in (0,len(val)-1):
            if val[k] == i:
                temp2 = k
                val[temp2] = x
        count += 1
        continue



print("VAl\tLeft\tOperator\tRight")
for i in range(0,count):
    print(f"{val[i]}\t{left[i]}\t{opr[i]}\t\t{right[i]}")
