
try:

    f = float(input("Digite a temperatura em Fahrenheit: "))

    c = (5 *(f-32) / 9)
    
    print(f"A temperatura em Celsius é: {c:.2f}")

except:
    print("Vc não digitou um número")