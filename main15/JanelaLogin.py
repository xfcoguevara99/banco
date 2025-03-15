#coding: utf-8

from classCliente import *
#import BancoDadosCliente as BDC
import tkinter as tk
from PIL import ImageTk, Image


#Pagina de login
class JanelaLogin(): 
	def PaginaLogin(self): 
		self.Apaga_frame(self.FramePrincipal)
		self.CriaJanelaBase() 
		self.title("Acesse sua conta")
		self.ConfigurarPaginaLogin()
		self.CriarPaginaLogin()
		self.InsereLabelEsquerdaSaudacao()
		self.ConfigurarPagLoginFrameUsuarioSenha()
		self.InserePagLoginFrameUsuarioSenha()
		self.InsereBotaoAcessarContaLogin()
		self.PagLoginBotaoRetornar()
		self.Usuario = Cliente() #Cliente a verificar
		self.InsereImagemLogin()
		self.InsereBannerLogin()

	def ConfigurarPaginaLogin(self): 	
		#Colocar duas linhas no inicio
		self.JanelaBase.columnconfigure(0, weight =2)
		self.JanelaBase.columnconfigure(1, weight =3)		
		self.JanelaBase.rowconfigure(0, weight = 3)
		self.JanelaBase.rowconfigure(1, weight = 4)	
		self.JanelaBase.rowconfigure(2, weight = 4)		
		self.JanelaBase.config(bg = self.PalhetaCores[5])

	def InsereBannerLogin(self): 
		filename = "Imagens/Banner.png"
		img = Image.open(filename)
		#img =img.resize(int(self.TamHorJanela), int(self.TamVertJanela*0.5))
		#img = img.resize((int(self.TamHorJanela*0.8), int(self.TamVertJanela*0.5)))
		img = ImageTk.PhotoImage(img)	
		LabelBanner =tk.Label(
			self.JanelaBase, image = img
			)
		LabelBanner.image = img
		LabelBanner.grid(row = 0, column = 0, columnspan=2)#, columnspan = 2)

	def CriarPaginaLogin(self): 		
		self.ContainerPaginaLogin=tk.Frame(self.JanelaBase, bg = self.PalhetaCores[8]) 
		self.ContainerPaginaLogin.rowconfigure(0, weight = 1) 
		self.ContainerPaginaLogin.rowconfigure(1, weight = 1) #Colocar tres botoes na linha 1
		self.ContainerPaginaLogin.rowconfigure(2, weight = 1)
		self.ContainerPaginaLogin.columnconfigure(0, weight = 1)
		#self.ContainerPaginaLogin.grid(row = 1, column = 0,sticky = tk.EW)
		self.ContainerPaginaLogin.grid(row = 1, column = 0,ipadx=30,ipady=30,rowspan=2)

	def InsereImagemLogin(self): 
		filename = "Imagens/tio-patinhas.png"
		img = Image.open(filename)		
		#img = img.resize((int(self.TamHorJanela), int(self.TamVertJanela*0.5)))
		img = ImageTk.PhotoImage(img)	
		LabelLogin =tk.Label(
			self.JanelaBase, image = img,
			width=450
			)
		LabelLogin.image = img
		LabelLogin.grid(row = 1, column = 1,rowspan=2)#, columnspan = 2)
		
	def InsereLabelEsquerdaSaudacao(self): #Frame para alguma string
		LabelInfo = tk.Label( #Informacoes de string
			self.ContainerPaginaLogin,#Frame de entrada
			bg = self.PalhetaCores[8],
			text = "Tudo para você, nosso melhor cliente."
			)
		LabelInfo.grid(row = 0, column = 0)	

	def ConfigurarPagLoginFrameUsuarioSenha(self): 
		self.ContainerPaginaLoginUsuarioSenha=tk.Frame(
			self.ContainerPaginaLogin, 
			bg = self.PalhetaCores[7]) 
		self.ContainerPaginaLoginUsuarioSenha.rowconfigure(0, weight = 1) 
		self.ContainerPaginaLoginUsuarioSenha.rowconfigure(1, weight = 1) 
		self.ContainerPaginaLoginUsuarioSenha.rowconfigure(2, weight = 1) 
		self.ContainerPaginaLoginUsuarioSenha.rowconfigure(3, weight = 1)
		self.ContainerPaginaLoginUsuarioSenha.rowconfigure(4, weight = 1)
		self.ContainerPaginaLoginUsuarioSenha.columnconfigure(0, weight = 1)
		self.ContainerPaginaLoginUsuarioSenha.columnconfigure(1, weight = 3)
		self.ContainerPaginaLoginUsuarioSenha.grid(row = 1, column = 0,ipadx=10,ipady=10)


	def InserePagLoginFrameUsuarioSenha(self):
		Label_Usuario = tk.Label(
			self.ContainerPaginaLoginUsuarioSenha,
			fg = "BLACK", 
			bg = self.PalhetaCores[7],
			height = 2, 
			text = "CPF:"
			)
		Label_Usuario.grid(row = 0, column = 0)		
		
		self.Entry_CPF_Usuario = tk.Entry(self.ContainerPaginaLoginUsuarioSenha)
		self.Entry_CPF_Usuario.grid(row = 0, column=1)
	
		Label_Senha = tk.Label(
			self.ContainerPaginaLoginUsuarioSenha,
			fg = "BLACK",
			bg = self.PalhetaCores[7], 
			height = 2, 
			text = "Senha."
			)
		Label_Senha.grid(row = 1, column = 0)	
		self.Entry_Senha = tk.Entry(self.ContainerPaginaLoginUsuarioSenha, show = "*")		
		self.Entry_Senha.grid(row = 1, column=1)
		
		

	def InsereBotaoAcessarContaLogin(self):	
		def _command_AcessarUsuario():
			#Verifica campos vazios:							
			CPF_Preenchido =(self.Entry_CPF_Usuario.get()!='')
			Senha_Preenchida = (self.Entry_Senha != "")			
			Campos_Preenchidos = (CPF_Preenchido and Senha_Preenchida)			
			if (Campos_Preenchidos):					
				self.Usuario.CPF = self.Entry_CPF_Usuario.get()				
				self.Usuario.senha = self.Entry_Senha.get()	
				#Falta verificar no banco de dados usuario a existencia do banco de dados e a verificacao da senha. 
				print(f"Usuario {self.Usuario.CPF} senha {self.Usuario.senha}")
				if(self.BD_Clientes.VerificarUsuarioNaBaseDados(self.Usuario.CPF)): #Continua se cliente está na base de dados.
					print(f"Cliente {self.Usuario.CPF} consta na base de dados.")	
					self.FramePrincipal.cursor =self.FramePrincipal.conexao.cursor()	
					ConsultaSenhaCliente = "SELECT senha FROM Clientes where CPF = ?"			
					self.FramePrincipal.cursor.execute(ConsultaSenhaCliente, (self.Usuario.CPF,))	#Posiciona o cursor
					SenhaCliente =self.FramePrincipal.cursor.fetchall()	
					print("Senha na base de dados: ", SenhaCliente)	
					if SenhaCliente[0][0] ==  self.Usuario.senha: 
						print("Senha confere")#Altera informacao no banco de dados. 
						#Altera status de ativo no banco de dados.
						self.FramePrincipal.cursor.execute("UPDATE Clientes SET ativo = ? where CPF = ?",(1, self.Usuario.CPF))
						self.FramePrincipal.conexao.commit() 						
						self.Paginas[2]()
					else: 
						print("Senha não confere")	
						self.Entry_Senha.delete(0, 'end')#Apaga o campo 
				else: 
					print("Usuario nao encontrado.")	
					
			else: 
				print("Há campos em branco no formulário")	

						
		ButtonAcessarConta = tk.Button(
			self.ContainerPaginaLoginUsuarioSenha, 
			bg = self.PalhetaCores[1], 
			height = 2, 
			text = "Acessar Conta", 
			command = _command_AcessarUsuario
			)		
		ButtonAcessarConta.grid(row = 3, column=0, columnspan = 2)	
		
	def PagLoginBotaoRetornar(self): 
		def _command_ButtonRetornar(): 
			self.Paginas[0]()
		ButtonRetornar = tk.Button(
			self.ContainerPaginaLogin, 
			bg = self.PalhetaCores[1], 
			height = 2, 
			text = "Retornar à página principal", 
			command = _command_ButtonRetornar
			)		
		ButtonRetornar.grid(row = 2, column=0)	



