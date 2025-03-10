
def tamString_(palavra):
    cont = 0
    
    while palavra != "":
        cont += 1
        palavra = palavra[1:]
    
    return cont
    
    
c = tamString_("bah")
print(c)