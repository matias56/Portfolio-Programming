def Sol():
    
    n, k = map(int, input().split())
    
    if k > n:
        print("YES")
    else:
        print("NO")


t = int(input())
while(t>0):
    t=t-1
    Sol()