#coding: utf-8
import sqlite3 as sq
from pathlib import Path #Para verificar se arquivo existe a priori
import os
import sys
from datetime import datetime

#https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/

#Funcoes para criação do banco de dados. 
def CriaTabelaClientes(): 
	tabela = """
	create table if not exists Clientes(		
		CPF TEXT PRIMARY KEY,
		nome TEXT NOT NULL,
		senha TEXT NOT NULL,
		dataAbertura TEXT NOT NULL,
		saldo REAL, 
		extrato TEXT,
		movimentacoes TEXT, 
		ativo INTEGER		
		);
		"""
	return tabela	

def VerificaExistenciaBD(NomeBanco):
	Arquivos = os.listdir()	
	flag = False
	for arquivo in Arquivos: 
		if arquivo == NomeBanco: 
			flag = True
			break		
	if flag: 
		print(f"Banco de dados {NomeBanco} preexistente")
	else: 
		print(f"Banco de dados {NomeBanco} criado")	
	return flag		

def CriarBancoDados(NomeDB): 
	flag = VerificaExistenciaBD(NomeDB)	
	conexao = sq.connect(NomeDB)
	cursor = conexao.cursor()	
	tabela = CriaTabelaClientes()
	cursor.execute(tabela)
	conexao.commit()
	conexao.close()	


#Classe de controle do banco de cados
class BancoDadosCliente():
	def __init__(self, NomeBD): 
		self.NomeBD = NomeBD
		#Verificacao de existência do Banco de Dados. 
		path = Path(self.NomeBD)
		flagDB = False
		if not path.is_file():									
			flagDB = True		
		if(flagDB): 
			CriarBancoDados(NomeBD)
			'''
			print(f"Banco de dados {self.NomeBD} inexistente.")
			print("Banco de dados deve ser criado externamente")
			print("Programa abortado.") 
			sys.exit(1)
			'''
		self.conexao = sq.connect(self.NomeBD)
		self.cursor = self.conexao.cursor()
		print(f"Conexão do banco de dados {self.NomeBD} realizada.")
	
	def get_cursor_conexao(self): 
		return 	self.conexao, self.cursor
	
	def __del__(self): 
		print(f"{self.NomeBD} desconectado")
		self.conexao.close()	
	

	def InserirCliente(self, Cliente): 
		#Fazer verificacao de entrada. Retornar os valores de cpf e verificar se está no banco. 		
		if(not self.VerificarUsuarioNaBaseDados(Cliente.CPF)): #Usuario nao esta na base de dados
			#Faz verificacao se CPF do cliente já se encontra na base de dados. 			 
			self.cursor.execute("INSERT INTO Clientes VALUES (?,?,?,?,?,?,?, ?)",(Cliente.CPF, Cliente.nome, Cliente.senha, Cliente.dataAbertura, Cliente.saldo, Cliente.extrato, Cliente.movimentacoes, Cliente.ativo))
			self.conexao.commit()
			return True
		else: 
			print(f"Cliente {Cliente.CPF} já se encontra na base de dados.")	#Alterar no caso do tkinter. 
			return False

	def ConectarBD(self): 	#Cria banco de dados ou conecta bd existente. 
		self.conexao = sq.connect(self.NomeBD)	#Abrir conexao com BD
		self.cursor = self.conexao.cursor() #Criacao da conexao com BD
		print("Conexao iniciada com ", self.NomeBD)
	
	def VerificarUsuarioNaBaseDados(self, nome): 
		Consulta = '''SELECT CPF FROM Clientes WHERE CPF = ?'''
		self.cursor.execute(Consulta, (nome,))
		Verificacao = self.cursor.fetchone()
		if Verificacao == None: 
			return False	#Cliente não está na base de dados. 
		else: 
			return True		#Cliente está na base de dados. 

	def RetornarDadosBD(self): 
		self.cursor = self.conexao.cursor()
		SelecaoBD = """
			SELECT * FROM Clientes	
			"""
		self.cursor.execute(SelecaoBD)
		return self.cursor.fetchall()	
	
	def get_Cliente_Ativo(self): 
		self.cursor = self.conexao.cursor()
		SelecaoBD = """
			SELECT * FROM Clientes where ativo = 1 	
			"""
		self.cursor.execute(SelecaoBD)
		return self.cursor.fetchall()	
		
	def Deletar_Usuario(self, CPF):	
		self.cursor = self.conexao.cursor()
		self.saida = self.cursor.execute("DELETE FROM Clientes WHERE CPF = ?", (CPF,))
		self.conexao.commit()
		#print(self.saida)
		
	def Alterar_Senha_Cliente(self, CPF, senha_antiga, senha_nova): 
		if(self.VerificarUsuarioNaBaseDados(CPF)): 
			self.cursor =self.conexao.cursor()	
			ConsultaSenhaCliente = "SELECT senha FROM Clientes where CPF = ?"			
			self.cursor.execute(ConsultaSenhaCliente, ("0822",))	#Posiciona o cursor
			SenhaCliente =self.cursor.fetchall()		
			print("Senha na base: ", SenhaCliente[0][0])
			if senha_antiga == SenhaCliente[0][0]: 
				self.cursor.execute("UPDATE Clientes SET senha = ? WHERE CPF = ?",(senha_nova, CPF))
				self.conexao.commit()
				print("Senha alterada com sucesso")
			else: 
				print("Senha antiga nao confere. ")	
			return True
		else: 
			print(f"Cliente {Cliente.CPF} não se encontra na base de dados.")		
			return False

class DadosCliente: #Será passado para entrar com valores de Entry
	def __init__(self): 		
		'''
		self.nome = input("Entre com o nome do cliente: ")		
		self.CPF = input("Entre com o CPF do cliente: ")
		self.senha = input("Entre com a senha do cliente: ")
		self.dataAbertura = datetime.now()
		self.saldo = 0
		self.extrato = ''
		self.movimentacoes = ''
		'''
		
		#'''				
		self.nome = "Louis"
		self.CPF = "0822"
		self.senha = "abc"
		self.dataAbertura = datetime.now()
		self.saldo = 0.
		self.extrato = ''
		self.movimentacoes = ''
		#'''
		
		'''				
		self.nome = "Marcio"
		self.CPF = "0878"
		self.senha = "abc"
		self.dataAbertura = datetime.now()
		self.saldo = 0.
		self.extrato = ''
		self.movimentacoes = ''
		'''
		'''
		self.nome = "Mauro"
		self.CPF = "08778"
		self.senha = "abc"
		self.dataAbertura = datetime.now()
		self.saldo = 0.
		self.extrato = ''
		self.movimentacoes = ''
		'''
		


if __name__=="__main__":
	NomeDB = "BancoDadosUsuarioClientes.db"
	
	CriarBancoDados(NomeDB)
	
	BD1 = BancoDadosCliente(NomeDB)
	#Cliente01 = DadosCliente()
	#BD1.InserirCliente(Cliente01)
	print(BD1.RetornarDadosBD())
	'''
	BD1.Alterar_Senha_Cliente("0822", 'abc', 'pas')
	BD1.Alterar_Senha_Cliente("0822", 'pas', 'abd')
	BD1.Alterar_Senha_Cliente("0822", 'abd', 'kct')
	'''
	#print(BD1.RetornarDadosBD())
	
	
	



'''
Chatgpt: python3,  how to retrieve a single entry in a database using sqlite3 
'''

'''
import sqlite3

# Connect to the SQLite database (or create if it doesn't exist)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create a sample table (if it doesn't already exist)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")
conn.commit()

# Insert sample data (only if necessary)
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))
conn.commit()

# Retrieve a single entry by a specific condition (e.g., name = 'Alice')
cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
user = cursor.fetchone()

# Print result
if user:
    print("User found:", user)  # Output: (1, 'Alice', 25)
else:
    print("User not found")

# Close connection
conn.close()

'''
