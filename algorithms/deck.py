import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10', '11', '12', '13']

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        i = 0
        j = 0
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k +=1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista

def crear_baraja():
	barajas = []
	for palo in PALOS:
		for valor in VALORES:
			barajas.append((palo, valor))

	return barajas

def obtener_mano(barajas, tamano_mano):
	mano = random.sample(barajas, tamano_mano)

	print(mano)

	return mano

def main(tamano_mano, intentos):
	barajas = crear_baraja()

	manos = []
	for _ in range(intentos):
		mano = obtener_mano(barajas, tamano_mano)

		manos.append(mano)

	corridas = 0
	puntero = mano[0]
	for mano in manos:
		counter = 0
		valores = []

		for i in range(5):
			counter += 1
			palo = mano[i]
			valores.append(palo[1])
			if palo[0] != puntero[0]:
				break

		if counter == 5:
			lista_ord = ordenamiento_por_mezcla(valores)

			band = 0
			for j in range(4):
				valor = lista_ord[j]
				if (int(valor)+1) != int(lista_ord[j+1]):
					band = 1
					break

			if band == 0:
				corridas += 1

	probabilidad_corrida = corridas / intentos
	print(f'La probabilidad de obtener una corrida en una mano {tamano_mano} barajas es {probabilidad_corrida}')

if __name__ == '__main__':
	tamano_mano = int(input('De cuantas barajas sera la mano: '))
	intentos = int(input('Cuantos intentos para calcular la probabilidad: '))

	main(tamano_mano, intentos)