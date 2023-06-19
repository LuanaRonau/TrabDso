from dao.list_dao import ListDAO
from entidade.promocao import Promocao


class PromocaoDAO(ListDAO):
    def __init__(self):
        super().__init__('promocoes.pkl')

    def add(self, promocao: Promocao):
        if((promocao is not None) and isinstance(promocao, Promocao)):
            if len(super().cache) == 0:
                super().add(0, promocao)
            else:
                for indice in range(len(super().cache)):
                    if super().cache[indice].data < promocao.data:
                        super().add(indice, promocao)
                        return

    def update(self, cpf: str, promocao: Promocao):
        if((promocao is not None) and isinstance(promocao, Promocao) and isinstance(cpf, str)):
            for indice in range(len(super().cache)):
                if super().cache[indice].empregado.cpf is cpf:
                    super().update(indice, promocao)
                    return

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)