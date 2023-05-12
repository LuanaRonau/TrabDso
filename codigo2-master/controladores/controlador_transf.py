from controlador_filial import ControladorFilial
from tela.tela_transf import TelaTransf

class ControladorTransf:

    def __init__(self):
        self.__tela_transf = TelaTransf
        self.__control_filial = ControladorFilial
        self.__transferencias =[]

    def incluir_transf(self):
        dados_transf =
