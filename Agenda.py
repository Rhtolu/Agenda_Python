#### Agenda Python - Rhuan Faria ID 1600902 e Ricardo Pierre ID 160187  ####
################# 2°ADS-C NOTURNO ####################


#importando classes de tempo e funcoes
import time
import funcao
import agContatos


#criação de uma agenda com alguns contatos

#solicitação do dono
nomeDono = "Rhuan"
#input("\nDigite o nome do dono: ")
senha = 12345
#int(input("\nDigite o numero da senha: "))
print("\n  /**********************************************************************/")
print("  /                        BEM VINDO A AGENDA                            /")
print("  /**********************************************************************/")	

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
	valida = funcao.testDados(nomeDono, senha)
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
			funcao.atualizarContato(nomeDono)
		else:
			funcao.menuPrincipal()

if int(opcao) == 2:
	nome = input("  Digite o nome do novo contato: ")
	funcao.novoContato(nome)
	resp = input("\n  Deseja voltar ao menu principal? Digite (s) para Sim e (n) para Não : ")
	if resp == 's':
		funcao.menuPrincipal()
	else:
		print(" ** OBRIGADO POR UTILIZAR A AGENDA **")
		quit()

if int(opcao) == 3:
	nome = input("  Digite o contato que você deseja remover: ")
	funcao.removerContato(nome)

if int(opcao) == 4:
	nome = input("\n  Digite o novo nome: ")
	funcao.atualizarContato(nome)

if int(opcao) == 5:
	nome = input("  Digite o nome que deseja buscar: ")
	funcao.testaContato(nome)
	resp = input("\n  Deseja voltar ao menu principal? Digite (s) para Sim e (n) para Não : ")
	if resp == 's':
		funcao.menuPrincipal()
	else:
		print(" ** OBRIGADO POR UTILIZAR A AGENDA **")
		quit()

if int(opcao) == 6:
	print(" ** OBRIGADO POR UTILIZAR A AGENDA **")
	quit()
