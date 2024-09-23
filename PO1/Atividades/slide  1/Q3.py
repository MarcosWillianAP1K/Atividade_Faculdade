

try:
    salario_h = float(input("Digite o valor do salario por hora: "))
    horas_trabalhadas = float(input("Digite o numero de horas trabalhadas: "))
    
    salario_bruto = salario_h * horas_trabalhadas
    IR = salario_bruto * 0.11
    INSS = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - IR - INSS - sindicato
    
    print(f"Salario Bruto: R${salario_bruto:.2f}\nIR: R${IR:.2f}\nINSS: R${INSS:.2f}\nSindicato: R${sindicato:.2f}\nSalario Liquido: R${salario_liquido:.2f}")
    
    
except:
    print("Vc não digitou um número")