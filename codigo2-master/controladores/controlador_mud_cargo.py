from telas.tela_mud_cargo import TelaMudCargo
from entidade.mud_cargo import MudancaCargo


class ControladorMudCargo:
    def __init__(self, control_sistema):
        self.__tela_mud = TelaMudCargo()
        self.__mudancas = []
        self.__control_sistema = control_sistema

    def excluir_mudanca(self):
        mudanca = self.seleciona_mud()
        self.__mudancas.remove(mudanca)
        contrato = self.__control_sistema.controlador_contrato.pega_contrato_por_cpf(mudanca.funcionario.cpf)
        contrato.rem_mud_cargo(mudanca)

    def listar_mudancas(self):
        if len(self.__mudancas) == 0:
            self.__tela_mud.mostra_mensagem("Nenhuma mudança de cargo foi realizada.")
        else:
            for mud in self.__mudancas:
                self.__tela_mud.mostra_mud_cargo({"data": mud.data, "cargo_antigo": mud.cargo.titulo, "cargo_novo":
                                                  mud.cargo.titulo, "funcionario": mud.funcionario.nome, "id": mud.id})

    def listar_mudanca(self, mudanca):
        self.__tela_mud.mostra_mud_cargo({"data": mudanca.data, "cargo_antigo": mudanca.cargo.titulo, "id": mudanca.id,
                                          "cargo_novo": mudanca.cargo.titulo, "funcionario": mudanca.funcionario.nome})

    def seleciona_mud(self):
        self.listar_mudancas()
        id = self.__tela_mud.le_id("mudança de cargo")
        return self.pega_mud_por_id(id)

    def pega_mud_por_id(self, id):
        for mud in self.__mudancas:
            if mud.id == id:
                return mud

    def retornar(self):
        self.__control_sistema.inicializa_sistema()

    def abre_tela(self):
        lista_opcoes = {1}