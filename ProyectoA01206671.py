
#Matriz de caracteres#
characters = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 
    ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
]

"""
================== variables de display para el usuario ======================
"""
#Explicacion del programa
intro = '''
Programa: Adivinador de Contraseñas
Autor: Fernanda Jimenez Estrada
Matricula: A01206671

Este es un programa para adivinar contraseñas.
Tiene tre formas para intentar adivinar tu contraseña.
1. Revisando las 700 contraseñas mas comunes en ingles.
2. Utilizando fuerza bruta, sobre un set de characteres.
'''
#Explicacion de la función compare_whith_list
common_passwords_explanation = '''
Vamos a comparar tu contraseña:
Contamos con las 9664 contraseñas mas comunes en ingles, 
guardadas en el archivo passwords.txt.

Descubramos si tu contraseña es una de ellas...
'''

#Explicacion de la función brute_force
brute_force_explanation = '''
A continuacion vamos a intentar adivinar tu contraseña por 
furtza bruta, es decir vamos a probar todas las combinaciones desde "a"
hasta "ZZZZZZZZ". Esto puede tomar un tiempo muy largo, por eso únicamente
vamos a probar contraseñas de máximo 8 characters, y para hacerlo más rápido
puedes seleccionar un grupo más pequeño de letras. 

'''

#Desplaye de menu para la funcion brute_force
brute_force_menu = '''
Lista de opciones: 
Opcion 0: Minusculas
Opcion 1: Números
Opcion 2: Mayusculas
Opcion 3: Todos los characters
Opcion a elegir: 
'''

"""
================== funciones de auxiliares  =====================================
"""


def get_brute_force_option():
    """
    (uso de funciones y ciclos)
    funcion auxiliar para obtener la opcion del menu que el usuario quiera
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
    funcion auxiliar para leer las lineas de contraseñas que se tiene en el 
    archivo passwoerds.txt, para poder compararlas en la función 
    compare_with_list
    """
    with open("passwords.txt", 'r') as file:
        all_lines = file.readlines()
        for i in range(len(all_lines)):
            all_lines[i] = all_lines[i].strip()
        return all_lines

"""
================== funciones de comparación  =====================================
"""


def compare_with_list(user_password):
    passwords = import_list_of_passwords()
    number_of_tries = 0
    for password in passwords:
        number_of_tries = number_of_tries + 1
        if (password == user_password):
            return f"Entcontre tu contraseña, es la {number_of_tries} de la lista."
    return f"No encontre tu contraseña, intente {number_of_tries} veces."



    """
    (operadores, funciones, listas, listas anidadas, ciclos y condicionales)
    recibe: user_password, brute_force_option
    Recibe la contraseña y la compra con una concatenacion de caracteres, guadados
    en una matriz que van cambiando si la contraseña no coincide con la concatenacion.
    devuelve: dependiendo si la contraseña es encotrada o no, despleagara el mensaje 
    de "Encontrada" o "No encontrada"
    """
def brute_force(user_password, brute_force_option):
    """
    (operadores, funciones, listas, listas anidadas, ciclos y condicionales)
    recibe: user_password, brute_force_option
    Recibe la contraseña y la compra con una concatenacion de caracteres, guadados
    en una matriz que van cambiando si la contraseña no coincide con la concatenacion.
    devuelve: dependiendo si la contraseña es encotrada o no, despleagara el mensaje 
    de "Encontrada" o "No encontrada"
    """
    count = 0 
    #positions in character set for each letter of the password
    p = [0,0,0]
    #chosen character set
    c = characters[brute_force_option]
    # """ because is a string
    current_guess = ""

    while current_guess is not user_password:
        count = count + 1
        print(f"Count: {count}, Current guess: {current_guess}")
        current_guess = c[p[0]] + c[p[1]] + c[p[2]]
        if current_guess == user_password:
            return "Encontre tu contraseña"
        p[0] = p[0] + 1
        if p[0] == len(c):
            p[1] = p[1] + 1
            p[0] = 0
            if p[1] == len(c):
                p[2] = p[2] + 1
                p[1] = 0
                if p[2] == len(c):
                    return "No encontre tu contraseña"

         
    return "Not found"


"""
========================== función main  =====================================
"""

def main():

    print(intro)

    #Leer la contraseña de tu usuario
    user_password = str(input("Introduce la contraseña a adivinar: "))

    print(common_passwords_explanation)
    print(compare_with_list(user_password))

    print(brute_force_explanation)
    brute_force_option = get_brute_force_option()
    print(brute_force(user_password, brute_force_option))

if __name__ == "__main__":
    main()

 
