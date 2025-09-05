#Avance dos#
user_password = str(input("Password: "))

#List of characters#
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Function to guess with brute force, first try, try only one character and lowercase#
#TODO, make it work with special characters, more than one letter, uppercase#
#How many time it takes#
def brute_force(user_password, characters):
    count = 0
    for character in characters:
        count = count + 1;
        if user_password == character:
            return character, count
    return "Not found"

char, count = brute_force(user_password, characters)

#imprimir un string formateado con los resultados#
print(f"Your password is:  {char}, number of tries: {count}")

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


