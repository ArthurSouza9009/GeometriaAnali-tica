Xa = float(input("insira o Valor de xa -> "))
print()
Ya = float(input("insira o Valor de ya -> "))
print()
Xb = float(input("insira o Valor de xb -> "))
print()
Yb = float(input("insira o Valor de yb -> "))
print()
Xc = float(input("insira o Valor de xc -> "))
print()
Yc = float(input("insira o Valor de yc -> "))
n1 = 1*Yb*Xc
n2 = Xa*1*Yc
n3 = Ya*Xb*1
p1 = Xa*Yb*1
p2 = Ya*1*Xc
p3 = 1*Xb*Yc

print('======Colinear======')
print()
print ("Positivos -> ",p1,p2,p3)
print()
print ("Negativos -> ",n1,n2,n3)
print()
resultado = (p1+p2+p3)-(n1+n2+n3)
if resultado != 0:
    print ('Não é Colinear -> ',resultado)
else:
    print ('É Colinear, O Resultado foi -> ',resultado)


"""
xa e ya 2 primeiros digitos da 1 fileira de cima
xb e yb 2 primeiros digitos da 2 fileira de cima
#xc e yc 2 primeiros digitos da 3 fileira de cima

EXEMPLO

#   | xa ya 1 |
#   | xb yb 1 | = 0
#   | xc yc 1 |

"""