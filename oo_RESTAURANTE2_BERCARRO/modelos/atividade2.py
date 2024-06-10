#atividade 1
class Carro:
    def __init__(self,modelo,cor,ano):
        self.modelo=modelo
        self.cor=cor
        self.ano=ano
    def __str__(self):
        return f'{self.modelo}|{self.cor}|{self.ano}'
    
carro1=Carro('Fusca','Preto','1968')
print(carro1)

#atividade 2
class Restaurante:
    nome=''
    categoria=''
    chef=''
    avaliação=''
    ativo=False

restaurante_DOM=Restaurante()
restaurante_DOM.nome='B.H.B'
restaurante_DOM.categoria='Gourmet'
restaurante_DOM.chef='Bernadete'
restaurante_DOM.avaliação='4 estrelas Michelin'
print(vars(restaurante_DOM))

#atividade 3
class Restaurante:
    def __init__(self,nome,categoria,chef,avaliação):
        self.nome=nome
        self.categoria=categoria
        self.chef=chef
        self.avaliação=avaliação
        self.ativo=False
#atividade 4
    def __str__(self):
        return f'{self.nome}|{self.categoria}|{self.chef}|{self.avaliação}|{self.ativo}'
#atividade 3
restaurante_DOM=Restaurante('B.H.B','Gourmet','Bernadete','4 estrelas Michelin')
#atividade 4
print(restaurante_DOM)

#atividade 5
class Cliente:
    def __init__(self,nome,idade,CPF):
        self.nome=nome
        self.idade=idade
        self.CPF=CPF
        self.estado='PR'
    
    def __str__(self):
        return f'{self.nome}|{self.idade}|{self.CPF}|{self.estado}'
cliente1=Cliente('Alisson',32, '313.442.157-09')

print(cliente1)



