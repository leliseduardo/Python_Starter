# Locadora de carros

import os

inicio = ["Ver portfólio |", "Devolver carro |", "Sair"]
menuAluguel = ["Alugar carro |", "Voltar"]
carros = ["Celta 1.0 - 2014", "Uno 1.0 - 2016", "Gol 1.6 - 2020", "Kwid 1.4 - 2021", "Sandero 1.6 - 2019", "L200 2.4 - 2020"]
precos = [120.0, 100.0, 190.0, 170.0, 250.0, 500.0]
precosAlugados = []
alugados = []
confirmacao = ["Sim |", "Não"]
devolucao = ["Devolver carro |", "Voltar"]

def imprimeMenuInicial():
  print("\n### Bem vindo a LelisCar Aluguel de Carros ###\n")
  for i in range(3):
    print("({}) {} ".format(i+1, inicio[i]), end="")
  print("\n")

def imprimeMenuPortfolio():
  print("\nEscolha uma opção:")
  for i in range(2):
    print("({}) {}".format(i+1, menuAluguel[i]), end="")
  print("\n")

def imprimeConfirmacao():
  for i in range(2):
    print("({}) {}".format(i+1, confirmacao[i]), end="")
  print("\n")

def imprimePortfolio():
  print("\n")
  for i in range(len(carros)):
    print("{}: {} - R${}/dia".format(i+1, carros[i], precos[i]))

def imprimeAlugados():
  if(len(alugados) > 0):
    for i in range(len(alugados)):
      print("{} : {}".format(i+1, alugados[i]))
  else:
    print("Não há nenhum carro alugado")

def imprimeDevolucao():
  print("\nEscolha uma opção:")
  for i in range(2):
    print("({}) {}".format(i+1, devolucao[i]), end="")
  print("\n")

while True:
  imprimeMenuInicial()
  mi = int(input())

  if(mi == 1):
    imprimePortfolio()
    imprimeMenuPortfolio()
    ma = int(input())
    if(ma == 1):
      print("Digite o número do carro que deseja alugar")
      ca = int(input())
      print("Digite o número de dias que quer ficar com o carro: ")
      nd = int(input())
      vt = precos[ca-1] * nd
      print("O valor total será de {} para alugar o carro {} por {} dias.\nConfirma aluguel?".format(vt, carros[ca-1], nd))
      imprimeConfirmacao()
      c = int(input())
      if(c == 1):
        print("Carro alugado. Tecle enter para continuar.")
        e = input()
        alugados.append(carros[ca-1])
        carros.pop(ca-1)
        precosAlugados.append(precos[ca-1])
        precos.pop(ca-1)
        os.system("clear")
        continue
      elif(c == 2):
        print("Carro não alugado. Tecle enter para continuar")
        e = input()
        os.system("clear")
        continue
    elif(ma == 2):
      os.system("clear")
      continue
  elif(mi == 2):
    imprimeAlugados()
    imprimeDevolucao()
    dv = int(input())
    if(dv == 1):
      print("Digite o numero do carro que pretende devolver:")
      cd = int(input())
      print("Carro {} devolvido. Pressione enter para continuar".format(alugados[cd-1]))
      carros.append(alugados[cd-1])
      precos.append(precosAlugados[cd-1])
      precosAlugados.pop(cd-1)
      alugados.pop(cd-1)
      e = input()
      os.system("clear")
      continue
    elif(dv == 2):
      os.system("clear")
      continue
  elif(mi == 3):
    break
