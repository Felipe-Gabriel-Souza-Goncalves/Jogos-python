import random

def showTutorial():
  print('\n------------------TUTORIAL--------------------')
  print("O jogo deve ser jogado com ao menos 2 jogadores \n")
  print("A cada rodada cada jogador escolhe quantas vezes")
  print("quer jogar um dado de 6 lados e então a soma dos")
  print("resultados vai para sua pontuação.\n")
  print("ENTRETANTO, se qualquer um dos resultados for 1")
  print("toda a pontuação do jogador naquela rodada é zerada\n")
  print("O primeiro que chegar a 50 pontos ganha! boa sorte!")
  print('-----------------------------------------------\n')

def jogar():  

  while(True):
    try:
      nJogadores = int(input("Quantos jogadores terá?\n"))
      break
    except ValueError or TypeError:
      print("Somente números")

  jogando = True
  currentPlayer = 0
  pontuacoes = []

  for i in range(0, nJogadores):
    pontuacoes.append(0)

  while(jogando):
    resultados = []
    pontuacaoRodada = 0 

    print(f"Vez do jogador {(currentPlayer+1)}")

    while(True):
      try:
        vezesJogar = int(input("Quantas vezes quer jogar o dado? (max 10 vezes)"))
      except TypeError or ValueError:
        print("Digite somente números")

      if(vezesJogar <= 10):
        break

    for i in range(0, vezesJogar):
      valorDado = random.randint(1, 6)
      resultados.append(valorDado)

    print(resultados)

    for i in range(0, len(resultados)):
      if resultados[i] != 1:
        pontuacaoRodada += resultados[i]
      else:
        print("CAIU 1! perdeu os pontos")
        pontuacaoRodada = 0
        break
      
    print(f"{pontuacaoRodada} pontos ganhos nessa rodada!")
    pontuacoes[currentPlayer] += pontuacaoRodada

    if(pontuacoes[currentPlayer] >= 50):
      print(f"JOGADOR {currentPlayer+1} GANHOU COM {pontuacoes[currentPlayer]} PONTOS!!")

      jogando = False
      continue

    if(currentPlayer == (nJogadores - 1)):
      print("")
      print("Resultado da rodada:")
      for i in range(nJogadores):
        print(f"Jogador {i+1}: {pontuacoes[i]} pontos")
      print("------------------")

    currentPlayer = (currentPlayer+1) % nJogadores

while(True):
  print('1 - Jogar')
  print('2 - Tutorial')
  print('3 - Sair')

  while(True):
    try:
      escolha = int(input())
      break
    except ValueError or TypeError:
      print("Somente 1, 2 ou 3")

  match (escolha):
    case 1:
      jogar()
    case 2:
      showTutorial()
    case 3:
      break
    case _:
      print("Insira somente números de 1 a 3")
    
  