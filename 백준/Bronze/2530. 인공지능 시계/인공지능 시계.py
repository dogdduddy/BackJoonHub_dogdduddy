h, m, s = map(int,input().split())
t = int(input())

s += t%60
t -= t%60

m += s//60 + t//60
t -= 60*(t//60)
s = s%60

h += m//60 + t//(60*60)
m = m%60
h = h%24

print(h,m,s)
