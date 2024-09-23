try:
    p1 = 0
    p2 = 1
    p3 = p1 + p2
    print(p1, end=" ")
    
    
    while p3 < 100:
        print(p3, end=" ")
        p1 = p2
        p2 = p3
        p3 = p1 + p2   
    
except:
    print("erro")