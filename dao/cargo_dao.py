from dao.dict_dao import DictDAO
from entidade.cargo import Cargo


class CargoDAO(DictDAO):
    def __init__(self):
        super().__init__('cargos.pkl')
        # inicia já com algumas opções
        cargo1 = Cargo("Gerente", "Controle de uma filial", 1000)
        cargo2 = Cargo("Atendente", "Atender os clientes", 600)
        cargo3 = Cargo("Faxineiro interno", "Limpeza da área dos funcionários", 800)
        self.add(cargo1)
        self.add(cargo2)
        self.add(cargo3)

    def add(self, cargo: Cargo):
        if((cargo is not None) and isinstance(cargo, Cargo) and isinstance(cargo.titulo, str)):
            super().add(cargo.titulo, cargo)

    def update(self, cargo: Cargo):
        if((cargo is not None) and isinstance(cargo, Cargo) and isinstance(cargo.titulo, str)):
            super().update(cargo.titulo, cargo)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)