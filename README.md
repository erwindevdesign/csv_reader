# Handling a comma-separated values (CSV) data table. 

:bar_chart:

*en*. Creating an application for manipulating data tables in  **CSV** format.

*es*. Creación de una aplicación para manipular tablas de datos en formato **CSV**.

## step by step

1. Working Directory
* *en*. Create a working directory for hostign the application.
* *es*. Crear un directorio de trabajo para alojar la aplicación.

~~~sh
# in cosole
❯ mkdir csv
~~~

2. Chenge Local Project
* *en*. From the **terminal**, change the current working directory to your local project.
* *es*. Desde la **terminal**, cambie el directorio de trabajo actual a su proyecto local.

~~~sh
# in cosole
❯ cd csv

❯ pwd
./csv
~~~

virtualenv

3. Environment
* *en*. Create a virtual environment in the current working directory.
* *es*. Crear un entorno virtual en el directorio de trabajo actual.

~~~sh
# in cosole
❯ python3 -m venv env
~~~

4. env ON
* *en*. To activate the virtual environment, run the command:
* *es*. Para activar el entorno virtual, ejecute el comando:

~~~sh
# in cosole
❯ source env/bin/activate
~~~

5. Where is it currently running from?
* *en*. To test the virtual environment, we'll check  the current locations of the **python3** and **pip** executables.
* *es*. Para probar el entorno virtual, verificaremos dónde las ubicaciones actuales de los ejecutables **python3** y **pip3**.

~~~sh
# in cosole
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
# in cosole
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
# in cosole
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

9. Gitignore File.
* *en*. Create a **.gitignore** file to ignore specific files and prevent them from being tracked.
* *es*. Crear un archivo **gitignore para ignorar archivos espesificos y evitar que sean rastreados.

~~~py
# in cosole
❯ mkdir gitignore

# copy and paste plane text from https://www.toptal.com/developers/gitignore/ in gitignore file.
# Created by https://www.toptal.com/developers/gitignore/api/windows,macos,android,linux,python
# Edit at https://www.toptal.com/developers/gitignore?templates=windows,macos,android,linux,python
~~~


10. Modularization
* *en*. We modularized the application by using import statements to allow communication between modules. For example, in **main.py** we imported functions from **utils.py**. 
* *es*. Modularisamos la aplicación utilizando sentencias de importación para permitir la comunicación entre módulos. Por ejemplo, en **main.py** importamos funciones de **utils.py**.

~~~py
# in main.py file 
import utils # importamos desde el módulos utils

keys, values = utils.get_population()
print(keys, values )

~~~
~~~py
# in utils.py file
def get_population():
    keys = ['a', 'b', 'c']
    values = [1,2,3]
    return keys, values
~~~
~~~sh
# in cosole
❯ python3 main.py

['a', 'b', 'c'] [1, 2, 3]
~~~

11. Reader Function
* *en*. Create a function in a module to read a **CSV** file.
* *es*. Crear una función en un módulo para leer un archivo **CSV**.

~~~py
# in read_csv.py file

import csv  

def read_csv(path):  
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

import matplotlib.pyplot as plot 

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
    generate_bar_chart(labels, values)
    #generate_pie_chart(labels, values)


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