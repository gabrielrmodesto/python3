def jogar():
	print("*********************************")
	print("Bem vindo ao jogo da Forca!")
	print("*********************************")

	palavra_secreta = "banana".upper()
	letras_acertadas = ["_" for letra in palavra_secreta]

	enforcou = False
	acertou = False
	erros = 0

	print(letras_acertadas)
	while(not enforcou and not acertou):
		chute = input("Digite uma letra ")
		chute = chute.strip().upper()

		if(chute in palavra_secreta):
			posicao = 0
			for letra in palavra_secreta:
				if(chute == letra):
					letras_acertadas[posicao] = letra
				posicao = posicao + 1
		else:
			erros += 1

		enforcou = erros == 6
		acertou = "_" not in letras_acertadas
		print(letras_acertadas)

	if(acertou):
		print("Voce ganhou")
	else:
		print("Voce errou")
	print("Fim de jogo")

if(__name__ == "__main__"):
	jogar()
