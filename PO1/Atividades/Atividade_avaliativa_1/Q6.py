def calcular_lucro(preco_ingresso, custo_total, ingressos_iniciais, aumento_ingressos, reducao_preco):
    ingressos_vendidos = ingressos_iniciais + aumento_ingressos * ((5 - preco_ingresso) / reducao_preco)
    receita = preco_ingresso * ingressos_vendidos
    lucro = receita - custo_total
    return lucro, ingressos_vendidos

custo_total = 200.00
preco_inicial = 5.00
preco_final = 1.00
intervalo = 0.50
ingressos_iniciais = 120
aumento_ingressos = 26
reducao_preco = 0.50

melhor_lucro = float('-inf')
melhor_preco = 0
melhor_ingressos = 0

print(f"{'Preço do Ingresso':<20}{'Lucro':<20}{'Ingressos Vendidos':<20}")
for preco in [preco_inicial - i * intervalo for i in range(int((preco_inicial - preco_final) / intervalo) + 1)]:
    lucro, ingressos_vendidos = calcular_lucro(preco, custo_total, ingressos_iniciais, aumento_ingressos, reducao_preco)
    print(f"R$ {preco:<18.2f}R$ {lucro:<18.2f}{int(ingressos_vendidos):<20}")

    if lucro > melhor_lucro:
        melhor_lucro = lucro
        melhor_preco = preco
        melhor_ingressos = ingressos_vendidos

print("\nMelhor lucro esperado:")
print(f"Preço do Ingresso: R$ {melhor_preco:.2f}")
print(f"Lucro: R$ {melhor_lucro:.2f}")
print(f"Ingressos Vendidos: {int(melhor_ingressos)}")
