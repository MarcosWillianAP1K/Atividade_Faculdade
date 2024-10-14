
def printar_lista(lista):
    
    for i in lista:
        if type(i) == list:
            printar_lista(i)
        else:
            print(i, end=" ")
            

printar_lista([1,2,3,[4,5,6],[7,8,9,[10,11,12]]])