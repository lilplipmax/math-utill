
def h1(list):
    sum = 0
    cnt = 0
    for i in range(0,len(list),2):
        if list[i] <= 0:
            sum += abs(list[i])
            cnt+=1
    if cnt == 0:
        return None
    srar = sum//cnt
    return srar

def h2(list):
    ost = []
    for i in range(len(list)):
        if abs(list[i]) <= 10:
            ost.append(list[i]%7)
    maximum = 0
    cnt = 0
    for j in range(len(ost)):
        if ost[j] > maximum:
            maximum = ost[j]
    return ost.count(maximum) 