import sys
input=sys.stdin.readline

gap=[]
num=0
j=0
n, l = map(int, input().split())
location=list(map(int,input().split()))
l-=1
le=l

for i in range(n-1):
    gap.append((location[i+1]-location[i]-1))

while j<n-1:
    if (l==le)and(l>gap[j]):
        le-=gap[j]+1
        j+=1

    elif (l!=le)and(le>gap[j]):
        le-= gap[j]+1
        j+=1
    else:
        num+=1
        le = l
        j+=1
num+=1
print(num)
