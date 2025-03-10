def converter_binario_antes(n):
    
    if n > 0:
        binario = ""
        while n >= 1:
        
            if int(n % 2) == 0:
                binario = "0"   + binario
            else:
                binario = "1" + binario
        
            n /= 2
        
        return int(binario)
    
    return 0


n = int(input())

print(converter_binario_antes(n))

