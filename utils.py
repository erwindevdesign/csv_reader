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
    """
    Searches a list of dictionaries containing population data for a specific country and returns the data for that country as a list.

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
