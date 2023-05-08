from funcionario import Funcionario
from contrato import Contrato

class Gerente(Funcionario):
    def __init__(self, nome: str, cpf: str, data_nasc: str):
        super().__init__(nome, cpf, data_nasc)
        self.__contratos = []

    @property
    def contratos(self):
        return self.__contratos

    def add_contrato(self, contrato: Contrato):
        self.__contratos.append(contrato)

    def rem_contrato(self, contrato: Contrato):
        self.__contratos.remove(contrato)