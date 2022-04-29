def dac(a,b):
    global c
    if b == 1:
        return a%c
    else:
        temp = dac(a,b//2)
        if b%2 == 0:
            return temp*temp % c
        else :
            return temp*temp*a % c

a, b, c = map(int,input().split())
print(dac(a,b))
