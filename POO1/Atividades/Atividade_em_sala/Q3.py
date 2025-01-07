
class pais:
    
    def __init__(self, habitantes, taxa_de_crescimento):
        self.habitantes = habitantes
        self.taxa_de_crescimento = taxa_de_crescimento


def calcular_anos(X, Y):
    
    anos = 0
    
    if X.habitantes > Y.habitantes and X.taxa_de_crescimento > Y.taxa_de_crescimento :
        return "Y não alcançará X"
    
    if X.habitantes < Y.habitantes and X.taxa_de_crescimento < Y.taxa_de_crescimento:
        return "X não alcançará Y"
    
    if X.taxa_de_crescimento == Y.taxa_de_crescimento:
        return "X e Y crescerão na mesma taxa"
    
    
    while X.habitantes < Y.habitantes:
        X.habitantes += X.habitantes * (X.taxa_de_crescimento / 100)
        Y.habitantes += Y.habitantes * (Y.taxa_de_crescimento / 100)
        anos += 1
        
    return anos



pais1 = pais(1000, 3)

pais2 = pais(1500, 1.5)

print(calcular_anos(pais1, pais2))