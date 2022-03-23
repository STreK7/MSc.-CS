a = ["E=E+T","E=T","T=T*F","T=F","F=(E)","F=i"]
rules = {}
terms = []
for i in a:
    temp = i.split("=")

    terms.append(temp[0])
    try:
        rules[temp[0]] += [temp[1]]
    except:
         rules[temp[0]] = [temp[1]]
terms = list(set(terms))

    
#========================================================#
x = list(rules.values())
prod_rules = []
for i in x:
    for j in i:
        prod_rules.append(j)
opr = []
list_oprs = ["+","-","*","/","(",")","i"]
for i in prod_rules:
    for x in range(0,len(i)):
        if  i[x] in list_oprs:
            opr.append(i[x])

opm= []
for i in range(0,len(opr)+1):
    x = []
    for j in range(0,len(opr)+1):
        x.append("0")
    opm.append(x)

#========================================================#
def leading(gram, rules, term, start):
    s = []
    if gram[0] not in terms:
        return gram[0]
    elif len(gram) == 1:
        return [0]
    elif gram[1] not in terms and gram[-1] is not start:
        for i in rules[gram[-1]]:
            s+= leading(i, rules, gram[-1], start)
            s+= [gram[1]]
        return s


    
def trailing(gram, rules, term, start):
    s = []
    if gram[-1] not in terms:
        return gram[-1]
    elif len(gram) == 1:
        return [0]
    elif gram[-2] not in terms and gram[-1] is not start:
        for i in rules[gram[-1]]:
            s+= trailing(i, rules, gram[-1], start)
            s+= [gram[-2]]
    return s

leads = {}
trails = {}
for i in terms:
    s = [0]
    for j in rules[i]:
        s+=leading(j,rules,i,i)
    s = set(s)
    s.remove(0)
    leads[i] = s
    s = [0]
    for j in rules[i]:
        s+=trailing(j,rules,i,i)
    s = set(s)
    s.remove(0)
    trails[i] = s
    
for i in terms:
    print("LEADING("+i+"):",leads[i])
for i in terms:
    print("TRAILING("+i+"):",trails[i])


print("\nOperator Precedance Matrix")
opr = sorted(opr)

opm[0][0] = "`"

for i in range(1,len(opm)):
    opm[0][i] = opr[i-1]
    opm[i][0] = opr[i-1]

for i in a:
    temp = i.split("=")
    cur_prod = temp[1]
    for j in range (0,len(cur_prod)-1):
        if cur_prod[j] in opr and cur_prod[j+1] in opr:
            opm[opr.index(cur_prod[j]) +1][opr.index(cur_prod[j+1])+1] = "="
        if j < (len(cur_prod)-2):
            if cur_prod[j] in opr and cur_prod[j+2] in opr:
                if cur_prod[j+1] in terms:
                    opm[opr.index(cur_prod[j])+1][opr.index(cur_prod[j+2])+1] = "="
        if cur_prod[j] in opr and cur_prod[j+1] in terms:
            for k in leads[temp[0]]: 
                opm[opr.index(cur_prod[j])+1][opr.index(k)+1] = "<"
        if cur_prod[j] in terms and cur_prod[j+1] in opr:
            for k in trails[cur_prod[j]]:
                opm[opr.index(k)+1][opr.index(cur_prod[j+1])+1] = ">"

for i in opm:
    print ('  '.join(map(str, i)))
