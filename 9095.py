import sys
input=sys.stdin.readline

def factorial(n):
    return n * factorial(n-1) if n > 1 else 1


T=int(input())
count=0

while count<T:
    case=1 #1의 합으로 num 표현
    num=int(input())
    two=num//2 #2의 최대갯수
    three=num//3 #3의 최대갯수
    for i in range(two):
        case+=factorial(num-i)/(factorial(i)*factorial(num-2*i)) #1,2의 조합
    for j in range(three):


def fac(n)
    if n>4:

    elif n>3:

    elif n>2:
        return 4
    elif n>1:
        return 2
    else:
        return 1





    count+=1

