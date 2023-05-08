from telas import  Telas

class TelaFilial(Telas):

    def __init__(self, cep):
        self.__cep = cep
        self.__controlador_filial = ControladorFilial(cep)



