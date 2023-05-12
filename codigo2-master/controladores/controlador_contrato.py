from telas.tela_contratos import TelaContratos
from entidade.contrato import Contrato
from controlador_filial import ControladorFilial
from datetime import datetime, date

class ControladorContrato:

    def __init__(self, control_filial):
        self.__contratos = []
        self.__tela_contrato = TelaContratos()
        self.__control_filial = control_filial

    def pega_contrato_por_codigo(self, codigo: int):
        for contrato in self.__contratos:
            if(contrato.codigo == codigo):
                return contrato
        return None

    def incluir_contrato(self):
        dados_contrato = self.__tela_contrato.pega_dados_contrato()
        id = dados_contrato["id"]
        data_inicio = dados_contrato["data_inicio"]
        #data_inicio.strftime("%d/%m/%Y")
        cargo = self.__control_filial.controlador_cargo.pega_cargo()
        empregado = self.__control_filial.pega_func_por_cpf(dados_contrato["cpf"])
        filial = self.__control_filial.pega_filial_por_cep(dados_contrato["cep"])
        empregador = filial.gerente
        empregado.atividade = True

        novo_contrato = Contrato(id, data_inicio, cargo, empregado, filial, empregador)
        self.__contratos.append(novo_contrato)
        empregador.add_contrato(novo_contrato)

    def alterar_contrato(self):
        self.listar_contratos()
        id_contrato = self.__tela_contrato.seleciona_contrato()
        contrato = self.pega_contrato_por_id(id_contrato)

        if (contrato is not None):
            novos_dados_contrato = self.__tela_contrato.pega_dados_contrato()
            contrato.data_inicio = novos_dados_contrato["data_inicio"]
            contrato.empregado = self.__control_filial.pega_func_por_cpf(novos_dados_contrato["cpf"])
            if (contrato.filial != novos_dados_contrato["filial"]):
                print("Filial não alterada, para alterá-la realize uma transferência.")
            self.listar_contrato(contrato)
        else:
            raise ValueError

    def pega_contrato_por_id(self, id: int):
        for contrato in self.__contratos:
            if (contrato.id == id):
                return contrato
        return None

    def listar_contratos(self):
        for contrato in self.__contratos:
            self.__tela_contrato.mostra_contrato({"empregador": contrato.empregador.nome, "id": contrato.id,
                                                  "empregado": contrato.empregado.nome, "cargo": contrato.cargo.titulo,
                                                  "filial": contrato.filial.cidade})

    def listar_contrato(self, contrato):
        self.__tela_contrato.mostra_contrato({"empregador": contrato.empregador.nome, "id": contrato.id, "empregado":
                                              contrato.empregado.nome, "cargo": contrato.cargo.titulo,
                                              "filial": contrato.filial.cidade})

    def excluir_contrato(self):
        self.listar_contratos()
        id_contrato = self.__tela_contrato.seleciona_contrato()
        contrato = self.pega_contrato_por_id(id_contrato)

        if (contrato is not None):
            self.__contratos.remove(contrato)
            self.listar_contrato(contrato)
            self.__tela_contrato.exclui_id(id_contrato)
        else:
            raise ValueError

    def retornar(self):
        self.__control_filial.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_contrato, 2: self.alterar_contrato, 3: self.listar_contratos, 4: self.excluir_contrato}

        continua = True
        while continua:
            opcao = self.__tela_contrato.tela_opcoes()
            while True:
                try:
                    lista_opcoes[opcao]()
                except ValueError:
                    print("Comando inválido")
                    lista_opcoes[opcao]()
