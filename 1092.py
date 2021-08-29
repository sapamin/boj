import sys
import heapq
import math
input=sys.stdin.readline

krain=[]
box=[]
sortkrain=[]
sortbox=[]


k_N=int(input())
krain=list(map(int,input().split()))
for a in krain:
    heapq.heappush(sortkrain,a)

b_N=int(input())
box=list(map(int,input().split()))
for b in box:
    heapq.heappush(sortbox,b)

count=0
ans=0

while(len(sortbox)>1):
    for i in sortkrain:
        if i>sortbox[-1]:
            sortbox.pop()

        else:
            pass
        count+=1
ans=math.ceil(count/k_N)
print(ans)