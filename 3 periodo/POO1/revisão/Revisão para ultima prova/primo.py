def achar_primo(num):
    for i in range(2, (num//2)+1):
        if num % i == 0:
            return False
    return  True

num = int(input("Digite um numero: "))
if achar_primo(num):
    print("Numero primo")
else:
    print("Numero não primo")