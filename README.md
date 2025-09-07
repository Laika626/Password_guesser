# I Know your password

## Contexto
Las contraseñas son una de las bases mas importantes de nuestra seguridad en linea. Frecuentemente nos encontramos con noticias que exponen casos en los cuales la seguridad de personas, organizaciones o empresas se vieron comprometidos por un problema o leak con las contraseñas, teniendo como consecuencia perdida monetaria significativa y de confianza por parte de los usuarios. La forma en la que nosotros como usuarios nos podemos proteger es mediante la eleccion de contraseñas que sean dificiles de adivinar. Este proyecto explorara que tan facil y rapido es adivinar una contraseña mediante diferentes metodos. Se implementaran los siguientes metodos: Al azar, comparando la contraseña del usuario mediante contraseñas comunes, mediante la comparacion de la contraseña con palabras de un diccionario y comparando caracter por caracter. Referencias: https://www.youtube.com/watch?v=7U-RbOKanYs, https://www.youtube.com/watch?v=3NjQ9b3pgIg
## Algoritmo
1. user_password = Pedir al usuario la contraseña.
2. Inicializar guess como un string vacio y un contador inicializado a cero.
3. Se utilizara un ciclo for por cada uno de los metodos.
   3.1 while (guess != user_password)
     3.1.1 Generara otro guess
   3.2 Imprimir guess, contador
4. Salir del programa
### Por investigar 
Algoritmo de random
Algoritmo fuerza bruta
Algoritmo contraseñas comunes
Algoritmo diccionario
## Password database
Las contraseñas para comparar estan guardadas en el archivo passwords.txt, asegurate de tenerlo en el mismo directorio que ProyectoA01206671.py  