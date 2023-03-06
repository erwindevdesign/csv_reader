import csv 


def read_csv(path): 

    """ Reads a CSV file and prints each row.
    ========================================
    Args:
    -----
        1. path (str): The path to the CSV file.
        2. mode (str): The mode in the which the file is opened. Default value is 'r'
        3. Delimiter (str): A one-character string used to separated fields. Default value is ',' 
    
    Returns: 
    --------
        1. reader (print): The 'reader' (variable) is an iterator containing the CSV file data, which is printed to the console using the 'print' function.

    Raises:
    -------
        1. FileNotFoundError: If the specified file does not exist.
        
        2. TypeError: If the CSV file is empty or if the delimiter is not valid.
    """
    # business rule: 
    try :
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

            return data # retornamos lo almacenado en "data"
    except FileNotFoundError as err:
        raise FileNotFoundError(f'\n{err}; The file {path} does not exist <--')
        #error_msg = (f'{err}: \nThe file {path} does not exist <--')
        #print(error_msg)


if __name__ == '__main__':  
    data = read_csv('./data.csv')
    print(data[0])
