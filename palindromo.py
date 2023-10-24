print("ingrese frase")
frase=input()
frase=frase.lower()
frase=frase.replace(" ","")
pali=frase[::-1]
palindromo=" es palíndromo"
if pali==frase:
    palindromo="sí"+palindromo
else:
    palindromo="no"+palindromo
print(palindromo)
