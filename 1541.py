n = list(input().split("-"))
sub = 0
num=[]
p=0
for i in n:
    x = i.split("+")
    for j in x:
        sub += int(j)
for k in n[:1]:
    y = k.split("+")
    for c in y:
        p+= int(c)
print(2 * p - sub)
