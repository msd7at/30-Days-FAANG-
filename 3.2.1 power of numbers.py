# link  https://www.geeksforgeeks.org/write-a-c-program-to-calculate-powxn/
def pow(x,y):
    if y==0:
        return 1
    temp=pow(x,y//2)
    if y%2==0:
        return (temp*temp)
    else:
        if y>0:
            return (temp*temp*x)
        else:
            return (temp*temp)/x
