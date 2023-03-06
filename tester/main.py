# index 10
""" 
import utils

keys, values = utils.population()
print(keys, values)
 """


import utils 

keys, values = utils.get_population() 
print(keys, values ) 


import utils  

def run(): 
    keys, values = utils.get_list()  
    print(keys, values)
    country = input('Type country item: ')
    result = utils.population_by_country(data, country)
    print(result)

if __name__ == '__main__': 
    run()