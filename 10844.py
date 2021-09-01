import sys
input=sys.stdin.readline

N=int(input())
stair=[]
stair.append(9)

if N==1:
    pass
else:
    for i in range(1,N):
        s=((2*stair[i-1])-i)
        stair.append(s)
print(stair[-1]%1000000000)

