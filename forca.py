import random

def boas_vindas():
	print("*********************************")
	print("***Bem vindo ao jogo da Forca!***")
	print("*********************************")

def ler_palavra_secreta():
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

def pede_chute():
	chute = input("Digite uma letra ")
	chute = chute.strip().upper()
	return chute

def chute_correto(chute,letras_acertadas,palavra_secreta):
	posicao = 0
	for letra in palavra_secreta:
		if(chute == letra):
			letras_acertadas[posicao] = letra
		posicao = posicao + 1

def mensagem_ganhador():
	print("Voce ganhou")
	print("             OOOOOOOOOOO               ")
	print("         OOOOOOOOOOOOOOOOOOO           ")
	print("      OOOOOO  OOOOOOOOO  OOOOOO        ")
	print("    OOOOOO      OOOOO      OOOOOO      ")
	print("  OOOOOOOO  #   OOOOO  #   OOOOOOOO    ")
	print(" OOOOOOOOOO    OOOOOOO    OOOOOOOOOO   ")
	print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  ")
	print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  ")
	print("OOOO  OOOOOOOOOOOOOOOOOOOOOOOOO  OOOO  ")
	print(" OOOO  OOOOOOOOOOOOOOOOOOOOOOO  OOOO   ")
	print("  OOOO   OOOOOOOOOOOOOOOOOOOO  OOOO    ")
	print("    OOOOO   OOOOOOOOOOOOOOO   OOOO     ")
	print("      OOOOOO   OOOOOOOOO   OOOOOO      ")
	print("         OOOOOO         OOOOOO         ")
	print("             OOOOOOOOOOOO              ")

def mensagem_perdedor():
	print("Voce perdeu")
	print("    _______________       ")
	print("   /               \      ")
	print("  /                 \     ")
	print("//                   \/\  ")
	print("\|   XXXX     XXXX   | /  ")
	print(" |   XXXX     XXXX   |/   ")
	print(" |   XXX       XXX   |    ")
	print(" |                   |    ")
	print(" \__      XXX      __/    ")
	print("   |\     XXX     /|      ")
	print("   | |           | |      ")
	print("   | I I I I I I I |      ")
	print("   |  I I I I I I  |      ")
	print("   \_             _/      ")
	print("     \_         _/        ")
	print("       \_______/          ")

def desenha_forca(erros):

	if(erros == 1):
		print("  _______      ")
		print(" |/      |     ")
		print(" |      (_)    ")
		print(" |             ")
		print(" |             ")
		print(" |             ")
		print(" |             ")
		print("_|___          ")
	if(erros == 2):
		print("  _______      ")
		print(" |/      |     ")
		print(" |      (_)    ")
		print(" |       |     ")
		print(" |       |     ")
		print(" |             ")
		print(" |             ")
		print("_|___          ")
	if(erros == 3):
		print("  _______      ")
		print(" |/      |     ")
		print(" |      (_)    ")
		print(" |      /|     ")
		print(" |       |     ")
		print(" |             ")
		print(" |             ")
		print("_|___          ")
	if(erros == 4):
		print("  _______      ")
		print(" |/      |     ")
		print(" |      (_)    ")
		print(" |      /|\    ")
		print(" |       |     ")
		print(" |             ")
		print(" |             ")
		print("_|___          ")
	if(erros == 5):
		print("  _______      ")
		print(" |/      |     ")
		print(" |      (_)    ")
		print(" |      /|\    ")
		print(" |       |     ")
		print(" |      /      ")
		print(" |             ")
		print("_|___          ")
	if(erros == 6):
		print("  _______      ")
		print(" |/      |     ")
		print(" |      (_)    ")
		print(" |      /|\    ")
		print(" |       |     ")
		print(" |      / \    ")
		print(" |             ")
		print("_|___          ")
		mensagem_perdedor()

def jogar():

	boas_vindas()
	palavra_secreta = ler_palavra_secreta()
	
	letras_acertadas = inicializar_letras(palavra_secreta)
	print(letras_acertadas)

	enforcou = False
	acertou = False
	erros = 0

	while(not enforcou and not acertou):
		
		chute = pede_chute()
		if(chute in palavra_secreta):
			chute_correto(chute,letras_acertadas,palavra_secreta)
		else:
			desenha_forca(erros)
			erros += 1

		enforcou = erros == 7
		acertou = "_" not in letras_acertadas
		print(letras_acertadas)

	if(acertou):
		mensagem_ganhador()
	else:
		mensagem_perdedor()

if(__name__ == "__main__"):
	jogar()