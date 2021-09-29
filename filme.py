class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome
        self.ano = ano
        self.__like = 0

    def dar_like(self):
        self.__like += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome

    @property
    def like(self):
        return self.__like

    def dar_like(self):
        self.__like += 1


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


