# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")
      
operacao = input ("Selecione o número da operação desejada:\n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n")

if operacao == '1':
      numero1 = input("Digite o primeiro número: ")
      numero2 = input("Digite o segundo número: ")
      resultadoSoma = float (numero1) + float(numero2)
      print(numero1, "+" ,numero2, "=" ,resultadoSoma)
      
elif operacao == '2':
      numero1 = input("Digite o primeiro número: ")
      numero2 = input("Digite o segundo número: ")
      resultadoSubtracao = float (numero1) - float(numero2)
      print(numero1, "-" ,numero2, "=" ,resultadoSubtracao)
      
elif operacao == '3':
      numero1 = input("Digite o primeiro número: ")
      numero2 = input("Digite o segundo número: ")
      resultadoMultiplicacao = float (numero1) * float(numero2)
      print(numero1, "*" ,numero2, "=" ,resultadoMultiplicacao)
      
elif operacao == '4':
      numero1 = input("Digite o primeiro número: ")
      numero2 = input("Digite o segundo número: ")
      resultadoDivisao = float (numero1) / float(numero2)
      print(numero1, "÷" ,numero2, "=" ,resultadoDivisao)
      
else: 
      print("Opção inválida")