class Pessoa:
    olhos = 2

    def __init__(self, *pets, nome = None, idade = 39):
        self.idade = idade
        self.nome = nome
        self.pets = list(pets)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_class = super().cumprimentar()
        return f'{cumprimentar_da_class}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    jack = Homem(nome='Jack')
    victor = Mutante(jack, nome='Victor')

    print(Pessoa.cumprimentar(victor))
    print(id(victor))
    print(victor.cumprimentar())
    print(victor.nome)
    print(victor.idade)
    for pet in victor.pets:
            print(pet.nome)
    victor.sobrenome = 'Nunes'
    del victor.pets
    jack.olhos = 1
    del jack.olhos
    print (victor.__dict__)
    print (jack.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(victor.olhos)
    print(jack.olhos)
    print(id(Pessoa.olhos), id(victor.olhos), id(jack.olhos))
    print(Pessoa.metodo_estatico(), victor.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), victor.metodo_estatico())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(pessoa,Homem))
    print(isinstance(victor,Homem))
    print(isinstance(victor,Pessoa))
    print(victor.olhos)
    print(jack.cumprimentar())
    print(victor.cumprimentar())
