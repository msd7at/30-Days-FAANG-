x=float(input())
n=int(input())
if (x >= 0 and x <= 1): 
    low = x 
    high = 1
else:
    low=1
    high=x
guess=(high+low)/2
epsilon = 0.000000000001
print(guess)
while guess**n-x >=epsilon:
    if guess**n >x:
        high=guess
    else:
        low=guess
    guess=(high+low)/2
    print(guess)
print(guess)
    
