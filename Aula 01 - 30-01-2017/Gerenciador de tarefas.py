class Projeto():
    def __init__(self,nome=None):
        self.nome=nome      
    def __str__(self):
        return self.nome

class Tarefa():
    def __init__(self, descricao=None, data_inicial=None, data_final=None, prioridade=None):
         self.descricao=descricao
         self.data_inicial=data_inicial
         self.data_final=data_final
         self.prioridade=prioridade
         self.projeto=Projeto()
         self.pessoaJ=PessoaJuridica()
         self.pessoaFisica=PessoaFisica()
    def __str__(self):
        return self.descricao, self.data_ini, self.data_fin, self.prioridade
    
class Pessoa():
    def __init__(self,nome=None):
        self.nome=nome
    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    def __init__(self,nome=None,cpf=None):
        Pessoa.__init__(self,nome)
        self.nome=nome
        self.cpf=cpf
    def __str__(self):
        return self.nome, self.cpf
    
class PessoaJuridica(Pessoa):
    def __init__(self,nome=None,cnpj=None):
        Pessoa.__init__(self,nome)
        self.cnpj=cnpj
    def __str__(self):
        return self.nome, self.cnpj

