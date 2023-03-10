a = float(input("Digite o Valor da Distância de A"))
b = float(input("Digite o Valor da Distância de B"))
c = float(input("Digite o Valor da Distância de C"))


pitagoras = (a*a) + (b*b)
resultado = c*2

if pitagoras == resultado:
    print('Esse Triângulo é Retângulo')
else:
    print('Esse Triângulo não é Retângulo')