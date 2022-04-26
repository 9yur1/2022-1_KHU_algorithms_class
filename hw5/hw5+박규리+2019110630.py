#문제1
import utility

class Node:
    def __init__(self,data):
        self.l_child=None
        self.r_child=None
        self.data = data
def tree(key,r,i,j):
    k=r[i][j]
    if(k==0):
        return
    else:
        p=Node(key[k])
        p.l_child=tree(key,r,i,k-1)
        p.r_child=tree(key,r,k+1,j)
        return p


#data1
# key=[" ","A","B","C","D","E"]
# p=[1/15,2/15,3/15,4/15,5/15]

#data2
key=[" ","A","B","C","D","E","F","G","H"]
p=[1/8,1/8,1/8,1/8,1/8,1/8,1/8,1/8]
n=len(p)-1

a=[[0 for j in range(0,n+2)]for i in range(0,n+2)]
r=[[0 for j in range(0,n+2)]for i in range(0,n+2)]

for i in range (1,n+1):
    a[i][i-1]=0
    a[i][i]=p[i]
    r[i][i]=i
    r[i][i-1]=0
a[n+1][n]=0
r[n+1][n]=0

for dia in range(1,n):
    for i in range(1,n-dia+1):
        j=i+dia
        small=1000
        for k in range(i,j+1):
            psum=0
            for y in range(i,j+1):
                psum+=p[y]
            t=a[i][k-1]+a[k+1][j]+psum
            if(t<small):
                small = t
                a[i][j]=t
                r[i][j]=k

utility.printMatrixF(a)
print()
utility.printMatrix(r)

root=tree(key,r,1,n)
utility.print_inOrder(root)
print()
utility.print_preOrder(root)

# 문제2
import utility

a=['G','A','C','T','T','A','C','C']
b=['C','A','C','G','T','C','C','A','C','C']


m=len(a)
n=len(b)
table=[[0 for j in range(0,n+1)]for i in range(0,m+1)]
minindex = [[(0,0) for j in range(0,n+1)]for i in range(0,m+1)] 

for i in range(n-1,-1,-1):
    table[m][i] = table[m][i+1]+2

for i in range(m-1,-1,-1):
    table[i][n] = table[i+1][n]+2

for i in range(m-1,-1,-1):
    for j in range(n-1,-1,-1):
        penalty=0
        if a[i] != b[j]:
            penalty=1
        tmin = table[i+1][j+1]+penalty
        minindex[i][j] = (i+1,j+1)
        if tmin > table[i+1][j]+2:
            tmin = table[i+1][j]+2
            minindex[i][j] = (i+1,j)
        if tmin > table[i][j+1]+2:
            tmin = table[i][j+1]+2
            minindex[i][j] = (i,j+1)
        table[i][j] = tmin


utility.printMatrix(table)
x=0
y=0

while (x <m and y <n):
    tx, ty = x, y
    print(minindex[x][y])
    (x,y)= minindex[x][y]
    if x == tx + 1 and y == ty+1:
        print(a[tx]," ",  b[ty])
    elif x == tx and y == ty+1:
        print(" - ", " ", b[ty])
    else:
        print(a[tx], " " , " -")

print(minindex)
print("--------------------")
print(type(minindex[0][1]))