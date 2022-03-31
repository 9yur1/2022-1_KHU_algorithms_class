import random

#랜덤리스트 생성 함수 정의
def random_List(size):
    result = []

    for i in range(size):
        result.append(random.randint(0,1000))

    return result

cnt = 0

# 빠른정렬 프로그램
def quickSort(s, low, high):
    pivotpoint = -1
    if (high > low):
        pivotpoint = partition(s, low, high)
        quickSort(s, low, pivotpoint-1)
        quickSort(s, pivotpoint+1, high)

def partition(s, low, high):
    pivotitem = s[low]
    j = low
    global cnt
    for i in range(low+1, high+1):
        if(s[i]<pivotitem):
            j+=1
            cnt+=1
            s[i], s[j] = s[j], s[i]
           
    pivotpoint = j
    s[low], s[pivotpoint] = s[pivotpoint], s[low]
    return pivotpoint

s = [3,5,2,9,10,14,4,8]
quickSort(s,0,7)
print(s)

def avg_comparison(n):
    sum = 0
    for i in range(100):
        global cnt 
        cnt =0 
        data = random_List(n)      
        quickSort(data,0,n-1)
        sum += cnt 
    avg = sum/100
    return avg

# 큰 정수 곱셈 알고리즘
# threshold = 2
def prod2(a,b):
    threshold = 2
    n1 = len(str(a))
    n2 = len(str(b))
    if n1>n2:
        n = n1
    else:
        n = n2
    if (a==0 or b ==0):
        return 0
    elif n<threshold:
        return a*b
    else:
        m = int(n/2)
        x = int(a / (10**m))
        y = a% (10**m)
        w = int(b / (10**m))
        z = b % (10**m)
        print(x,y,w,z)
        r = prod2(x+y, w+z)
        p = prod2(x,w)
        q = prod2(y,z)
        return p*10**(2*m)+(r-p-q)*10**m + q

a=1234567812345678
b=2345678923456789

print(prod2(a,b))
print(a*b)