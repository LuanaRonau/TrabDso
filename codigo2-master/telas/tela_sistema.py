from controladores.controlador_sistema import ControladorSistema
from entidade.filial import Filial
from telas import Telas

class TelaSistema(Telas):

    def __init__(self):
        self.__controlador_sis = ControladorSistema()

    def pega_info_cadastro(self):
        print("BEM VINDO AO CADASTRO DE FILIAIS")
        print("(Duas unidades na mesma cidade não serão aceitas.)")
        nova_cidade = input("Digite a cidade: ")
        novo_cep = int(input("Digite o CEP: "))
        return Filial(novo_cep, nova_cidade)


    def tela_opcoes(self):
        opcao = input("SEJA BEM VINDO AO SISTEMA! "
              +"Oque deseja fazer?"
              +"1) Adicionar uma nova filial"
              +"2) Excluir uma nova filial"
              +"3) Editar uma filial (identificação por cep)"
              +"4) Listar todas as filiais por fitragem")
        return opcao
