print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

total_tentativas = 3
rodada = 1

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
		print("Voce acertou")
		break
	else:
		print("Voce errou")
		if(maior):
			print("O numero secreto eh menor que seu chute")
		elif(menor):
			print("O numero secreto eh maior que seu chute")

#	rodada += 1