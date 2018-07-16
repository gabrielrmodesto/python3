import random

def jogar():
	print("*********************************")
	print("Bem vindo ao jogo de Adivinhação!")
	print("*********************************")

	numero_secreto = random.randrange(1,101)	
	total_tentativas = 0

	rodada = 1
	pontos = 1000
	print("Qual o nivel de dificuldade? ")
	print("(1) Facil - (2) Medio - (3) Dificil")
	nivel = int(input("Qual o nivel? "))

	if(nivel == 1):
		total_tentativas = 20
	elif(nivel == 2):
		total_tentativas = 10
	elif(nivel == 3):
		total_tentativas = 5
	else:
		print("Esse nao eh um nivel aceitavel")

	#while (rodada <= total_tentativas):
	for rodada in range(1,total_tentativas+1):
		print("Tentativa: {} de {} ".format(rodada,total_tentativas))
		chute_str = input("Digite um numero entre 1 e 100: ")
		print("Voce chutou ", chute_str)
		chute = int(chute_str)
		acertou =  chute == numero_secreto
		maior = chute > numero_secreto
		menor = chute < numero_secreto

		if(chute < 1 or chute > 100):
			print("Por favor digite um numero entre 1 e 100")
			continue

		if(acertou):
			print("Voce acertou e fez {} pontos".format(pontos))
			break
		else:
			print("Voce errou")
			if(maior):
				print("O numero secreto eh menor que seu chute")
			elif(menor):
				print("O numero secreto eh maior que seu chute")
			pontos_perdidos = abs(numero_secreto - chute)
			pontos = pontos - pontos_perdidos
			
if (__name__ == "__main__"):
	jogar()