"""
    Fazer uma calculadora em Python. Ela deverá ter 5 opções de operação,
    sendo adição, subtração, multiplicação, divisão e exponenciação.
"""

import os

operacoes = {
  "+": "Soma",
  "-": "Subtração",
  "*": "Multiplicação",
  "/": "Divisão",
  "^": "Exponenciação"
}

control = 1
resultado = 0
op = ""

while(control == 1):

  os.system("cls")
  print("")
  print("")

  i = 0
  print("Qual operação deseja realizar?")
  print("")
  for op, nome in operacoes.items():
    i += 1
    print("{}: {}".format(i, nome))
    
  operacao = int(input())

  print("Qual o primeiro valor?")
  n1 = float(input())
  print("Qual o segundo valor?")
  n2 = float(input())

  if(operacao == 1):
    op = "+"
    resultado = n1 + n2
  elif(operacao == 2):
    op = "-"
    resultado = n1 - n2
  elif(operacao == 3):
    op = "*"
    resultado = n1 * n2
  elif(operacao == 4):
    op = "/"
    resultado = float(n1 / n2)
  elif(operacao == 5):
    op = "^"
    resultado = n1 ** n2
  else:
    print("Operação inválida")

  print("")
  print("--------------------------------------------------")
  print("")
  print("Resultado:")
  print("")
  print("{} {} {} = {}".format(n1, op, n2, resultado))
  print("")
  print("--------------------------------------------------")

  print("Deseja fazer outra operação?")
  print("1: Sim")
  print("0: Sair")
  control = int(input())
  os.system("cls")
