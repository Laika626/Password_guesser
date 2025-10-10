#Avance dos#
user_password = str(input("Password: "))

#List of characters#
characters = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 
['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']]

# Function to guess with brute force, first try, try only one character and lowercase
# TODO, make it work with special characters, more than one letter, uppercase
# How many time it takes
# Brute force works with 2 char
print(
    '''
    Lista de opciones: 
    Opcion 0: Minusculas
    Opcion 1: Numeros
    Opcion 2: Mayusculas
    ''')
option = int(input("Dame la opcion elegida: "))
def brute_force(user_password, characters, option):
    count = 0 
    chosen_characters = characters[option]
    for character in chosen_characters:
        # ##count = count + 1;
        # if user_password == character:
        #     return character, count
        if character == user_password:
            return character
        for second_character in chosen_characters:
            concatenacion = character + second_character
            if concatenacion == user_password:
                return(concatenacion)
    return "Not found"

concatenacion = brute_force(user_password, characters, option)

#imprimir un string formateado con los resultados#
print(f"Your password is:  {concatenacion}")

def import_list_of_passwords():
    with open("passwords.txt", 'r') as file:
        all_lines = file.readlines()
        for i in range(len(all_lines)):
            all_lines[i] = all_lines[i].strip()
        return all_lines
#Try only with 'a'#
def compare_with_list(user_password):
    passwords = import_list_of_passwords()
    for password in passwords:
        if (password == user_password):
            return "I know your password"
    return "Not found"

print(compare_with_list(user_password))



