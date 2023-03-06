#!/usr/bin/env python3

""" 
Handling a CSV data table
=========================
Description: Create the application for manipulating data tables in CSV format.
--------------------------------------------------------------------------------
This script reads data from a CSV file and generates visualizations of the data using matplotlib library.
---------------------------------------------------------------------------------------------------------
Author: Erwin Francisco Sanchez Vargas.
---------------------------------------
Email: erwindevdesign@infinitummail.com
--------------------------------------- 
Date: 23-02-2023 (ddmmaaaa).
----------------------------

Version:
--------
    v0.0.1

Usage:
------
    $ python3 main.py [parameter] [parameter] [path]

    $ python3 main.py [type_chart] [continent] [path]

    $ python3 main.py [-h] [--version] [-v] type_chart continent path

Options:
--------



Example:
--------

To run the app with bar chart:

    $ python3 main.py bar Asia ./data.csv

    $ Type country item: 


https://www.kaggle.com  - data in csv format -

"""


import utils  # importamos desde el módulos utils
import read_csv # importamos desde el modulo read_csv
import charts # importamos desde el módulo charts
import argparse

parser = argparse.ArgumentParser(description='Select Type Chart, Continent, Country* & file path')
parser.add_argument('type_chart', type=str, help='Select a type chart')
parser.add_argument('continent', type=str, help='Enter the search continent')
parser.add_argument('path', type=str, help='Enter the file path')
#parser.add_argument('--version', action='version', version='%(prog)s v0.0.1')
parser.add_argument('--version', action='version', version='v0.0.1')
parser.add_argument('-v','--verbose', action='store_true', help='Verbose mode')




def run(): # creamor la funsión que ejecute el llamado a la fución con dualidad
    try:
        # print('Select a continent: ')
        # print('Africa | Asia | Europe | North America | Oceania | South America')


        # parser = argparse.ArgumentParser(description='Select Continent & Country')
        # parser.add_argument('continent', type=str, help='Enter the search continent')
        # parser.add_argument('path', type=str, help='Enter the file path')

        # args = parser.parse_args()

        # obtenemos la data en formato de diccionario
        # data = read_csv.read_csv('./data.csv') # desde el módulo read_csv importamos la funcionalidad read_csv

        data = read_csv.read_csv(args.path) # desde el módulo read_csv importamos la funcionalidad read_csv


        # filter by continent
        data = list(filter(lambda item: item['Continent'] == args.continent, data))

        if args.type_chart == 'pie':

            # pie chart
            countries = list(map(lambda x: x['Country'], data))
            percentages = list(map(lambda x: x['World Population Percentage'], data))
            charts.generate_pie_chart(countries, percentages)

        elif args.type_chart == 'bar':

            # bar chart
            country = input('Type country item: ') # entrada de parametro de busqueda

            result = utils.population_by_country(data, country) # variable que almacena los parametros retornados por utils.py


            if len(result) > 0:
                country = result[0] 
                labels, values = utils.get_population(country)  # llamamos a la función desde utils.py
                # una vez retornaron los valores de la función imprimos sus valores por consola
                charts.generate_bar_chart(labels, values)
                #charts.generate_pie_chart(labels, values)

    except TypeError as terr:
        raise TypeError(f'{terr}; does not exist <--')    
        # error_msg = (f'{terr}:  does not exist data type <--')
        # print(error_msg)

args = parser.parse_args()

if __name__ == '__main__': # control de ejcución de funciones y dualidad en el llamado
    run()
