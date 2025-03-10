
def adicionar_aluno(dicionario):
    
    while True:
        nome = input("Digite o nome do aluno: ")
        notas = []
        
        if nome not in dicionario.keys():
            break
        else:
            print("Aluno já cadastrado!")
        
    i = 0
    while i < 3:
        try:
            nota = float(input(f"Digite a {i+1}ª nota: "))
            notas.append(nota)
            i += 1
            
        except:
            print("Digite um número válido")
        
    return {nome: notas} 
    
   
def media(notas_alunos):
    return sum(notas_alunos)/len(notas_alunos)

def printar_media(Alunos):
    for i in Alunos:
        print(f"Aluno: {i}\nMedia: {media(Alunos[i]):.2f}\n")
    
    
Alunos = {}

for i in range(3):
    Alunos.update(adicionar_aluno(Alunos))
    
printar_media(Alunos)