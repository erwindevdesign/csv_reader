import matplotlib.pyplot as plot 

def generate_bar_chart(labels, values): 
    """ Generate a bar based on the given labels and values.

    Args:
        labels (list): A list of strings representing the labels for each bar.
        values (list): A list of numbers representing the values for each bar.

    Display a bar chart with the given labels and values.
    
    """
    fig, ax = plot.subplots()
    plot.title('Population increase')
    plot.xlabel('Year')
    plot.ylabel('Population')
    ax.bar(labels, values, color='green') 
    plot.show() 
    

def generate_pie_chart(labels, values):
    """ 
    explode = [0] * len(labels)
    for i, value in enumerate(values):
        if value < "1":
            explode[i] = 0.1
    """

    # explode=explode

    fig, ax = plot.subplots()
    plot.title('World Population Percentage')
 
    ax.pie(values, labels=(labels), autopct='%1.0f%%', wedgeprops={"linewidth": 0.7, "edgecolor": "white"}, shadow=True, startangle=45)
    ax.axis('equal')
    plot.show()

     

if __name__ == '__main__':
    labels = ['a', 'b', 'c'] # para testear la funvionalidad 
    values = [25,80,190] # introducimos parametros de prueba
    generate_bar_chart(labels, values) # función para gráficas de barras
    # generate_pie_chart(labels, values) # función para gráficas de tipo pastel
