import csv  # importamos la funcionalidad csv de python


def read_csv(path):  # declaramos la función que leera el csv
    # mediante un bucle with abrimos la ruta (path) con permisos de lectura ('r') como la variable "csvfile"
    with open(path, 'r') as csvfile:
        # dentro del buble la variable "reader" llamara a la función csv.reader
        # el cual recibira por parametro la data del csv con una comma (,) como delimitador
        reader = csv.reader(csvfile, delimiter=',')

        # se crea una variable que almacene la primera fila de la data que representa la cabecera de las comlumnas dentro del CSV
        header = next(reader)
        # imprimimos por pantalla lo almacenado en la variable "header"
        # print(header)
        data = [] # se crea una variable en blanco
        # dentro del ciclo with se incluira un ciclo for para iterar cada fila (row) del csv
        for row in reader:

            # utiliaremos la función zip para unir el array con los headers de columnas y el array con el contenido del CSV
            iter = zip(header, row)
            
            ## print(list(iter)) # imprimimos por consola las tuplas construidas con el zip
            
            # contruimos un dict-comprehensions con los valores creados en las tuplas del zip
            country_dict = {key: value for key, value in iter}
            data.append(country_dict) # agregamos a la variable data el resultado del dict-comprehension

        return data 

"""    
            # imprimira una secuancia de numeros para separar visualmente las filas
            print('....' * 5)
            print(row)  # imprimiremos por consola las filas
            """


if __name__ == '__main__':  # control de ejcución de funciones y dualidad en el llamado
    # al ser llamada la funsión se ejecutara con la ruta del csv espesificada
    data = read_csv('./data.csv')
    print(data[1])
