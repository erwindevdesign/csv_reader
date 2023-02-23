# Handling a comma-separated values (CSV) data table. 

:bar_chart:

*en*. Creating an application for manipulating data tables in **CSV** format.

*es*. Creación de una aplicación para manipular tablas de datos en formato **CSV**.

## step by step

1. Working Directory
* *en*. Create a working directory for hostign the application.
* *es*. Crear un directorio de trabajo para alojar la aplicación.

~~~sh
# in console
❯ mkdir csv
~~~

2. Chenge Local Project
* *en*. From the **terminal**, change the current working directory to your local project.
* *es*. Desde la **terminal**, cambie el directorio de trabajo actual a su proyecto local.

~~~sh
# in console
❯ cd csv

❯ pwd
./csv
~~~

virtualenv

3. Environment
* *en*. Create a virtual environment in the current working directory.
* *es*. Crear un entorno virtual en el directorio de trabajo actual.

~~~sh
# in console
❯ python3 -m venv env
~~~

4. env ON
* *en*. To activate the virtual environment, run the command:
* *es*. Para activar el entorno virtual, ejecute el comando:

~~~sh
# in console
❯ source env/bin/activate
~~~

5. Where is it currently running from?
* *en*. To test the virtual environment, we'll check  the current locations of the **python3** and **pip** executables.
* *es*. Para probar el entorno virtual, verificaremos dónde las ubicaciones actuales de los ejecutables **python3** y **pip3**.

~~~sh
# in console
❯ which python3
./csv/env/bin/python3

❯ which pip3
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
# in console
❯ touch requirements.txt

❯ pip3 freeze > requirements.txt

❯ cat requirements.txt
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

9. (**.gitignore**) File.
* *en*. Create a **.gitignore** file to ignore specific files and prevent them from being tracked.
* *es*. Crear un archivo **.gitignore** para ignorar archivos espesificos y evitar que sean rastreados.

~~~py
# in console
❯ touch .gitignore

# copy and paste plane text from:
# https://www.toptal.com/developers/gitignore/ 
# in .gitignore file.

# Created by:
# https://www.toptal.com/developers/gitignore/api/windows,macos,android,linux,python

# Edit at:
# https://www.toptal.com/developers/gitignore?templates=windows,macos,android,linux,python
~~~

10. Modularization
* *en*. We modularized the application by using import statements to allow communication between modules. For example, in **main.py** we imported functions from **utils.py**. 
* *es*. Modularisamos la aplicación utilizando sentencias de importación para permitir la comunicación entre módulos. Por ejemplo, en **main.py** importamos funciones de **utils.py**.

~~~py
# in utils.py file

def get_population(): # 01 we define the function (get_population).
    
    """ Function that receives keys and values in list format.
    Args: 
        None

    Returns:
        keys [list]: A list of keys for testing
        values [list]: A list of values for testing 
    """ # 02 we document the functionallity.    
    
    keys = ['a', 'b', 'c'] # 03 Define tester keys.
    values = [1,2,3] # 04 Define tester values.
    
    return keys, values # 05 return tester values.
~~~
~~~py
# in main.py file 

import utils # 01 import the utils module in main. 

keys, values = utils.get_population() # 02 call the function from utils.

print(keys, values ) # 03 display the values returned by the function.
~~~
~~~sh
# in console

❯ python3 main.py # 01 call the main file in console.

['a', 'b', 'c'] [1, 2, 3] 
~~~

11. Reader Function
* *en*. Create a function in a module to read a **CSV** file.
* *es*. Crear una función en un módulo para leer un archivo **CSV**.

~~~sh
# in the working directory, create a file to hold the read function.
❯ touch read_csv.py 
~~~

~~~py
# in read_csv.py file

import csv # 01 import csv functionality native from python

def read_csv(path):  
    """ 
    Args:
    path []

    Returns:
    """ # 02 we document the functionallity. 
    with open(path, 'r') as csvfile:  
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print('....' * 5)
            print(row) 


if __name__ == '__main__': 
    read_csv('./data.csv')
~~~

12. **read_csv.py** Module.
* *en*. Modify the function to read a **CSV** file and transform its contents into a **dictionary**.
* *es*. Modifique la función para leer un archivo **CSV** y transformar su contenido en un **diccionario**.

~~~py
# in read_csv.py file

import csv  

def read_csv(path):  
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)

        data = [] 
        
        for row in reader:
            iter = zip(header, row) # zip - union to tuples
            country_dict = {key: value for key, value in iter} # dictionary comprehension
            data.append(country_dict)
        
        return data

if __name__ == '__main__':  
    data = read_csv('./data.csv') # CSV file rute
    print(data[0]) # call to index 0 
~~~

13. **charts.py** Module.
* *en*. Define a function to create **charts**.
* *es*. Define una función para crear gráficas.

~~~py
# in charts.py file

import matplotlib.pyplot as plot # functionality from matplotlib

def generate_bar_chart(labels, values):
    fig, ax = plot.subplots()
    ax.bar(labels, values)
    plot.show()

def generate_pie_chart(labels, values):
    fig, ax = plot.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plot.show()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [25,80,190]
    generate_bar_chart(labels, values) # function to bar chart
    # generate_pie_chart(labels, values) # (uncoment) function to pie chart 
~~~

14. Refactorized **utils.py**.

* *en*. Restructure the **get_population** function in utils.py to accept a dictionary from a **CSV** file.
* *es*. Reestructure la dunción **get_population** en utils.py para aceptar un diccionario desde un archivo **CSV**.

~~~py
# before utils.py file

def get_population(): 
    keys = ['a', 'b', 'c'] # tester keys
    values = [1,2,3] # tester values
    return keys, values
~~~
~~~py
# after utils.py file

def get_population(country_dict): 
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
    # search for ['Country'] in the header row
    result = list(filter(lambda item: item['Country'] == country, data))
    return result
~~~

15. Restructure main.py 

* *en*. Restructure **main.py** to import the created modules.
* *es*. Reestructura **main.py** para importar los módulos creados.

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


<!-- 
https://www.kaggle.com 
- data in csv format -
 -->