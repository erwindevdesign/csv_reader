def get_population(country_dict):  # definimos la función que recibe los valores creados en read.py 
    population_dict = { 
        # creamos la variable del diccionaryo con los valores que la grafica recibirá
        # recibe como llave los años con los que se definirán en la gráfica
        # y los valores que recibe de las columnas descritas en el CSV
        '2022': int(country_dict['2022 Population']),
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])
    }

    # extraemos como labels las keyś
    # y los valores como values

    labels = population_dict.keys()
    values = population_dict.values()
    # retornamos estos valores para utilizar a lo largo de la vida de la aplicación
    return labels, values


# creamos la función para llamar la población por ciudad desde main.py
# función recibira el csv como objeto y trakeara el dato tipeado
def population_by_country(data, country):
    # search for ['Country'] in the header row
    result = list(filter(lambda item: item['Country'] == country, data))
    return result
