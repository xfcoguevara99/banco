#coding: utf-8

from datetime import datetime
import tkinter as tk
from classCliente import *
from PIL import ImageTk, Image	

from tkinter import messagebox 
  
#Pagina de login
class JanelaAbrirConta(): 
	def PaginaAbrirConta(self): 
		self.Apaga_frame(self.FramePrincipal)
		self.CriaJanelaBase() 
		self.title("Criacao de conta")
		self.ConfigurarPaginaInicial()
		self.CriarPaginaAbrirConta()
		self.InsereLabelEsquerdaInformacoes()
		self.CriarFrameUsuarioSenha()
		self.CriarFrameColuna2()
		self.InsereFrameUsuarioSenha()
		self.InsereBotaoCriarConta()
		self.InsereBannerContaCriada()
		self.CriarBotaoPagLogin()
		self.CriarBotaoRetornar()
		self.Cliente = Cliente() #Cliente a verificar
		

		
	def ConfigurarPaginaInicial(self): 	
		#Colocar duas linhas no inicio
		self.JanelaBase.columnconfigure(0, weight =1)		
		self.JanelaBase.rowconfigure(0, weight = 1)
		self.JanelaBase.rowconfigure(1, weight = 4)	
		self.JanelaBase.rowconfigure(2, weight = 1)	
		self.JanelaBase.rowconfigure(3, weight = 20)	
		self.JanelaBase.config(bg = self.PalhetaCores[5])

	def CriarPaginaAbrirConta(self): 		
		self.ContainerPaginaAbrirConta=tk.Frame(self.JanelaBase, bg = self.PalhetaCores[8]) 
		self.ContainerPaginaAbrirConta.rowconfigure(0, weight = 1) 
		self.ContainerPaginaAbrirConta.rowconfigure(1, weight = 1) #Colocar tres botoes na linha 1
		self.ContainerPaginaAbrirConta.columnconfigure(0, weight = 1)
		self.ContainerPaginaAbrirConta.columnconfigure(1, weight = 1)
		self.ContainerPaginaAbrirConta.columnconfigure(2, weight = 1)
		self.ContainerPaginaAbrirConta.grid(row = 1, column = 0,sticky = tk.EW)#, rowspan = 2)
	
	def InsereBannerContaCriada(self): 
		filename = "Imagens/Banner.png"
		img = Image.open(filename)
		#img =img.resize(int(self.TamHorJanela), int(self.TamVertJanela*0.5))
		#img = img.resize((int(self.TamHorJanela*0.8), int(self.TamVertJanela*0.5)))
		img = ImageTk.PhotoImage(img)	
		LabelBanner =tk.Label(
			self.JanelaBase, image = img
			)
		LabelBanner.image = img
		LabelBanner.grid(row = 0, column = 0)#, columnspan = 2)
		
	
	
	def InsereImagemContaCriada(self): 
		filename = "Imagens/TelaParabensContaCriada.png"
		img = Image.open(filename)
		#img =img.resize(int(self.TamHorJanela), int(self.TamVertJanela*0.5))
		img = img.resize((int(self.TamHorJanela*0.8), int(self.TamVertJanela*0.5)))
		img = ImageTk.PhotoImage(img)	
		LabelParabens =tk.Label(
			self.JanelaBase, image = img
			)
		LabelParabens.image = img
		LabelParabens.grid(row = 2, column = 0, sticky = tk.EW)#, columnspan = 2)
		print(int(self.TamHorJanela), int(self.TamVertJanela*0.5))
		
		
	def InsereLabelEsquerdaInformacoes(self): #Frame para alguma string
		LabelInfo = tk.Label( #Informacoes de string
			self.ContainerPaginaAbrirConta,#Frame de entrada
			bg = self.PalhetaCores[8], 
			#height = 10, 
			text = "Aproveite\n as vantagens\n de ser cliente.",
			font=["None",12,"bold"],
			justify="center"
			)
		LabelInfo.grid(row = 0, column = 0)	

	def CriarFrameColuna2(self):
		self.ContainerFrameColuna2=tk.Frame(
			self.ContainerPaginaAbrirConta, 
			bg = self.PalhetaCores[8]) 
		self.ContainerFrameColuna2.rowconfigure(0, weight = 1) 
		self.ContainerFrameColuna2.rowconfigure(1, weight = 1) 
		self.ContainerFrameColuna2.columnconfigure(0, weight = 1)
		self.ContainerFrameColuna2.grid(row = 0, column = 2,sticky = tk.EW)


	def CriarBotaoRetornar(self): 
		def _command_ButtonRetornar(): 
			self.Paginas[0]()
		ButtonRetornar = tk.Button(
			self.ContainerFrameColuna2, 
			bg = self.PalhetaCores[1], 
			height = 2, 
			text = "Retornar à página principal", 
			command = _command_ButtonRetornar
			)		
		ButtonRetornar.grid(row = 0, column=0,  pady = 3)	
		
	def CriarBotaoPagLogin(self): 
		def _command_ButtonPagLogin(): 
			self.Paginas[1]()
		ButtonPagLogin = tk.Button(
			self.ContainerFrameColuna2, 
			bg = self.PalhetaCores[1], 
			height = 2, 
			text = "Fazer Login", 
			command = _command_ButtonPagLogin
			)		
		ButtonPagLogin.grid(row = 1, column=0,  pady = 3)	


	def CriarFrameUsuarioSenha(self): 
		self.ContainerPaginaUsuarioSenha=tk.Frame(
			self.ContainerPaginaAbrirConta, 
			bg = self.PalhetaCores[7]) 
		self.ContainerPaginaUsuarioSenha.rowconfigure(0, weight = 1) 
		self.ContainerPaginaUsuarioSenha.rowconfigure(1, weight = 1) 
		self.ContainerPaginaUsuarioSenha.rowconfigure(2, weight = 1) 
		self.ContainerPaginaUsuarioSenha.rowconfigure(3, weight = 1)
		self.ContainerPaginaUsuarioSenha.rowconfigure(4, weight = 1)
		self.ContainerPaginaUsuarioSenha.rowconfigure(5, weight = 1)
		self.ContainerPaginaUsuarioSenha.columnconfigure(0, weight = 1)
		self.ContainerPaginaUsuarioSenha.columnconfigure(1, weight = 3)
		self.ContainerPaginaUsuarioSenha.grid(row = 0, column = 1,sticky = tk.EW)
	
	def InsereFrameUsuarioSenha(self):
		Label_Topo = tk.Label(
			self.ContainerPaginaUsuarioSenha,
			fg = "BLACK", 
			height = 2, 
			bg = self.PalhetaCores[7],
			text = "Abra sua conta",
			font=["None",15,"bold"]
			)
		Label_Topo.grid(row = 0, column = 0, columnspan = 2, pady = 5)		
		
		Label_Nome = tk.Label(
			self.ContainerPaginaUsuarioSenha,
			fg = "BLACK", 
			height = 2, 
			bg = self.PalhetaCores[7],
			text = "Usuário: ",
			font=["normal",10,"bold"]
			)
		Label_Nome.grid(row = 1, column = 0, pady = 2)	
		self.Entry_Nome_usuario = tk.Entry(self.ContainerPaginaUsuarioSenha)
		self.Entry_Nome_usuario.grid(row = 1, column=1)
		
		
		Label_CPF = tk.Label(
			self.ContainerPaginaUsuarioSenha,
			fg = "BLACK", 
			height = 2, 
			bg = self.PalhetaCores[7],
			text = "CPF: ",
			font=["normal",10,"bold"]
			)
		Label_CPF.grid(row = 2, column = 0, pady = 2)	
		self.Entry_CPF_usuario = tk.Entry(self.ContainerPaginaUsuarioSenha)
		self.Entry_CPF_usuario.grid(row = 2, column=1)			

		Label_Senha1 = tk.Label(
			self.ContainerPaginaUsuarioSenha,
			fg = "BLACK", 
			height = 2, 
			bg = self.PalhetaCores[7],
			text = "Senha.",
			font=["normal",10,"bold"]
			)
		Label_Senha1.grid(row = 3, column = 0, pady = 2)	
		self.Entry_Senha1 = tk.Entry(self.ContainerPaginaUsuarioSenha, show = "*")
		self.Entry_Senha1.grid(row = 3, column=1)
		
		
		Label_Senha2 = tk.Label(
			self.ContainerPaginaUsuarioSenha,
			fg = "BLACK", 
			height = 2, 
			bg = self.PalhetaCores[7],
			text = "Repetir senha.",
			font=["normal",10,"bold"]
			)
		Label_Senha2.grid(row = 4, column = 0, pady = 2)	
		self.Entry_Senha2 = tk.Entry(self.ContainerPaginaUsuarioSenha, show = "*")
		self.Entry_Senha2.grid(row = 4, column=1)

	def InsereBotaoCriarConta(self):	
		def _command_CriarUsuario():
			senha = ''
			#Verifica campos vazios:				
			Nome_Preenchido =  (self.Entry_Nome_usuario.get()!='')
			CPF_Preenchido =(self.Entry_CPF_usuario.get()!='')
			Senha1_Preenchido = (self.Entry_Senha1 != "")
			Senha2_Preenchido = (self.Entry_Senha2 != "")
			Campos_Preenchidos = (Nome_Preenchido and CPF_Preenchido and Senha1_Preenchido and Senha2_Preenchido)				
			flag = False
			if self.Entry_Senha1.get()==self.Entry_Senha2.get(): 				
				flag = True
				senha = self.Entry_Senha1.get()
			else: 
				print("Senhas nao coincidem")	
			self.Entry_Senha1.delete(0, 'end')	#Apaga o que estiver escrito no campo da senha		
			self.Entry_Senha2.delete(0, 'end')			
			if flag: 
				if (Campos_Preenchidos):
					self.Cliente.nome = self.Entry_Nome_usuario.get()
					self.Cliente.CPF = self.Entry_CPF_usuario.get()				
					self.Cliente.senha = senha
					self.Cliente.saldo = 1000.0
					self.Cliente.ativo = 0					
					self.Cliente.dataAbertura = datetime.now()				
					if(self.BD_Clientes.InserirCliente(self.Cliente)):#Conta criada
						print(f"Cliente {self.Cliente.nome} inserido no banco de dados.")
						self.InsereImagemContaCriada()
						messagebox.showinfo("Importante!!",f"Dados do cliente {self.Cliente.nome} inseridos com sucesso na base de dados." ) 	
					else: 
						print(f"Cliente {self.Cliente.nome} já está na base de dados.")
						messagebox.showwarning("Atenção!!","Cliente Já na base de dados." ) 	
				else: 
					print("Há campos em branco no formulário")	

						
		ButtonCriarConta = tk.Button(
			self.ContainerPaginaUsuarioSenha, 
			bg = self.PalhetaCores[1], 
			height = 2, 
			text = "Criar Conta", 
			command = _command_CriarUsuario
			)		
		ButtonCriarConta.grid(row = 5, column=0, columnspan = 2, pady = 3)	
		
		
		
		
		
			
		
