#coding: utf-8
#Desenvolvendo a funcao de transferir

import tkinter as tk
import BancoDadosCliente as BDC
#https://docs.python.org/pt-br/3.13/library/tkinter.messagebox.html

'''
Pagina de login gravando nome do usuario. 


'''
from JanelaBase import *
from JanelaApresentacao import *
from JanelaLogin import *
from JanelaUsuario import *
from JanelaAbrirConta import *


class JanelaRaiz(
		tk.Tk, 
		JanelaBase,
		JanelaApresentacao,
		JanelaLogin,
		JanelaUsuario,
		JanelaAbrirConta,
		): 
	def __init__(self, nomeDB): 
		super().__init__()
		self.NomeBD_Clientes = nomeDB		
		self.BD_Clientes = BDC.BancoDadosCliente(self.NomeBD_Clientes)
		self.conexao, self.cursor = self.BD_Clientes.get_cursor_conexao()
		self.TituloApp = "Banco Python"
		self.title(self.TituloApp)
		self.set_PalhetaCores()
		self.ConfiguraTelaInicial()
		self.FramePrincipal = self

		self.Paginas = [
			self.PaginaApresentacao, #0
			self.PaginaLogin, #1
			self.PaginaUsuario,#2
			self.PaginaAbrirConta, #3	
		]	#requer as funcoes operando	
		self.CriaJanelaBase()		
		self.Paginas[0]()
	
	def __del__(self): 
		print("Desfaz conexao com BD")
			
	def ConfiguraTelaInicial(self): 
		self.TamHorJanela = int(self.winfo_screenwidth()*0.6)
		self.TamVertJanela = int(self.winfo_screenheight()*0.8)	
		self.TamTela = str(self.TamHorJanela)+"x"+str(self.TamVertJanela)		
		self.geometry(self.TamTela)
		self.config(bg = self.PalhetaCores[0])
		
	def set_PalhetaCores(self): 
		self.PalhetaCores = [
			"#222448", #Azul escuro.
			"#54527E", #Roxo claro
			"#c0f0c0", #Verde claro
			"#93bd93", #Verde Ifsc
			"WHITE", 
			"CYAN",
			"GREEN",
			"ORANGE",
			"BROWN",		
			]

		
if __name__=="__main__": 
	NomeDB = "BancoDadosUsuarioClientes.db"
	#CriaBD_clientes = BDC.CriarBancoDados(NomeDB)
	InstanciaRaiz = JanelaRaiz(NomeDB)
	#print(InstanciaRaiz)
	InstanciaRaiz.mainloop()
	
	

