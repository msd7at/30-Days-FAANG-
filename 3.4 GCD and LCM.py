# link:-https://practice.geeksforgeeks.org/problems/lcm-and-gcd/0
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
t=int(input())
for q in range(t):
    a,b=map(int,input().split())
    s=a*b
    g=gcd(a,b)
    l=s//g
    print(l,g,sep=" ")
