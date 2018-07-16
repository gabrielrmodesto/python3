def jogar():
	print("*********************************")
	print("Bem vindo ao jogo da Forca!")
	print("*********************************")

	palavra_secreta = "banana"

	enforcou = False
	acertou = False

	while(not enforcou and not acertou):
		chute = input("Digite uma letra ")
		chute = chute.strip()

		posicao = 0
		for letra in palavra_secreta:
			if(chute.upper() == letra.upper()): 
				print("A letra {} foi encontrada na posicao {} ".format(letra,posicao))
			posicao = posicao + 1


	print("Fim de jogo")

if(__name__ == "__main__"):
	jogar()