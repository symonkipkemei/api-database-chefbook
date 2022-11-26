'''
Use the countries API https://restcountries.com/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''


import requests
from pprint import pprint



def get_data(country:str):

    base_url = f"https://restcountries.com/v3.1/name/{country}"


    response = requests.get(base_url)

    print(f"Status code: {response.status_code}")
    print()
    pprint(f"Headers:  {response.headers}")
    print()

    array = response.json() #array/list 
    dict_array = array[0]

    population = dict_array["population"]
    area = dict_array["area"]
    native_name = dict_array["name"]["nativeName"]["eng"]["common"]
    capitals = dict_array["capital"]
    
    return(population,area,native_name,capitals)


def compare_countries(country_a:str, country_b:str):

    population_a,area_a,native_name_a,capitals_a = get_data(country_a)

    population_b,area_b,native_name_b,capitals_b = get_data(country_b)


    #population

    print()
    print("POPULATION")
    print("______________________________________________________________________________________________")

    if population_a > population_b:
        print(f"{country_a} population is bigger than {country_b} by {population_a - population_b} people")
    else:
        print(f"{country_b} population is bigger than {country_a} by {population_b - population_a} people")

    #difference in area

    print()
    print("AREAS")
    print("______________________________________________________________________________________________")

    if area_a > area_b:
        print(f"The landmass of {country_a} is bigger than {country_b} by {area_a -area_b} square meters")
    else:
        print(f"The landmass of {country_b} is bigger than {country_a} by {area_b -area_a} square meters")


    # native names 
    print()
    print("NATIVE NAMES")
    print("______________________________________________________________________________________________")

    print( f"The native name of {country_a} is {native_name_a}")
    print( f"The native name of {country_b} is {native_name_b}")


    # CAPITAL CITY
    print()
    print("CAPITAL CITY")
    print("______________________________________________________________________________________________")

    print( f"The capital city of {country_a} is {capitals_a}")
    print( f"The capital city  of {country_b} is {capitals_b}")


if __name__ == "__main__":

    print("A COMPARISON OF TWO COUNTRIES")
    print("______________________________________________________________________________________________")
    country_a = input("insert country A: ")
    country_b = input("insert country B: ")
    compare_countries(country_a,country_b)

