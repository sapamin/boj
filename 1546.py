n=int(input())
score=[]
score=list(map(int,input().split()))
score.sort()
score.reverse()
i=0
max=score[0]

while i<n:
 score[i]=(score[i]/max)*100
 i+=1

avg=(sum(score)/n)
print(avg)