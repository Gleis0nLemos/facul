# Exercício 02-Me

# Implementar uma solução em Python que faça o tratamento de exceção de divisão por Zero.

def divisao():         
  
  while True:

    try: 
      # código que pode gerar uma exceção
      a = int(input("Digite o dividendo: "))
      b = int(input("Agora digite o dividor: "))

      # se o "b" for diferente de zero, este loop é encerrado
      if b != 0:
        break # sair do loop se a entrada for válida
      print("Divisão inválida")

    except ValueError:
        # lidar com a exceção de valor inválido, caso o valor de "a" e "b" não for um int
        print("Entrar com um número válido!")

  resultado = a/b
  return resultado

# continuar a execução do programa após a entrada ser válida
x = divisao()
print("Resultado:", x)