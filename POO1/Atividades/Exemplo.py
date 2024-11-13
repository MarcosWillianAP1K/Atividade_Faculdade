

i = 0

while i <= 40:
    
    # if i == 0:
    #     print("PIN")
    if i % 4 == 0 or i % 10 == 0:
        
        if i == 40:
            print("FIM")
        else:
            print("PIN")
    else:
        print(i)
    
    i += 1
    
print("\n")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in lista:
    if i % 2 == 0:
        print(i)