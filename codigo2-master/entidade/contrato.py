from funcionario import Funcionario
from fun_comum import FunComum
from gerente import Gerente
from filial import Filial
from mud_cargo import MudancaCargo
from transferencia import Transferencia
from cargo import Cargo
from datetime import datetime, date
from exception.jaEAFilialAtualException import JaEAFilialAtualException
from exception.jaEOCargoAtualException import JaEOCargoAtualException


class Contrato:
    def __init__(self, id: int, data_inicio: date, cargo: Cargo, empregado: Funcionario, filial: Filial, empregador: Gerente):
        self.__id = id
        self.__data_inicio = date
        self.__data_final = None
        self.__cargo = cargo
        self.__empregado = empregado
        self.__filial = filial        
        self.__empregador = empregador
        self.__mud_cargos = []
        self.__transferencias = []

    @property
    def id(self):
        return self.__id

    @property
    def data_inicio(self):
        return self.__data_inicio

    @property
    def data_final(self):
        return self.__data_final

    @property
    def cargo(self):
        return self.__cargo

    @property
    def empregado(self):
        return self.__empregado

    @property
    def filial(self):
        return self.__filial

    @property
    def empregador(self):
        return self.__empregador

    @property
    def mud_cargos(self):
        return self.__mud_cargos
    
    @property
    def transferencias(self):
        return self.__transferencias
    
    @data_inicio.setter
    def data_inicio(self, data_inicio: date):
        self.__data_inicio = data_inicio

    @data_final.setter
    def data_final(self, data_final: date):
        self.__data_final = data_final

    @cargo.setter
    def cargo(self, cargo: Cargo):
        self.__cargo = cargo

    @empregado.setter
    def empregado(self, empregado: Funcionario):
        self.__empregado = empregado

    @filial.setter
    def filial(self, filial: Filial):
        self.__filial = filial

    @empregador.setter
    def empregador(self, empregador: Gerente):
        self.__empregador = empregador

    def add_transferencia(self, id: int, filial_nova: Filial, funcionario: Funcionario, data: Date):
        if (filial_nova == self.__filial):
            raise JaEAFilialAtualException(filial_nova)
        self.__transferencias.append(Transferencia(id, self.__filial, filial_nova, funcionario, data))
        self.__filial = filial_nova

    def add_mud_cargo(self, id: int, cargo_novo: Cargo, funcionario: Funcionario, data: Date):
        if (cargo_novo == self.__cargo):
            raise JaEOCargoAtualException(cargo_novo)
        self.__mud_cargos.append(MudCargo(id, self.__cargo, cargo_novo, funcionario, data))
        self.__cargo = cargo_novo
        
        if (cargo_novo.titulo == "Gerente"):
            self.__empregado = funcionario
            self.__empregador = "Empresa"

    def rem_transferencia(self, transferencia):
        self.__transferencias.remove(transferencia)

    def rem_mud_cargo(self, mud_cargo):
        self.__mud_cargos.remove(mud_cargo)
