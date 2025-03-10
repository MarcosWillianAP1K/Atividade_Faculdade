
#não foi especificado em adicionar os nome dos competidores
competidores = {
    "paulo": [],
    "joaquim": [],
    "kleiton": [],
    "bianca": [],
    "marcos": []
}


def adicionar_tempo(tempo_competidor: list[float]) -> None:
    i = 0
    while i < 3:
       try:
           tempo_competidor.append(float(input(f"Volta {i+1}: ")))  
           i += 1
            
       except:
           print("Tempo invalido")
    print()

def melhor_volta(competidores):
    
    for cont in range(3):
        melhor = next(iter(competidores))
        
        for i in competidores:
            if competidores[melhor][cont] > competidores[i][cont]:
                melhor = i
        
        print(f"O melhor tempo da volta {cont+1}: {melhor} com {competidores[melhor][cont]}")
        
def media_lista(lista):
    return sum(lista) / len(lista)
        
def melhor_competidor(competidores):
    
    melhor = next(iter(competidores))
    
    for i in competidores:
        if media_lista(competidores[melhor]) > media_lista(competidores[i]):
            melhor = i
    print(f"\nO melhor competidor é: {melhor} com {media_lista(competidores[melhor]):.2f} de media")
        
        

for i in competidores:
    print(f"Competidor: {i}")
    adicionar_tempo(competidores[i])

melhor_volta(competidores)
melhor_competidor(competidores)
