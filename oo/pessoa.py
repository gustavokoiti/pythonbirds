class Pessoa:
    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá Sr. {id(self)}'


if __name__ == '__main__':
    gustavo = Pessoa(nome='Gustavo')
    luciano = Pessoa(gustavo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Okamura'
    del luciano.filhos
    print(luciano.__dict__)
    print(gustavo.__dict__)

