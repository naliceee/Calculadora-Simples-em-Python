# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("\nSelecione o número da operação desejada:")

print("\n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")

operador = input("\nDigite sua opção (1/2/3/4): ")

num1 = input("\nDigite o primeiro número: ")

num2 = input("\nDigite o segundo número: ")

num3 = int(num1)
num4 = int(num2)

if operador == '1':
    res = num3 + num4
    print("\n\n %r + %r = %r"%(num3, num4, res))
    
elif operador == '2':
    res = num3 - num4
    print("\n\n %r - %r = %r" % (num3, num4, res))
    
elif operador == '3':
    res = num3 * num4
    print("\n\n %r * %r = %r" % (num3, num4, res))

elif operador == '4':
    res = num3 / num4
    print("\n\n %r / %r = %r" % (num3, num4, res))

else:
    print("\nOperação inválida!")

print("\nClique em run para começar novamente!")