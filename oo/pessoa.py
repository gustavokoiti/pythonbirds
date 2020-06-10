class Pessoa:
    def __init__(self, nome=None, idade=37):
        self.idade = idade
        self.nome = nome


    def cumprimentar(self):
        return f'Olá Sr. {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Gustavo')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Gustavo Koiti'
    print(p.nome)
    print(p.idade)