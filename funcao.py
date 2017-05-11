import time
import getpass
import agContatos

nomeDono = "Rhuan"
senha = 12345

def menuPrincipal():
	print("\nSelecione uma das opções: \n")

	print(" (1)  Dados Pessoais")
	time.sleep(0.5)
	print(" (2)  Inserir novo contato")
	time.sleep(0.5)
	print(" (3)  Remover contato")
	time.sleep(0.5)
	print(" (4)  Atualizar contato")
	time.sleep(0.5)
	print(" (5)  Buscar contato")
	time.sleep(0.5)
	print(" (6)  Desligar agenda\n")
	time.sleep(0.5)

	opcao = input("Digite a opção desejada: ")

	if int(opcao) == 1:
		valida = testDados(nomeDono, senha)
		if valida == True:
			#puxando informações do dono da agenda
			print("\n (1) Nome do prorietário: " + nomeDono)
			email = agContatos.contatos[nomeDono]["Email"]
			print(" (2) Email: " + email)
			tel = agContatos.contatos[nomeDono]["Telefone"]
			print(" (3) Telefone: " + str(tel))
			endereco = agContatos.contatos[nomeDono]["Endereço"]
			print(" (4) Endereço: " + endereco)
			opcao2 = input("\nDeseja alterar os dados? Digite (s) para Sim e (n) para Não: ")
			if opcao2 == 's':
				atualizarContato(nome)
			else:
				menuPrincipal()

	if int(opcao) == 2:
		nome = input("Digite o nome do novo contato: ")
		novoContato(nome)
		resp = input("\n  Deseja voltar ao menu principal? Digite (s) para Sim e (n) para Não :\n")
		if resp == 's':
			menuPrincipal()
		else:
			print(" ** OBRIGADO POR UTILIZAR A AGENDA **")
			quit()

	if int(opcao) == 3:
		nome = input("Digite o contato que você deseja remover: ")
		removerContato(nome)
		resp = input("\n  Deseja voltar ao menu principal? Digite (s) para Sim e (n) para Não :\n")
		if resp == 's':
			menuPrincipal()
		else:
			print(" ** OBRIGADO POR UTILIZAR A AGENDA **")
			quit()

	if int(opcao) == 4:
		nome = input("\n  Digite o novo nome: ")
		atualizarContato(nome)
		resp = input("\n  Deseja voltar ao menu principal? Digite (s) para Sim e (n) para Não :\n")
		if resp == 's':
			menuPrincipal()
		else:
			print(" ** OBRIGADO POR UTILIZAR A AGENDA **")
			quit()

	if int(opcao) == 5:
		nome = input("Digite o nome que deseja buscar: ")
		testaContato(nome)
		resp = input("\n  Deseja voltar ao menu principal? Digite (s) para Sim e (n) para Não :\n")
		if resp == 's':
			menuPrincipal()
		else:
			print(" ** OBRIGADO POR UTILIZAR A AGENDA **")
			quit()

	if int(opcao) == 6:
		print(" ** OBRIGADO POR UTILIZAR A AGENDA **")
		quit()



def testDados(nomeDono, senha):
	confirmN = input("\nDigite o usuário: ")
	confirmS = getpass.getpass("Digite a senha: ")
	if nomeDono == confirmN:
		if int(senha) == int(confirmS):
			print("\nOlá, " + nomeDono)
			return True		
		else:
			print("Senha não confirma.")
			return False
	else:
		print("Usuario não cadastrado.")
		return False



def novoContato(newName):
	testaContato(newName)
	agContatos.contatos[newName] = {}
	newEmail = input("  Digite o novo Email: ")
	newTel = input("  Digite o novo numero de telefone: ")
	newEnder = input("  Digite o novo endereço: ")
	agContatos.contatos[newName] = {"Email": newEmail, "Telefone": newTel, "Endereço": newEnder}
	print("\n  Contato adicionado com sucesso!")
	resp = input("\n  Deseja voltar ao menu principal? Digite (s) para Sim e (n) para Não :\n")
	if resp == 's':
		menuPrincipal()
	else:
		print(" ** OBRIGADO POR UTILIZAR A AGENDA **")
		quit()
	#print(agContatos.contatos.keys())


def removerContato(nome):
	testaContato(nome)
	del agContatos.contatos[nome]
	print("\n  Contato removido com sucesso!")
	resp = input("\n  Deseja voltar ao menu principal? Digite (s) para Sim e (n) para Não : ")
	if resp == 's':
		menuPrincipal()
	else:
		print(" ** OBRIGADO POR UTILIZAR A AGENDA **")
		quit()



def atualizarContato(newName):
	testaContato(newName)
	agContatos.contatos[newName] = {}
	newEmail = input("  Digite o novo Email: ")
	newTel = input("  Digite o novo numero de telefone: ")
	newEnder = input("  Digite o novo endereço: ")
	agContatos.contatos[newName] = {"Email": newEmail, "Telefone": newTel, "Endereço": newEnder}
	print("\  Contato atualizado com sucesso!")
	resp = input("\n  Deseja voltar ao menu principal? Digite (s) para Sim e (n) para Não : ")
	if resp == 's':
		menuPrincipal()
	#print(agContatos.contatos.keys())

def testaContato(nomeContato):
	contato = agContatos.contatos.get(nomeContato, "Contato não existe")
	print(contato)
	if contato == "  **** Contato não existe ****":
		resp = input("\n  Deseja voltar ao menu principal? Digite (s) para Sim e (n) para Não : ")
		if resp == 's':
			menuPrincipal()
		else:
			print(" ** OBRIGADO POR UTILIZAR A AGENDA **")
			quit()

		


