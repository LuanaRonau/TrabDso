from ABC import abstractmethod

class Telas(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mostra_mensagem(self, mensagem):
        print(mensagem)


