import os

peso1 = 18.5
peso2 = 25.0
peso3 = 30.0
peso4 = 35.0
peso5 = 40.0


control = 1
resultado = ""


while (control == 1):
  
  print("Digite sua altura: ")
  altura = float(input())
  print("Digite seu peso: ")
  peso = float(input())
  print("Digite seu sexo (F ou M):")
  sexo = input()

  imc = peso / (altura**2)

  if(sexo == "f" or sexo == "F"):
    peso1 = 17.5
    peso2 = 24.0
    peso3 = 29.0
    peso4 = 34.0
    peso5 = 39.0

  if(imc < peso1):
    resultado = "Abaixo do peso normal"
  elif(imc < peso2):
    resultado = "Peso normal"
  elif(imc < peso3):
    resultado = "Excesso de peso"
  elif(imc < peso4):
    resultado = "Obesidade classe 1"
  elif(imc < peso5):
    resultado = "Obesidade classe 2"
  else:
    resultado = "Obesidade classe 3"

  print("")
  print("Resultado: IMC = {}, {}".format(imc, resultado))
  print("")

  print("Recalcular?")
  control = int(input())