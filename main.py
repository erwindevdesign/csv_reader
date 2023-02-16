import utils  # importamos desde el módulos utils
import read_csv # importamos desde el modulo read_csv
import charts # importamos desde el módulo charts

def run(): # creamor la funsión que ejecute el llamado a la fución con dualidad

    # obtenemos la data en formato de diccionario
    data = read_csv.read_csv('./data.csv') # desde el módulo read_csv importamos la funcionalidad read_csv
    
    # filter by continent
    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    
    # pie chart
    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)
    
    """ 
    # bar chart
    country = input('Type country item: ') # entrada de parametro de busqueda
    
    result = utils.population_by_country(data, country) # variable que almacena los parametros retornados por utils.py


    if len(result) > 0:
        country = result[0] 
        labels, values = utils.get_population(country)  # llamamos a la función desde utils.py
        # una vez retornaron los valores de la función imprimos sus valores por consola
        charts.generate_bar_chart(labels, values)
        #charts.generate_pie_chart(labels, values)

 """
if __name__ == '__main__': # control de ejcución de funciones y dualidad en el llamado
    run()
