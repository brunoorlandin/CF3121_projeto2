import os
import math

def sep():
    print("\n=======================================\n")

def tresPolarizador ():
  teta = float(input("Digite o angulo (em graus) entre primeiro e o segundo polarizador:"))
  fi = float(input("Digite o angulo (em graus) entre segundo e o terceiro polarizador:"))
  tetaRad = math.radians(teta)
  tetaCosseno = math.cos(tetaRad)
  alfa = fi - teta
  alfaRad = math.radians(alfa)
  alfaCosseno = math.cos(alfaRad)
  if teta == 90 or teta == 270:
    tetaCosseno = 0
  if alfa == 90 or alfa == 270:
    alfaCosseno = 0
  while True:
    while True:
      if teta == 90 or teta == 270:
        print("Escolha qual sera a intensidade")
        print("[1] I0")
        print("[2] I1")
        print("I2 = 0 *pois o cosseno de 90 graus = 0")
        print("I3 = 0 *pois I2 = 0")
      elif alfa == 90 or alfa == 270:
        print("Escolha qual sera a intensidade")
        print("[1] I0")
        print("[2] I1")
        print("[3] I2")
        print("I3 = 0 *pois o cosseno de 90 graus = 0")
      else:
        print("Escolha qual sera a intensidade")
        print("[1] I0")
        print("[2] I1")
        print("[3] I2")
        print("[4] I3")

      op = int(input("Esolha: "))

      if op == 1:
        I0 = float(input("Digite o valor de I0 em w/m2: "))
        I1 = I0/2
        I2 = I1 * (math.pow(tetaCosseno,2))
        if alfaCosseno != 0:
          I3 = I2 * (math.pow(alfaCosseno,2))
        else:
          I3 = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        break
      elif op == 2:
        I1 = float(input("Digite o valor de I1 em w/m2: "))
        I0 = I1 * 2
        I2 = I1 * (math.pow(tetaCosseno,2))
        I3 = I2 * (math.pow(alfaCosseno,2))
        os.system('cls' if os.name == 'nt' else 'clear')
        break
      elif op == 3:
        I2 = float(input("Digite o valor de I2 em w/m2: "))
        if tetaCosseno == 0:
          I1 = 0
        else:
          I1 = I2 / (math.pow(tetaCosseno,2))
        I0 = I1 * 2
        I3 = I2 * (math.pow(alfaCosseno,2))
        os.system('cls' if os.name == 'nt' else 'clear')
        break
      elif op == 4:
        I3 = float(input("Digite o valor de I2 em w/m2: "))
        I2 = I3 / (math.pow(alfaCosseno,2))
        I1 = I2 / (math.pow(tetaCosseno,2))
        I0 = I1 * 2
        os.system('cls' if os.name == 'nt' else 'clear')
        break
      else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opcao invalida! Digite uma opcao valida.\n")
    
    print("I0 = %.2e w/m2" % I0)
    print("I1 = %.2e w/m2" % I1)
    print("I2 = %.2e w/m2" % I2)
    print("I3 = %.2e w/m2" % I3)
    break
         

def doisPolarizadores ():
  teta = float(input("Digite o angulo (em graus) entre primeiro e o segundo polarizador:"))
  tetaRad = math.radians(teta)
  cosseno = math.cos(tetaRad)
  if teta == 90 or teta == 270:
    cosseno = 0
  while True:
    if teta != 90 and teta != 270:
      print("Escolha qual sera a intensidade")
      print("[1] I0")
      print("[2] I1")
      print("[3] I2")
      op = int(input("Esolha: "))
    else:
      print("Escolha qual sera a intensidade")
      print("[1] I0")
      print("[2] I1")
      print("I2 = 0 *pois o cosseno de 90 graus = 0")
      op = int(input("Esolha: "))

    if op == 1:
      I0 = float(input("Digite o valor de I0 em w/m2: "))
      I1 = I0/2
      I2 = I1 * (math.pow(cosseno,2))
      os.system('cls' if os.name == 'nt' else 'clear')
      break
    elif op == 2:
      I1 = float(input("Digite o valor de I1 em w/m2: "))
      I0 = I1 * 2
      I2 = I1 * (math.pow(cosseno,2))
      os.system('cls' if os.name == 'nt' else 'clear')
      break
    elif op == 3:
      I2 = float(input("Digite o valor de I2 em w/m2: "))
      if cosseno == 0:
        I1 = 0
      else:
        I1 = I2 / (math.pow(cosseno,2))
      I0 = I1 * 2
      os.system('cls' if os.name == 'nt' else 'clear')
      break
    else:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Opcao invalida! Digite uma opcao valida.\n")
  
  print("I0 = %.2e w/m2" % I0)
  print("I1 = %.2e w/m2" % I1)
  print("I2 = %.2e w/m2" % I2)

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
      break
    elif op == 2:
      os.system('cls' if os.name == 'nt' else 'clear')
      I1 = float(input("Digite o valor de I1 em w/m2: "))
      I0 = I1 * 2
      break
    else:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Opcao invalida! Digite uma opcao valida.\n")
  
  print("I0 = %.2e w/m2" % I0)
  print("I1 = %.2e w/m2" % I1)


def main ():
    while True:
      print("Escolha a quantidade de polarizadores: ")
      print("[1] Um polarizador")
      print("[2] Dois polarizadores")
      print("[3] Tres polarizadores")
      print("[0] Sair")
      op = int(input("Escolha:"))

      if op == 1:
        umPolarizador()
      elif op == 2:
        doisPolarizadores()
      elif op == 3:
        tresPolarizador()
      elif op == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        break
      else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opcao invalida! Escolha uma das opcoes")
      sep() 

if __name__ == "__main__":
    main()