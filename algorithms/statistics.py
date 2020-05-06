import random


def media(lista):
     return sum(lista) / len(lista)

def varianza(lista):
    x_varianza = 0
    for numero in lista:
        x_varianza += (numero - media(lista)) ** 2
    return round(x_varianza / len(lista), 2)

def desviacion(lista):
    return round(varianza(lista) ** 0.5, 2)


if __name__ == '__main__':
    lista = [random.randint(0, 20) for _ in range(20)]
    X = lista

    print(f'{X}')
    print(f'Media: \t\t{media(X)}')
    print(f'Varianza: \t{varianza(X)}')
    print(f'Desviacion: \t{desviacion(X)}')