import csv  # importamos la funcionalidad csv de python


def read_csv(path):  # declaramos la función que leera el csv
    # mediante un bucle with abrimos la ruta (path) con permisos de lectura ('r') como la variable "csvfile"
    with open(path, 'r') as csvfile:
        # dentro del buble la variable "reader" llamara a la función csv.reader
        # el cual recibira por parametro la data del csv con una comma (,) como delimitador
        reader = csv.reader(csvfile, delimiter=',')
        # dentro del ciclo with se incluira un ciclo for para iterar cada fila (row) del csv
        for row in reader:
            # imprimira una secuancia de numeros para separar visualmente las filas
            print('....' * 5)
            print(row)  # imprimiremos por consola las filas


if __name__ == '__main__':  # control de ejcución de funciones y dualidad en el llamado
    # al ser llamada la funsión se ejecutara con la ruta del csv espesificada
    read_csv('./data.csv')
