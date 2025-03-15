#coding: utf-8


import tkinter as tk

class JanelaBase(): 
	def Apaga_frame(self, frame): #Usado para trocar de tela. 
		for filho in frame.winfo_children(): 
			filho.destroy()		

	def CriaJanelaBase(self ): 	
		self.JanelaBase= tk.Frame(
			self.FramePrincipal, 
			bg = self.PalhetaCores[1] #Coloca em roxo claro.
			)
		self.JanelaBase.pack(fill = tk.BOTH, expand = True)		


