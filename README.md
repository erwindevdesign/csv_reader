# Handling a Comma-Separated Values (CSV) data table. :bar_chart:

*en*. Creating an application for manipulating data tables in **CSV** format.

*es*. Creación de una aplicación para manipular tablas de datos en formato **CSV**.

## step by step

> #!/usr/bin/env python3

1. Working Directory
* *en*. Create a working directory for hostign the application.
* *es*. Crear un directorio de trabajo para alojar la aplicación.

~~~sh
# in console
❯ mkdir csv
~~~

2. Change a working directory.
* *en*. From the **terminal**, change the current working directory to your local project.
* *es*. Desde la **terminal**, cambie el directorio de trabajo actual a su proyecto local.

~~~sh
# 01 in console
❯ cd csv
~~~
~~~sh
# 02 in console
❯ pwd
~~~
~~~sh
# return
!./csv
~~~

3. Environment
* *en*. Create a virtual environment in the current working directory for managing projects with different dependencies, installing the Python packages and libraries.
* *es*. Crear un entorno virtual en el directorio de trabajo actual para administrar projctos con diferentes dependencies, installisn the Python packages and libraries.

~~~sh
# in console to create venv
❯ python3 -m venv env
~~~

4. **venv:** activate  / deactivate
* *en*. To activate the virtual environment, run the command:
* *es*. Para activar el entorno virtual, ejecute el comando:

~~~sh
# in console to activate venv
❯ source env/bin/activate
~~~

* *en*. To deactivate the virtual environment, run the command:
* *es*. Para desactivar el entorno virtual, ejecute el comando:

~~~sh
# in console to deactivate venv
❯ deactivate
~~~

5. Where is it currently running from?
* *en*. To test the virtual environment, we'll check the current locations of the **python3** and **pip** executables.
* *es*. Para probar el entorno virtual, verificaremos las ubicaciones actuales de los ejecutables **python3** y **pip3**.

~~~sh
# 01 in console
❯ which python3
~~~
~~~sh
# return
./csv/env/bin/python3
~~~
~~~sh
# 02 in console
❯ which pip3
~~~
~~~sh
# return 
./csv/env/bin/pip3
~~~

6. Dependencies.
* *en*. Install the dependencies required for the execution of the application.
* *es*. Instalar las dependencias requeridas para la ejecición de la aplicación.

~~~sh
# in cosole
❯ pip3 install matplotlib
~~~

7. Check Dependencies.
* *en*. To verify the installed dependencies, run the following command:
* *es*. Para verificar las dependencias instaladas ejecute el siguiente comando:

~~~sh
# in console
❯ pip3 freeze
~~~
~~~sh
# return
contourpy==1.0.7
cycler==0.11.0
fonttools==4.38.0
kiwisolver==1.4.4
matplotlib==3.7.0
numpy==1.24.2
packaging==23.0
Pillow==9.4.0
pyparsing==3.0.9
python-dateutil==2.8.2
six==1.16.0
~~~
8. Requirements File.
* *en*. Create a **requirements.txt** file for future installations
* *es*. Crear un archivo **requirements.txt** para futuras instalaciones.

~~~sh
# in console create the file to contain
❯ touch requirements.txt 

# send to plain text a file
❯ pip3 freeze > requirements.txt 

# review file content
❯ cat requirements.txt
~~~
~~~sh
# return
contourpy==1.0.7
cycler==0.11.0
fonttools==4.38.0
kiwisolver==1.4.4
matplotlib==3.7.0
numpy==1.24.2
packaging==23.0
Pillow==9.4.0
pyparsing==3.0.9
python-dateutil==2.8.2
six==1.16.0
~~~
~~~sh
# to install the dependencies from requirements.txt when downloading the project.

❯ pip3 install -r requirements.txt
~~~

9. (**.gitignore**) File.
* *en*. Create a **.gitignore** file to ignore specific files and prevent them from being tracked.
* *es*. Crear un archivo **.gitignore** para ignorar archivos espesificos y evitar que sean rastreados.

~~~py
# in console
❯ touch .gitignore
~~~

> Copy and paste plane text from in .gitignore file: https://www.toptal.com/developers/gitignore/ 

>   Created by: https://www.toptal.com/developers/gitignore/api/windows,macos,android,linux,python

>   Edit at: https://www.toptal.com/developers/gitignore?templates=windows,macos,android,linux,python


10. Create and import modules.
* *en*. In the working directory create **utils.py** and **main.py** files to define functions.
* *es*. Eb el directorio de trabajo, crear archivos **utils.py** y **main.py** para definir funsiones.
~~~sh
# in console create utils.py file
❯ touch utils.py
~~~
~~~py
# in utils.py file we define the function (get_population). 
def get_population(): 
    """ Returns test data in the form of keys and values.

    Returns:
        1. keys (list): A list of keys for testing.
        2. values (list): A list of values for testing. 

    """
    keys = ['a', 'b', 'c']
    values = [1,2,3]
    
    return keys, values
~~~
~~~sh
# in console create main.py file
❯ touch main.py
~~~
~~~py
# in main.py file import the utils module in main. 
import utils 
# call the function from utils.
keys, values = utils.get_population() 
# display the values returned by the function. 
print(keys, values ) 
~~~
~~~sh
# in console call the main file.
❯ python3 main.py 
~~~
~~~sh
# returned testing keys and values
['a', 'b', 'c'] [1, 2, 3] 
~~~
11. Modularization
* *en*. We modularized the application by using import statements, which enable communication between modules. For example, in **utils.py** we defined functions that are imported into **main.py** to return tuples from a csv file. 
* *es*. Modularisamos la aplicación mediante el uso de sentencias de importación, que permiten la comunicación entre módulos. Por ejemplo, en **utils.py** definimos funciones que se importarán a **main.py** para retornar tuplas desde un archivo csv.
~~~py
# in utils.py file we define the function (populatión_by_country). 
def get_population(): 
    keys = ['a', 'b', 'c']
    values = [1,2,3]
    return keys, values

def populatión_by_country(data, country):
    """ 
    
    """
    result = list(filter(lambda item: item ['Country'] == country, data))
    return result

~~~
~~~py
# in main.py file import the utils module in main. 
import utils 
# call the function from utils.
keys, values = utils.get_population() 
# display the values returned by the function. 
print(keys, values ) 
~~~
~~~sh
# in console call the main file.
❯ python3 main.py 
~~~
~~~sh
# returned testing keys and values
['a', 'b', 'c'] [1, 2, 3] 
~~~




12. Data source.
* *en*. We import the CSV file into working directory with a descritive name to by called by the console.
* *es*. Importamos el archivo CSV al directorio de trabajo con un nombre descriptivo oara ser llamado por consola.  

![Imgur](https://i.imgur.com/Ai9eI5c.png)
![Imgur](https://i.imgur.com/0VAjHpN.png)

~~~py
""" This script reads data from a CSV file and generates visualizations of the data using matplotlib library.

Usage:

    To run the script, use the following command in the terminal:

        $ python3 main.py [type_chart] [continent] [path] <-- 

Parameters:

    1. type_chart (str): The type of chart to generate. Possible values are "bar" or "pie".
    2. continent (str): The region to filter the data by. Possible values are "Asia", "Europe", "Africa", "North\ America", "South\ America" or "Oceania".
    3. path (str): The path to the CSV file containing the data.

        csv_reader = reader(iterable [, dialect='excel']
        
        [optional keyword args])
        
        for row in csv_reader:
            process(row)

Example:

    $ python3 main.py bar Asia ./data.csv <--

    $ python3 main.py bar North\ America ./data.csv <--

"""
~~~




12. Reader Function
* *en*. Create a function in a module to import **csv** functionality native and read a **CSV** type file.
* *es*. Crear una función en un módulo para importar la funcionalidad nativa **csv** y leer un archivo de tipo **CSV**.
~~~sh
# in console create a file to hold the read function.
❯ touch read_csv.py 
~~~
~~~py
# in read_csv.py file import csv functionality native from python import csv. 
import csv 

# we define the function (read_csv). 
def read_csv(path):
    """ Reads a CSV file and prints each row.

    Args:
        1. path (str): The path to the CSV file.
        2. mode (str): The mode in the which the file is opened. Default value is 'r'
        3. Delimiter (str): A one-character string used to separated fields.Default value is ','
        
    Returns: 
        1. reader (process): The returned object is an iterator.
    
    Raises:
        1. FileNotFoundError: If the specified file does not exist.
        2. TypeError: If the CSV file is empty or if the delimiter is not valid.
    """
    
    # Open file and return a stream. Raise "FileNotFoundError" upon failure.
    # We open the CSV file and read its content with the csv module
    # using the with structure to ensure that the file
    # closes automatically after use.
    # Save the data {object} from csv file in reader variable.
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') 

        # loop for printing the data from reader function in console.
        # We iterate over each roe of the CSV file and perform
        # Operation on the data.
        for row in reader:
            # Printng the row separated visually with 
            # a string of dots through a "for" loop.
            print('....' * 5)
            print(row)     

# Entry Point: "duality"
# This section checks if the current 
# script is being executed as the main 
# program and calls the 'read_csv' 
# function with the path to the CSV 
# file as an argument.
if __name__ == '__main__': 
    read_csv('./data.csv') # path to the CSV file as an argument
~~~






13. **read_csv.py** Module.
* *en*. Modify the function to read a **CSV** file and transform its contents into a **dictionary**.
* *es*. Modifique la función para leer un archivo **CSV** y transformar su contenido en un **diccionario**.

~~~py
# in read_csv.py file refactorized a funtion and transform the content into a dictionary.
import csv 

 
def read_csv(path):
    """ Reads a CSV file and prints each row.

    Args:
    -----
        1. path (str): The path to the CSV file.
        2. mode (str): The mode in the which the file is opened. Default value is 'r'
        3. Delimiter (str): A one-character string used to separated fields.Default value is ','
        
    Returns: 
        
        1. reader (process): The 'reader' (variable) is an iterator containing the CSV file data, which is returned to the console using the 'print' function.
    
    Raises:
    -------
        1. FileNotFoundError: If the specified file does not exist.
        2. TypeError: If the CSV file is empty or if the delimiter is not valid.
    """
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') 

        # Create a variable that stores the fist 
        # element of the iterator, witch will be 
        # used as a header to initialize a dictionary.
        header = next(reader)
        data = [] 

        for row in reader:

            # Modulate the for loop to recive the header 
            # variable and row from the reader as parameter.
            # The zip() function takes iterables, aggregates them in a tuple, and return it. The number of iterables passed as positional arguments to zip() is the length of the tuples it yields. 
            # We make use of a "dictionary comprehension" 
            # to convert the tuples into a dictionary and rstore it in the "data" dictionary. 
            iter = zip(header, row) 
            country_dict = {key: value for key, value in iter} # dictionary comprehension
            data.append(country_dict)   

        return data

if __name__ == '__main__': 
    read_csv('./data.csv') 
    # The "data" dictionary is returned in the console with its contents displayed in various positions withing square brackets [ ].
    print(data[0]) 
~~~

13. **charts.py** Module.
* *en*. Define the function to create **charts** in a new module.
* *es*. Define la función para crear **gráficas** en un nuevo módulo.
~~~sh
# in console create charts.py file
❯ touch charts.py
~~~
~~~py
# In the charts.py file, we import the "matplotlib" library
# and the "pyplot" module to create a chart. 

import matplotlib.pyplot as plot 

def generate_bar_chart(labels, values):
    """ Generates a bar chart using the provided labels and values.

    Parameters:
        labels (list): A list of labels for the x-axis.
        values (list): A list of values for the y-axis.

    Returns:
        None. Displays the generated chart using pyplot.show().

    Example:
        >>> generate_bar_chart(['Jan', 'Feb', 'Mar'], [100, 200, 150])
    """
    fig, ax = plot.subplots()
    ax.bar(labels, values)
    plot.show()

def generate_pie_chart(labels, values):
    """
    Generates a pie chart using the provided labels and values.

    Parameters:
        labels (list): A list of labels for the different sections of the chart.
        values (list): A list of values representing the size of each section.

    Returns:
        None. Displays the generated chart using pyplot.show().

    Example:
        >>> generate_pie_chart(['Apple', 'Banana', 'Orange'], [20, 30, 50])
    """
    fig, ax = plot.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plot.show()

if __name__ == '__main__':
    # Example usage
    generate_pie_chart(['Asia', 'Europe', 'Africa', 'Americas', 'Oceania'], [59.69, 22.05, 17.21, 13.48, 0.52])
    generate_bar_chart(['Jan', 'Feb', 'Mar'], [100, 200, 150])   
~~~











14. Refactorized **utils.py**.

* *en*. Refactorized the **get_population** function in utils.py to accept a dictionary from a **CSV** file.
* *es*. Refactorized la dunción **get_population** en utils.py para aceptar un diccionario desde un archivo **CSV**.

~~~py
# before utils.py file we define the function (get_population). 
def get_population(): 
    """ Returns test data in the form of keys and values.

    Returns:
        1. keys (list): A list of keys for testing.
        2. values (list): A list of values for testing. 

    """
    keys = ['a', 'b', 'c']
    values = [1,2,3]
    
    return keys, values
~~~
~~~py
# after utils.py file

def get_population(country_dict): 

    """ Extracts the population data for a given country from a dictionary and returns it as a tuple of labels and values.

    Parameters:
        - country_dict (dict): A dictionary containing the population data for a single country, with keys representing years and values representing population.

    Returns:
        A tuple containing two lists: labels and values. Labels contains the year labels for the x-axis, and values contains the population values for the y-axis.

    Example:
        >>> country_data = {'2022 Population': '5000000', '2020 Population': '4800000', '2015 Population': '4500000'}
        >>> get_population(country_data)
        (['2022', '2020', '2015'], [5000000, 4800000, 4500000])
    """
    population_dict = { 
        '2022': int(country_dict['2022 Population']),
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])
    }

    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values

def population_by_country(data, country):
    """ Searches a list of dictionaries containing population data for a specific country and returns the data for that country as a list.

    Parameters:
        - data (list): A list of dictionaries containing population data for various countries.
        - country (str): The name of the country to search for.

    Returns:
        A list containing the population data for the specified country.

    Example:
        >>> data = [{'Country': 'Canada', '2022 Population': '38000000', '2020 Population': '37000000'}, {'Country': 'Mexico', '2022 Population': '133000000', '2020 Population': '129000000'}]
        >>> population_by_country(data, 'Canada')
        [{'Country': 'Canada', '2022 Population': '38000000', '2020 Population': '37000000'}]
    """
    result = list(filter(lambda item: item['Country'] == country, data))
    return result
~~~

15. Refactorized main.py 

* *en*. Refactorized **main.py** to import the created modules.
* *es*. Refactorized **main.py** para importar los módulos creados.

~~~py
# before main.py file

import utils  

def run(): 
    keys, values = utils.get_list()  
    print(keys, values)
    country = input('Type country item: ')
    result = utils.population_by_country(data, country)
    print(result)

if __name__ == '__main__': 
    run()
~~~country item: ')
    result = utils.population_by_country(data, country)
    print(result)

if __name__ == '__main__': 
    run()
~~~
~~~py
# after main.py file

import utils  
import read_csv 
import charts 

def run(): 
    # dictionary from read.csv.py
    data = read_csv.read_csv('./data.csv') # 
    
    # -- Bar Chart -- 
    country = input('Type country item: ') # tracked input
    result = utils.population_by_country(data, country) 
    if len(result) > 0:
        country = result[0] 
        labels, values = utils.get_population(country)  
        charts.generate_bar_chart(labels, values)
      
if __name__ == '__main__': 
    run()
~~~


16. Modify the **run()** function.

* *en*. Modify the **run()** function in **main.py** to create a pie chart using information from a CSV file.
* *es*. Modifique la función **run()** en **main.py** para crear un gráfico circular usando información de un archivo CSV.

~~~py
# before main.py file

import utils  
import read_csv 
import charts 

def run(): 
    # dictionary from read.csv.py
    data = read_csv.read_csv('./data.csv') # 
    
    # -- Bar Chart -- 
    country = input('Type country item: ') # tracked input
    result = utils.population_by_country(data, country) 
    if len(result) > 0:
        country = result[0] 
        labels, values = utils.get_population(country)  
        charts.generate_bar_chart(labels, values)
      
if __name__ == '__main__': 
    run()
~~~
~~~py
# after main.py file
 
import read_csv 
import charts 

def run(): 
    data = read_csv.read_csv('./data.csv') 
    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)
    
if __name__ == '__main__': 
    run()
~~~














~~~py
# main.py


~~~
~~~py
# utils.py

~~~

~~~py
# read_csv.py


~~~

~~~py
# charts.py


~~~


<!-- 

* *en*.
* *es*.

 -->