
def campeao_media_tempo(tempos):
    media = []
    menor = 0
    primeiro = list(tempos.keys())[0]
    
    for i in tempos:
        media.append(sum(tempos[i])/len(tempos[i]))
        
        if min(media) < menor or i == primeiro:
            menor = min(media)
            campeao = i
        
    return campeao, media
        


tempos = {"Joao" : [1,2,3],
          "Maria" : [4,6,8],
          "Pedro" : [5, 5, 5],
          "Jose" : [7, 8, 9]
}

campeao, media = campeao_media_tempo(tempos)

print(campeao, media)