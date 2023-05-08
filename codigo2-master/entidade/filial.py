
class Filial:
    def __init__(self, cep: int, cidade: str):
        self.__cep = cep
        self.__cidade = cidade
        self.__funcionarios = []


    @property
    def cep(self):
        return self.__cep

    @property
    def cidade(self):
        return self.__cidade

    @property
    def funcionarios(self):
        return self.__funcionarios

    @cep.setter
    def cep(self, cep):
        if isinstance(cep, str):
            self.__cep = cep

    @cidade.setter
    def cidade(self, cidade):
        if isinstance(cidade, str):
            self.__cidade = cidade

    @funcionarios.setter
    def funcionarios(self, funcionarios: list):
        self.__funcionarios = funcionarios