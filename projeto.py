import os
import math

def sep():
    print("\n===========================================\n")

def doisPolarizadores ():
  teta = float(input("Digite o angulo (em graus) entre segundo e o primeiro polarizador:"))
  tetaRad = math.radians(teta)
  while True:
    print("Escolha qual sera a intensidade")
    print("[1] I0")
    print("[2] I1")
    print("[3] I0")
    op = int(input("Esolha: "))

    if op == 1:
      I0 = float(input("Digite o valor de I0 em w/m2: "))
      I1 = I0/2
      I2 = I1 * (math.pow(math.cos(tetaRad),2))
      os.system('cls' if os.name == 'nt' else 'clear')
      break
    elif op == 2:
      I1 = float(input("Digite o valor de I1 em w/m2: "))
      I0 = I1 * 2
      I2 = I1 * (math.pow(math.cos(tetaRad),2))
      os.system('cls' if os.name == 'nt' else 'clear')
      break
    elif op == 3:
      I2 = float(input("Digite o valor de I2 em w/m2: "))
      I0 = I1 * 2
      I1 = I2 / (math.pow(math.cos(tetaRad),2))
      os.system('cls' if os.name == 'nt' else 'clear')
      break
    else:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Opcao invalida! Digite uma opcao valida.\n")
  
  print("I0 = %.2e w/m2" % I0)
  print("I1 = %.2e w/m2" % I1)
  print("I1 = %.2e w/m2" % I2)

def umPolarizador ():
  while True:
    print("Escolha a entrada:")
    print("[1] I0")
    print("[2] I1")
    op = int(input("Escolha: "))

    if op == 1:
      I0 = float(input("Digite o valor de I0 em w/m2: "))
      I1 = I0/2
      os.system('cls' if os.name == 'nt' else 'clear')
      print("I0 = %.2e w/m2" % I0)
      print("I1 = %.2e w/m2" % I1)
      break
    elif op == 2:
      os.system('cls' if os.name == 'nt' else 'clear')
      I1 = float(input("Digite o valor de I1 em w/m2: "))
      I0 = I1 * 2
      print("I0 = %.2e w/m2" % I0)
      print("I1 = %.2e w/m2" % I1)
      break
    else:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Opcao invalida! Digite uma opcao valida.\n")


def main ():
    while True:
      print("Escolha a quantidade de polarizadores: ")
      print("[1] Um polarizador")
      print("[2] Dois polarizadores")
      print("[0] Sair")
      op = int(input("Escolha:"))

      if op == 1:
        umPolarizador()
      elif op == 2:
        doisPolarizadores()
      elif op == 0:
        break
      else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opcao invalida! Escolha uma das opcoes")
      sep() 

if __name__ == "__main__":
    main()