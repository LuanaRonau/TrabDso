from datetime import datetime, date

data = input("data no formato ...: ")

#dia, mes, ano = teclado.split("/")

def verifica_data_valida(data: str):
    while True:
        try:
            data = datetime.strptime(data, "%d/%m/%Y").date()
            if (date.today() < data):
                raise ValueError
            return data
        except ValueError:
            print("Data incorreta ou fora do formato desejado [dia/mes/ano]: ")
            data = input("Digite a data novamente: (exemplo: 14/04/2023) ")


print(verifica_data_valida(data))