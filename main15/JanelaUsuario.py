#coding: utf-8

from  classCliente import *
import tkinter as tk
from PIL import ImageTk, Image


#Pagina de usuario

class JanelaUsuario(): 
	def PaginaUsuario(self):
		self.Apaga_frame(self.FramePrincipal) #Apaga o que tiver na janela.
		self.CriaJanelaBase()
		self.ClienteAtivo = Cliente()
		self.PesquisaBD() 
		self.ConfigurarPagUsuario() 		
		self.CriarPaginaUsuario()
		self.InsereBannerUsuario()
		self.InsereAnuncio()
		self.ControleBotoes()
		self.title(f"Bem vindo {self.ClienteAtivo.nome}")
	def PesquisaBD(self): 
		ConsultaClienteAtivo = "SELECT * FROM Clientes where ativo = 1"			
		self.FramePrincipal.cursor.execute(ConsultaClienteAtivo)	#Posiciona o cursor
		DadosRecebidos = self.FramePrincipal.cursor.fetchall()
		if len(DadosRecebidos)==0: 
			print(DadosRecebidos)
		else: 	
			self.ClienteAtivo.CPF = DadosRecebidos[0][0]
			self.ClienteAtivo.nome = DadosRecebidos[0][1]
			self.ClienteAtivo.senha = DadosRecebidos[0][2]
			self.ClienteAtivo.dataAbertura = DadosRecebidos[0][3]
			self.ClienteAtivo.saldo = DadosRecebidos[0][4]
			self.ClienteAtivo.extrato = DadosRecebidos[0][5]
			self.ClienteAtivo.movimentacoes = DadosRecebidos[0][6]
			self.ClienteAtivo.ativo = DadosRecebidos[0][7]


	def ConfigurarPagUsuario(self): 		
		self.JanelaBase.columnconfigure(0, weight =1)#https://www.pythontutorial.net/tkinter/tkinter-grid/
		self.JanelaBase.rowconfigure(0, weight = 1)
		self.JanelaBase.rowconfigure(1, weight = 1)	
		self.JanelaBase.rowconfigure(2, weight = 20)		
		self.JanelaBase.config(bg = self.PalhetaCores[5])
		
				
	def CriarPaginaUsuario(self):
		self.ContainerDinamico = tk.Frame(self.JanelaBase) 		
		self.ContainerPaginaUsuario=tk.Frame(self.JanelaBase, bg = self.PalhetaCores[8]) #Passa para marrom
		self.ContainerPaginaUsuario.rowconfigure(0, weight = 1) #Colocar tres botoes na linha 1
		self.ContainerPaginaUsuario.rowconfigure(1, weight = 1) #Colocar tres botoes na linha 1
		self.ContainerPaginaUsuario.columnconfigure(0, weight = 1)
		self.ContainerPaginaUsuario.columnconfigure(1, weight = 1)
		self.ContainerPaginaUsuario.columnconfigure(2, weight = 1)
		self.ContainerPaginaUsuario.columnconfigure(3, weight = 1)
		self.ContainerPaginaUsuario.grid(row = 1, column = 0,sticky = tk.EW)
		self.ContainerDinamico.grid(row = 2,column = 0)
	
	
	def InsereBannerUsuario(self): 
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
		
	
		
	def InsereAnuncio(self): 
		filename = "Imagens/Teletubbies.jpg"
		img = Image.open(filename)
		#img =img.resize(int(self.TamHorJanela), int(self.TamVertJanela*0.5))
		#img = img.resize((int(self.TamHorJanela*0.8), int(self.TamVertJanela*0.5)))
		img = ImageTk.PhotoImage(img)	
		LabelBanner_teletubbies =tk.Label(
			self.ContainerDinamico, image = img
			)
		LabelBanner_teletubbies.image = img
		LabelBanner_teletubbies.pack()
		#self.LabelBanner_teletubbies.grid(row = 2, column = 0, sticky = tk.EW, columnspan = 2)
		
			

	def ControleBotoes(self):

		def ContainerDadosParaTransferir():
			self.DadosParaTransferir = tk.Frame(self.ContainerDinamico)
			self.DadosParaTransferir.columnconfigure(0, weight = 1) 
			self.DadosParaTransferir.columnconfigure(1, weight = 1) 
			self.DadosParaTransferir.rowconfigure(0, weight = 1)
			self.DadosParaTransferir.rowconfigure(1, weight = 1)
			self.DadosParaTransferir.rowconfigure(2, weight = 1)
			self.DadosParaTransferir.rowconfigure(3, weight = 1)
			self.DadosParaTransferir.rowconfigure(4, weight = 1)
			self.DadosParaTransferir.rowconfigure(5, weight = 1)

			label_chave = tk.Label(self.DadosParaTransferir,text= "Chave:")
			label_cpf = tk.Label(self.DadosParaTransferir,text= "CPF:")
			label_monto = tk.Label(self.DadosParaTransferir,text= "Monto:")
			botomTransferir = tk.Button(self.DadosParaTransferir,text = "Transferir")

			self.entry_chave = tk.Entry(self.DadosParaTransferir)
			self.entry_cpf = tk.Entry(self.DadosParaTransferir)
			self.entry_monto = tk.Entry(self.DadosParaTransferir)

			label_chave.grid(row = 1,column=0)
			label_cpf.grid(row = 2,column=0)
			label_monto.grid(row = 3,column=0)
			botomTransferir.grid(row = 4,column = 0,columnspan=2)
			self.entry_chave.grid(row=1,column=1)
			self.entry_cpf.grid(row=2,column=1)
			self.entry_monto.grid(row=3,column=1)
			self.DadosParaTransferir.pack()

		def FazerTransferencia():
			print("hola mundo")

		def JanelaFazerTransferenca():
			self.Apaga_frame(self.ContainerDinamico)
			ContainerDadosParaTransferir()
		
		def GerarSaldo():
			self.Apaga_frame(self.ContainerDinamico)
			label_usuario = tk.Label(self.ContainerDinamico,text = self.ClienteAtivo.nome)
			label_saldo = tk.Label(self.ContainerDinamico,text= self.ClienteAtivo.saldo)
			label_usuario.grid(row = 2,column=0)
			label_saldo.grid(row = 3,column=0)

			print("Saldo = ",self.ClienteAtivo.saldo)
			

		def SaidaApp(): 
			self.FramePrincipal.cursor.execute("UPDATE Clientes SET ativo = ? where CPF = ?",(0, self.ClienteAtivo.CPF))
			self.FramePrincipal.conexao.commit()
			print("Saida do programa") 			
			self.FramePrincipal.quit()
		

		Button1 = tk.Button(
			self.ContainerPaginaUsuario, 
			bg = self.PalhetaCores[3], 
			height = 2, 
			text = "Transferencia", 
			command = JanelaFazerTransferenca
			)		
		Button1.grid(row = 0, column=1)	
		ButtonRetornarInicio = tk.Button(
			self.ContainerPaginaUsuario, 
			bg = self.PalhetaCores[3], 
			height = 2, 
			text = "Botao Retornar", 
			command = self.Paginas[0]			
			)		
		ButtonRetornarInicio.grid(row = 0, column=2)	

		ButtonSair = tk.Button(
			self.ContainerPaginaUsuario, 
			bg = self.PalhetaCores[3], 
			height = 2, 
			text = "Sair do Aplicativo", 
			command = SaidaApp #Tem que colocar a saida do banco de dados, tudo. Utilizar update para ativo passar para zero. 
			)		
		ButtonSair.grid(row = 0, column=3)	
		ButtonGerarSaldo = tk.Button(
			self.ContainerPaginaUsuario,
			bg = self.PalhetaCores[3], 
			height = 2, 
			text = "Gerar Saldo", 
			command = GerarSaldo
			)
		ButtonGerarSaldo.grid(row = 0, column=0)			
		
		

