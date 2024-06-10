#criando uma classe usando construtor
class Restaurante:

    restaurantes= []

    def __init__(self,nome,categoria):
        self.nome=nome.title()
        self.categoria=categoria.upper()
        self._ativo=False
        Restaurante.restaurantes.append(self)

    def __str__(self):
       # return self.nome
        return f'{self.nome}|{self.categoria}|{self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):   
        print(f'Nome do restaurante | Categoria | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(20)}|{restaurante.categoria.ljust(20)}|{restaurante.ativo}')
    @property
    def ativo(self):
        return "✅" if self._ativo else "❌"
    
    def _alternar_estado(self):
        self._ativo = not self._ativo




    

restaurante_praca=Restaurante('Praça','Gourmet')
restaurante_praca.nome='Praca 2.0'
restaurante_praca._alternar_estado()
restaurante_pizza=Restaurante("Pizza Express","Italiana")
#print(vars(restaurante_praca))
#print(vars(restaurante_pizza))
#print('')

#print(vars(restaurante_praca))
#print(vars(restaurante_pizza))
#print('')

Restaurante.listar_restaurantes()



