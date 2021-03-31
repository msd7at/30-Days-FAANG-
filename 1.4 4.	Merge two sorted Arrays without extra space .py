x=list(map(int,input().split()))
y=list(map(int,input().split()))

def merge(x,y):
    m,n=len(x),len(y)
    for i in range(m):
        if x[i]>y[0]:
            x[i],y[0]=y[0],x[i]
            fi=y[0]
            k=1
            while k < n and y[k]<fi:
                y[k-1]=y[k]
                k+=1
            y[k-1]=fi
merge(x,y)
print(x,y)
