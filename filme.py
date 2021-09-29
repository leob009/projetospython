class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._like = 0

    def dar_like(self):
        self._like += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novoNome):
        self._nome = novoNome

    @property
    def like(self):
        return self._like



class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
