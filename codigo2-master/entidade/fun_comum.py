from funcionario import Funcionario
from gerente import Gerente

class FunComum(Funcionario):
    def __init__(self, nome: str, cpf: str, data_nasc: str, gerente: Gerente):
        super().__init__(nome, cpf, data_nasc)
        self.__gerente = gerente

    @property
    def gerente(self):
        return self.__gerente

    @gerente.setter
    def gerente(self, gerente: Gerente):
        self.__gerente = gerente