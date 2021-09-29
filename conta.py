class Conta:

    def __init__(self, numero, titular, saldo, limite) -> object:
        print(f'construindo objeto...{self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'saldo de {self.__saldo} do titular {self.__titular}')

    def saca(self, valor):
        if valor <= (self.__saldo + self.__limite):
            self.__saldo -= valor

    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, NovoSaldo):
        self.__saldo = NovoSaldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, NovoLimite):
        self.__limite = NovoLimite

    @staticmethod
    def codigo_banco():
        return '001'
