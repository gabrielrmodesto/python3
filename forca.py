import random

def boas_vindas():
	print("*********************************")
	print("***Bem vindo ao jogo da Forca!***")
	print("*********************************")

def ler_palavra_secreta():
	#leitura do arquivo
	arquivo = open("palavras.txt", "r")
	palavras = []
	for linha in arquivo:
		palavras.append((linha.strip()))

	arquivo.close()
	numero = random.randrange(0,len(palavras))
	palavra_secreta = palavras[numero].upper()

	return palavra_secreta

def inicializar_letras(palavra):
	return ["_" for letra in palavra]

def jogar():

	boas_vindas()
	palavra_secreta = ler_palavra_secreta()
	letras_acertadas = inicializar_letras(palavra_secreta)

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
