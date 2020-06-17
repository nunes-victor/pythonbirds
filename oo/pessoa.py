class Pessoa:
    def __init__(self, *pets, nome = None, idade = 39):
        self.idade = idade
        self.nome = nome
        self.pets = list(pets)

    def cumprimentar(self):
        return f'Olá{id(self)}'


if __name__ == '__main__':
    jack = Pessoa(nome='Jack')
    victor = Pessoa(jack, nome='Victor')
    print(Pessoa.cumprimentar(victor))
    print(id(victor))
    print(victor.cumprimentar())
    print(victor.nome)
    print(victor.idade)
    for pet in victor.pets:
            print(pet.nome)