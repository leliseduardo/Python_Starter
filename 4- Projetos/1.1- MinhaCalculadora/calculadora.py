# Calculadora

import os

operacoes = ["Adição", "Subtração", "Multiplicação", "Divisão", "Exponenciação"]
simbolos = ["+", "-", "*", "/", "^"]

while True:
  for i in range(5):
    print("{} : {}".format(i+1, operacoes[i]))

  print("\nEscolha uma das operações:")
  o = int(input())
  print("Digite o primeiro número:")
  a = int(input())
  print("Digite o segundo número:")
  b = int(input())

  if(o-1 == 0):
    r = a + b
  elif(o-1 == 1):
    r = a - b
  elif(o-1 == 2):
    r = a * b
  elif(o-1 == 3):
    r = a / b
  elif(o-1 == 4):
    r = a ** b
  else:
    print("\n########## Operação inválida ##########")
    print("\n")
    print("\nDigite enter para reiniciar")
    os.system("clear")

  
  print("\nResultado:")
  print("{} {} {} = {}".format(a, simbolos[o-1], b, r))
  
  print("\nDigite enter para reiniciar")
  t = input()
  os.system("clear")
  