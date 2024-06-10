#questao 1
#class Pessoa:
    #def __init__(self,nome,idade,profissao):
     #   self.nome=nome
      #  self.idade=idade
       # self.profissao=profissao
    


   # def __str__(self):
      #  return f'Nome: {self.nome} | Idade: {self.idade} | Profissão: {self.profissao}'
    
    #def aniversario(self):
       # for idades in self.idade:
        #    self.idade +=1
            
   # def aniversario(self):
      #  self.idade += 1
    
   # @property
   # def saudacao(self):
    #    if self.profissao == self.profissao:
     #       print(f'Ola {self.profissao} tenha um bom dia')
      #  else: print("tenha um pessimo dia")

#Pessoa1= Pessoa("maju",'12','Professor')
#print(Pessoa1)

#questao 2 
class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
#3
    def __str__(self):
        return f"Titular: {self._titular}, Saldo: {self._saldo}"
# 4 
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = not conta._ativo
#5
    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

#7
class ClienteBanco:
    def __init__(self, nome, sobrenome, idade, endereco, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone

    @classmethod
    def conta(cls):
        return "Essa é uma conta bancária de um cliente do banco."

conta1 = ContaBancaria("Maju", 1000)
conta2 = ContaBancaria("Bernardo", 2000)


print(conta1)
print(conta2)


ContaBancaria.ativar_conta(conta1)


print(conta1.ativo)

#8
cliente1 = ClienteBanco("Alisson", "Carlesso", 16, "Rua Jose Paiva Vidal", "419810-0910")
print(cliente1.nome)


print(ClienteBanco.conta())
