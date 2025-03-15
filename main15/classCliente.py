#coding: utf-8
class Cliente: 
	def __init__(self, nome = '', cpf='', senha='' ): 			
		self.nome = nome
		self.CPF = cpf
		self.senha = senha
		self.dataAbertura = ''
		self.saldo = 0.
		self.extrato = ''
		self.movimentacoes = ''
		self.ativo = 0

