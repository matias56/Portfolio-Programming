t = int(input())
for i in range(t):
    (x1,y1,x2,y2)=map(int,input().split(" "))
    
    
    if (x1+y1)<(x2+y2):
        print("Chef will choose style 1")
        
    else:
        print("Chef will choose style 2")