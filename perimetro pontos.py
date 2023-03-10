X1 = float(input('Digite o Valor de x de A -> '))
Y1 = float(input('Digite o Valor de y de A -> '))
X2 = float(input('Digite o Valor de x de B -> '))-1
Y2 = float(input('Digite o Valor de y de B -> '))
X3 = float(input('Digite o Valor de x do C -> '))
Y3 = float(input('Digite o Valor de y do C -> '))

resultado2 = (((X2 - X1)**2) + ((Y2 - Y1)**2))**0.5
resultado3 = (((X3 - X2)**2) + ((Y3 - Y2)**2))**0.5
resultado4 = (((X3 - X1)**2) + ((Y3 - Y1)**2))**0.5

pitagoras = (resultado2*resultado2) + (resultado3*resultado3)
peri = resultado2 + resultado3 + resultado4

print()
print('======Distância de Pontos======')
print()
print('A Distância de A-B é ->',resultado2)
print('A Distância de B-C é ->',resultado3)
print('A Distância de C-A é ->',resultado4)
print()
print('O Permimetro é Igual a ->',peri)
