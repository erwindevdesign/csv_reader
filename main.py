import utils  # importamos desde el módulos utils

def run(): # creamor la funsión que ejecute el llamado a la fución con dualidad
    keys, values = utils.get_list()  # llamamos a la fución desde utils.py
    # una vez retornaron los valores de la función imprimos sus valores por consola
    print(keys, values)

    country = input('Type country item: ')

    result = utils.population_by_country(data, country)
    print(result)

if __name__ == '__main__': # control de ejcución de funciones y dualidad en el llamado
    run()
