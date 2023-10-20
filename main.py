# Aplicação desenvolvida por Daniel Camilo da Silva como formar de atividade prática
# da disciplina de Linguagem de Programação do curso Tecnólogo em DevOps
# da instituição de ensino Centro Universitário Anhanguera Pitágoras Ampli.

# Tabela de classificação do Índice de Massa Corpórea (IMC):
# 18.4 abaixo = Magreza
# 18.5 a 24.9 = Normal
# 25 a 29.9   = Sobrepeso
# 30 a 34.9   = Obesidade grau I
# 35 a 39.9   = Obesidade grau II
# 40 pra cima = Obesidade grau III

# Função que calcula o IMC:
def IMC(peso: float, altura: float) -> float:
    return round(peso / (altura ** 2), 1)

# Função que executa o IMC:
def calcular_imc():
  f_peso = float(input("Informe seu Peso: "))
  f_altura = float(input("Informe sua Altura: "))
  v_imc = IMC(f_peso, f_altura)

  print(f'------------------------------------')
  if v_imc < 18.4:
    print(f'Seu IMC é {v_imc}.\nSua classificação é: MAGREZA.')
  elif v_imc >= 18.5 and v_imc < 24.9:
    print(f'Seu IMC é {v_imc}.\nSua classificação é: NORMAL.')
  elif v_imc >= 25 and v_imc < 29.9:
    print(f'Seu IMC é {v_imc}.\nSua classificação é: SOBREPESO.')
  elif v_imc >= 30 and v_imc < 34.9:
    print(f'Seu IMC é {v_imc}.\nSua classificação é: OBESIDADE GRAU I.')
  elif v_imc >= 35 and v_imc < 39.9:
    print(f'Seu IMC é: {v_imc}.\nSua classificação é: OBESIDADE GRAU II.')
  elif v_imc > 40:
    print(f'Seu IMC é {v_imc}, sua classificação é OBESIDADE GRAU III.')
  print(f'------------------------------------\n')


# Menú:
while True:
    print("*** Menu de opções ***")
    print("1. IMC")
    print("2. Sair")

    # Obtém a escolha do usuário e aloca em uma variável:
    escolha = input("Escolha uma opção: ")

    # Checa a escolha do usuário:
    if escolha == '1':
        calcular_imc()

    elif escolha == '2':
        print("Saindo do programa. Tchau!!!\n")
        break  # Saia do loop while para encerrar o programa.
    else:
        print("Opção inválida. Tente novamente...\n")
