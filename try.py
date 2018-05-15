countries = {
    'venezuela': 31,
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = input('Ingresa país: ').lower()
    try:
        print('La población de {} es {}M'.format(country, countries[country]))
    except KeyError:
        print('Ingresa un país que este en el diccionario')
