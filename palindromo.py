def palindromo(cadena):
    if cadena == cadena[::-1]:
        print('Es palindromo')
    else:
        print('NO es palindromo')

palabra = input('Ingresa palabra: ')
palindromo(palabra)
