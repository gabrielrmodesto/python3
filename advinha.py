print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu chute: ")
print("Voce chutou ", chute_str)
chute = int(chute_str)

if(chute == numero_secreto):
	print("Voce acertou")
else:
	print("Voce errou")
