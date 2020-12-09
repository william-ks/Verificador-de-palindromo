#projeto verificador de palíndromo

frase = str(input('Insira uma frase: ')).strip().upper().split()
junto = ''.join(frase)
fraseInversa = ''

for letra in range(len(junto) - 1, -1, -1):
    fraseInversa = fraseInversa+junto[letra]

if(fraseInversa == junto):
    print("É um poliodromo")
else:
    print("Não é poliodromo")

