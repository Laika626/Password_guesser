# Importar time API de la libreria estandar de python
import time

# Matriz de caracteres
characters = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    ]

"""
================== variables de display para el usuario ======================
"""
# Explicacion del programa
intro = '''
Programa: Adivinador de Contraseñas de 5 caracteres como máximo
Autor: Fernanda Jimenez Estrada
Matricula: A01206671

Este es un programa para adivinar contraseñas.
Tiene dos formas para intentar adivinar tu contraseña.
1. Revisando las 9664 contraseñas más comunes.
2. Utilizando fuerza bruta, sobre un set de caracteres.
Por favor, digita tu contraseña de máximo 5 caracteres.
'''
# Explicacion de la función compare_whith_list
common_passwords_explanation = '''
Vamos a comparar tu contraseña:
Contamos con las 2258 contraseñas mas comunes de 5 caracteres,
guardadas en el archivo passwords.txt.

Descubramos si tu contraseña es una de ellas...
'''

# Explicacion de la función brute_force
brute_force_explanation = '''
A continuacion vamos a intentar adivinar tu contraseña por
fuerza bruta, es decir vamos a probar todas las combinaciones desde "a"
hasta "ZZZZZ". Esto puede tomar un tiempo muy largo, por eso únicamente
vamos a probar contraseñas de máximo 5 characters, y para hacerlo más rápido
puedes seleccionar un grupo más pequeño de letras.
'''

# Desplaye de menu para la funcion brute_force
brute_force_menu = '''
Lista de opciones:
Opcion 0: Minusculas
Opcion 1: Números
Opcion 2: Mayusculas
Opcion 3: Todos los characters
Opcion a elegir:
'''

"""
==================== funciones de auxiliares  ================================
"""


def get_brute_force_option():
    """
    (uso de funciones y ciclos)
    Funcion auxiliar para obtener la opcion del menu que el usuario quiera
    Le muestra al usuario el menu por lo menos una vez, hasta que el usuario
    de una opcion valida
    """
    option = -1
    while option not in ['0', '1', '2', '3']:
        option = input(brute_force_menu)
    return int(option)


def import_list_of_passwords():
    """
    (uso de ciclos y funciones)
    Funcion auxiliar para leer las lineas de contraseñas que se tiene en el
    archivo passwords.txt, para poder compararlas
    en la función compare_with_list
    Devuelve: Una lista en la que cada elemento es una de las contraseñas
    obtenidas del archivo.
    """
    with open("passwords.txt", 'r') as file:
        all_lines = file.readlines()
        for i in range(len(all_lines)):
            all_lines[i] = all_lines[i].strip()
        return all_lines


"""
================== funciones de comparación  =================================
"""


def compare_with_list(user_password):
    """
    (uso de ciclos, variables, condicionales, operadores y funciones)
    Función que llama a la función import_list_of_passwords y compara
    las contraseñas del archivo con la que el usuario proporciono.
    Devuelve: si la contraseña es encontrada, le da un mensaje afirmativo
    al usuario. Si no es encontrada el mensaje contiene la negacion.
    Ambas respuestas manejan el numero de intentos.
    """
    passwords = import_list_of_passwords()
    number_of_tries = 0
    for password in passwords:
        number_of_tries = number_of_tries + 1
        if (password == user_password):
            return f"Tu contraseña, es la {number_of_tries} de la lista."
    return f"No encontre tu contraseña, intente {number_of_tries} veces."


def brute_force_next_password(c, p):
    """
    (uso de ciclos, variables, condicionales, operadores aritmeticos
    y funciones)
    Función que actua como un candado de combinación, cada vez que se ejecuta
    mueve las posisiones de cada caracter de la contraseña a la siguiente
    posición para poder hacer el mapping con el set de caracteres escogidos
    por el usuario.
    Devuleve: p o falso dependiendo del resulado de iteración.s
    """
    i = 0
    carry_over = 1

    while i < len(p) and carry_over == 1:
        p[i] = p[i] + 1
        if p[i] == len(c):
            p[i] = 0
            carry_over = 1
        else:
            carry_over = 0
        i = i + 1

    if carry_over == 1:
        return False
    return p


def bf_specific_length(user_password, brute_force_option, length):
    """
    (operadores, funciones, listas, listas anidadas, ciclos y condicionales)
    recibe: user_password, brute_force_option, length
    En esta función se prueban todas las contraseñas posibles dado un set de
    caracteres y una longitud especifica.
    devuelve: dependiendo si la contraseña es encotrada, regresa la contraseña.
    Si la contraseña no es encontrada regresa False.
    """
    count = 0
    # positions in character set for each letter of the password
    p = []

    for i in range(length):
        p.append(0)

    # chosen character set
    c = characters[brute_force_option]
    # ""because is a string
    current_guess = ""

    while current_guess is not user_password:
        count = count + 1
        current_guess = ""
        for i in range(length):
            current_guess = current_guess + c[p[i]]
        if current_guess == user_password:
            return current_guess
        p = brute_force_next_password(c, p)
        if not p:
            return False


def brute_force(user_password, brute_force_option):
    """
    (Funciones, ciclos y condicionales)
    Recibe: user_password, brute_force_option
    Funcion que itera
    Devuelve: dependiendo si la contraseña es encotrada o no, asi
    como la contraseña que encontro la función. En caso que la
    funcion no encuentre la contraseña, esta despleagara el mensaje
    "Not found"
    """
    for i in range(1, 6):
        guess = bf_specific_length(user_password, brute_force_option, i)
        if (guess):
            return "Your password is " + guess
    return "Not found"


"""
========================== función main  =====================================
"""


def main():
    """
    (operadores, funciones, listas,operadores aritmeticos, ciclos y API)
    Logica principal del programa.
    devuelve: implicitamente regresa 0 si todo se ejecuta correctamente"
    """
    print(intro)

    # Leer la contraseña de tu usuario
    user_password = str(input("Introduce la contraseña: "))

    print(common_passwords_explanation)
    print(compare_with_list(user_password))

    print(brute_force_explanation)
    brute_force_option = get_brute_force_option()
    # Guardamos el tiempo de inicio de la fución brute_force
    start_time = time.perf_counter()
    print(brute_force(user_password, brute_force_option))
    # Guardamos el tiempo final de la fución brute_force
    end_time = time.perf_counter()
    # Guardamos el tiempo total transcurrido
    tiempo_total = end_time - start_time
    print(f"Tiempo para adivinar tu contraseña : {tiempo_total:.2f}s")


if __name__ == "__main__":
    main()
