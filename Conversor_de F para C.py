
#Sistema para converter Graus Centigrados para Fahrenheit
#Sistema para converter Graus Fahrenheit  para Centigrados

# Converter
# Valor em Centigrados para Fahrenheit
C1 = float(input("Digite a temperatura em graus Centigrados:"))
print(f"Valor em Centigrados é:{C1}")

# Valor em Centigrados para Fahrenheit
F1 = float(C1*1.8 + 32)
print(f"Valor de {C1} em Fahrenheit e:{F1}")


# Converter
# Valor em Fahrenheit para Centigrados 
F2 = float(input("Digite a temperatura em graus Fahrenheit :"))
print(f"Valor em Fahrenheit é:{F2}")

# Valor em Centigrados para Fahrenheit
C2 = float((F2-32)/1.8)
print(f"Valor de {F2}em Centigrados e:{C2}")