from datetime import datetime
class Tarefa:
	def __init__(self, nome, prioridade, prazo):
		self.nome = nome
		self.prioridade = prioridade
		self.prazo = prazo
		self.inicio = None
		self.fim = None
		self.status = "Nova"

	def iniciar_tarefa(self):
		if self.status == "Nova" and self.inicio is None:
			self.inicio = datetime.now()
			self.status = "Em andamento"
			print(f"A tarefa {self.nome} foi iniciada em {self.inicio}")
		else:
			print(f"A tarefa {self.nome} já foi iniciada ou concluída")

	def finalizar_tarefa(self):
		if self.status == "Em andamento":
			self.fim = datetime.now
			self.status = "Concluída"
			print(f"A tarefa {self.nome} foi concluída em {self.fim}")
		else:
			print(f"A tarefa {self.nome} ainda não foi iniciada ou já foi concluída")

	def editar_tarefa(self, nome=None, prioridade=None, prazo=None):
		if nome:
			self.nome = nome
		if prioridade:
			self.prioridade = prioridade
		if prazo:
			self.prazo = prazo
		print(f"Tarefa {self.nome} editada com sucesso!")
	
	def __str__(self):
		return f"{self.nome} | Prioridade: {self.prioridade} | Prazo: {self.prazo} | Status: {self.status}"