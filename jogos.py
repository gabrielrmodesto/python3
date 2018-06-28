import forca
import advinha

def escolhe_jogo():
	print("*********************************")
	print("********Escolha o seu jogo*******")
	print("*********************************")
	print("(1) Advinha - (2) Forca")

	escolha = int(input("Qual o seu jogo?"))

	if(escolha == 1):
		advinha.jogar()
	elif(escolha == 2):
		forca.jogar()
if(__name__ == "__main__"):
	escolhe_jogo()