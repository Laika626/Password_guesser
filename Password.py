#Avance dos#
password = str(input("Password: "))

#List of characters#
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Function to guess with brute force, first try, try only one character and lowercase#
#TODO, make it work with special characters, more than one letter, uppercase#
#How many time it takes#
def brute_force(password, characters):
    count = 0
    for character in characters:
        count = count + 1;
        if password == character:
            return character, count
    return "Not found"

char, count = brute_force(password, characters)

#imprimir un string formateado con los resultados#
print(f"Your password is:  {char}, number of tries: {count}")




