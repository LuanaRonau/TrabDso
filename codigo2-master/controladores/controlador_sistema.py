from entidade.filial import Filial
from telas.tela_sistema import TelaSistema
from exception.repeticao import Repeticao

class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__lista_filials = [Filial(222, "Floripa")]

    def adicionar_filial(self):
        nova_filial = self.__tela_sistema.pega_info_cadastro()
        for _ in self.__lista_filials:
            if _.cidade == nova_filial.cidade:
                raise Repeticao("cidade", nova_filial.cidade)
            if _.cep == nova_filial.cep:
                raise Repeticao("CEP", nova_filial.cep)

        self.__lista_filials.append(nova_filial)

    def inicializa_sistema(self):
        lista_opcoes = {1: self.adicionar_filial()}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
