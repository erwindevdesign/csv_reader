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
* *en*. Create a **gitignore** file for it should ignore certain files and not track them.
* *es*. Crear un archivo **gitignore para que ignore ciertos archivos y no los rastree.

~~~py
# in cosole
❯ mkdir gitignore

# copy and paste plane text from https://www.toptal.com/developers/gitignore/ in gitignore file.
# Created by https://www.toptal.com/developers/gitignore/api/windows,macos,android,linux,python
# Edit at https://www.toptal.com/developers/gitignore?templates=windows,macos,android,linux,python
~~~


10. Modularization
* *en*. We modularized the application, with modules communicating from **main.py** to **utils.py** via an **import** statement in **main**. 
* *es*. Modularisamos la aplicación, con módulos que se comunican desde **main.py** a **utils.py** a travéz de una declaración **import** en **main**.

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



~~~sh
# main.py


~~~
~~~sh
# utils.py

~~~

<!-- 
* *en*.
* *es*.


* *en*.
* *es*.
 -->


<!-- 
https://www.kaggle.com 
- data in csv format -
 -->