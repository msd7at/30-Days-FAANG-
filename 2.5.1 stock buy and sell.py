#https://www.geeksforgeeks.org/stock-buy-sell/
def stockBuySell(price, n,tu): 

    if (n == 1): 
        return
 
    i = 0
    while (i < (n - 1)): 
        while ((i < (n - 1)) and 
                (price[i + 1] <= price[i])): 
            i += 1
        if (i == n - 1): 
            break
          
        buy = i 
        i += 1
          
        while ((i < n) and (price[i] >= price[i - 1])): 
            i += 1
              
        sell = i - 1
          
        tu.append((buy,sell))
t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    tu=[]
    stockBuySell(l, n,tu)
    if tu==[]:
        print("No Profit")
    else:
        print(*tu)
    
