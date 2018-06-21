print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu chute: ")
print("Voce chutou ", chute_str)
chute = int(chute_str)
acertou =  chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
	print("Voce acertou")
else:
	print("Voce errou")
	if(maior):
		print("O numero secreto eh menor que seu chute")
	elif(menor):
		print("O numero secreto eh maior que seu chute")
