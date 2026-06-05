op = ""

while op != "0":
  while True:
    try:
      num1 = int(input("Insira o primeiro valor: "))
      num2 = int(input("Insira o segundo valor: "))
      break
    except ValueError:
      print("Ops! Valor inválido. Digite um número.")


  print("Escolha a operação desejada: \n1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n0 - para terminar o programa")
  op = input()

  if op == "1":
    print("O resultado da adição é", num1 + num2)
  elif op == "2":
    print("O resultado da subtração é", num1 - num2)
  elif op == "3":
    print("O resultado da multiplicação é", num1 * num2)
  elif op == "4":
    # Corrige a divisão por zero
    if num2 != 0:
      print("O resultado da divisão é", num1 / num2)
    else:
      print("Erro: Divisão por zero não é permitida.")
  elif op == "0":
    print("O programa foi finalizado.")
  else:
    print("Operação inválida. Por favor, escolha uma opção válida.")