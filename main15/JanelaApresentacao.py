#coding: utf-8


import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

class JanelaApresentacao(): 
	def PreencheFrameApresentacao(self): 		
		self.JanelaBase.columnconfigure(0, weight =1)#https://www.pythontutorial.net/tkinter/tkinter-grid/
		self.JanelaBase.rowconfigure(0, weight = 1)
		self.JanelaBase.rowconfigure(1, weight = 4)
		self.JanelaBase.rowconfigure(2, weight = 4)
		self.JanelaBase.config(bg = self.PalhetaCores[3])
		
	def CriarPaginaApresentacaoTopo(self): 		
		self.ContainerPaginaApresentacaoTopo=tk.Frame(self.JanelaBase, bg = self.PalhetaCores[6]) #Passa para verde forte
		#self.ContainerPaginaApresentacaoTopo.rowconfigure(0, weight = 1)
		#self.ContainerPaginaApresentacaoTopo.rowconfigure(1, weight = 1)
		#self.ContainerPaginaApresentacaoTopo.rowconfigure(2, weight = 5) #Colocar tres botoes na linha 1
		self.ContainerPaginaApresentacaoTopo.columnconfigure(0, weight = 1)
		self.ContainerPaginaApresentacaoTopo.columnconfigure(1, weight = 1)
		self.ContainerPaginaApresentacaoTopo.columnconfigure(2, weight = 1)
		self.ContainerPaginaApresentacaoTopo.grid(row = 0, column = 0,sticky ="nsew")
	
	
	def PaginaApresentacaoBotoesTopo(self): 	
		def MudarPagLogin(): #Comando do botao para pagina de Login
			self.Paginas[1]()
		Button1 = tk.Button(
			self.ContainerPaginaApresentacaoTopo, 
			bg = self.PalhetaCores[3], 
			height = 2, 
			text = "Cadastro Pessoal",
			command = self.Paginas[3]
			)		
		Button1.grid(row = 1, column=0,ipadx=5)
		Button2 = tk.Button(
			self.ContainerPaginaApresentacaoTopo, 
			bg = self.PalhetaCores[3], 
			height = 2, 
			text = "Cadastro empresarial"
			)
		Button2.grid(row = 1, column=1,ipadx=5)
		ButtonAcessar = tk.Button(
			self.ContainerPaginaApresentacaoTopo, 
			bg = self.PalhetaCores[3], 
			height = 2, 
			text = "Acessar conta", 
			state = tk.ACTIVE, 
			command = MudarPagLogin
			)
		ButtonAcessar.grid(row = 1, column=2,ipadx=5)
		LabelAcessar = tk.Label(
			self.ContainerPaginaApresentacaoTopo, 
			bg = self.PalhetaCores[6], 
			text = "Já é cliente? ",	#Colocar moldura				
			)
		LabelAcessar.grid(row = 0, column=2, ipady = 7)


	def CriarPaginaApresentacaoCentro(self): 		
		self.ContainerPaginaApresentacaoCentro=tk.Frame(self.JanelaBase, bg = self.PalhetaCores[6]) #Passa para azul escuro
		self.ContainerPaginaApresentacaoCentro.rowconfigure(0, weight = 1) #Colocar tres botoes na linha 1
		self.ContainerPaginaApresentacaoCentro.rowconfigure(1, weight = 1)
		self.ContainerPaginaApresentacaoCentro.rowconfigure(2, weight = 1)
		self.ContainerPaginaApresentacaoCentro.rowconfigure(3, weight = 1)
		self.ContainerPaginaApresentacaoCentro.columnconfigure(0, weight = 1)
		self.ContainerPaginaApresentacaoCentro.columnconfigure(1, weight = 1)
		self.ContainerPaginaApresentacaoCentro.columnconfigure(2, weight = 3)		
		self.ContainerPaginaApresentacaoCentro.grid(row = 1, column = 0,sticky = tk.EW)
	
	def PaginaApresentacaoBotoesCentro(self):
		Button11 = tk.Button(
			self.ContainerPaginaApresentacaoCentro, 
			bg = self.PalhetaCores[4], 
			height = 2, 
			text = "Habitação",
			pady = 20,
			)
		Button11.grid(row = 1, column=0)			
		Button12 = tk.Button(
			self.ContainerPaginaApresentacaoCentro, 
			bg = self.PalhetaCores[4], 
			height = 2, 
			text = "Cartões",
			pady = 20,
			)
		Button12.grid(row = 1, column=1)			
		Button21 = tk.Button(
			self.ContainerPaginaApresentacaoCentro, 
			bg = self.PalhetaCores[4], 
			height = 2, 
			text = "Crédito",
			pady = 20,
			)
		Button21.grid(row = 2, column=0)			
		Button22 = tk.Button(
			self.ContainerPaginaApresentacaoCentro, 
			bg = self.PalhetaCores[4], 
			height = 2, 
			text = "Investimentos", 
			pady = 20,
			)
		Button22.grid(row = 2, column=1)
		#Preparacao para colocar a foto. 
		filename = "Imagens/Tela_entrada_BancoPython.jpg"
		img = Image.open(filename)
		LadoImagem = 300
		img = img.resize((LadoImagem, LadoImagem))
		img = ImageTk.PhotoImage(img)		
		Label01 = tk.Label(
			self.ContainerPaginaApresentacaoCentro, 
			image = img, 
			height = LadoImagem, 
			)
		Label01.image = img	
		Label01.grid(row=1, column = 2, sticky = tk.NS, rowspan = 3)		
		#Label01.grid_propagate(0)
		
		

	def PaginaApresentacao(self): 
		self.Apaga_frame(self.FramePrincipal) #Apaga o que tiver na janela.
		self.CriaJanelaBase() 
		self.PreencheFrameApresentacao()
		self.CriarPaginaApresentacaoTopo()	
		self.CriarPaginaApresentacaoCentro()		
		self.PaginaApresentacaoBotoesTopo()
		self.PaginaApresentacaoBotoesCentro()
		

