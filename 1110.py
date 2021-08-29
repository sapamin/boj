num = str(input())

if int(num) < 10:
    firstnum = '0' + num
    firstnum=int(firstnum)
else:
    firstnum=int(num)

cycle = 0
result = -1

while (firstnum!=result):
    second = int(num) // 10
    first = int(num) % 10
    b =second+first
    bfirst = int(b) % 10
    result = str(first) + str(bfirst)
    num=result
    result=int(result)
    cycle+=1

print(cycle)
