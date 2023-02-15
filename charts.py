import matplotlib.pyplot as plot # importamos la dependencia matplotlib, instalada al inicio

def generate_bar_chart(labels, values): # definimos la función que creara la gráfica de barras
    fig, ax = plot.subplots() # utlizando la funcionalidad pyplot de la dependencia definimos las variables que representeran la figura o grafo
    ax.bar(labels, values) # la función recibira las etiquetas y valores
    plot.show() # y los mostrara por consola

def generate_pie_chart(labels, values):
    fig, ax = plot.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plot.show()

if __name__ == '__main__':
    labels = ['a', 'b', 'c'] # para testear la funvionalidad 
    values = [25,80,190] # introducimos parametros de prueba
    generate_bar_chart(labels, values) # función para gráficas de barras
    # generate_pie_chart(labels, values) # función para gráficas de tipo pastel
