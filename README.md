# I Know your password

## Contexto
Las contraseñas son una de las bases mas importantes de nuestra seguridad en linea. Frecuentemente nos encontramos con noticias que exponen casos en los cuales la seguridad de personas, organizaciones o empresas se vieron comprometidos por un problema o leak con las contraseñas, teniendo como consecuencia perdida monetaria significativa y de confianza por parte de los usuarios. La forma en la que nosotros como usuarios nos podemos proteger es mediante la eleccion de contraseñas que sean dificiles de adivinar. Este proyecto explorara que tan facil y rapido es adivinar una contraseña mediante diferentes metodos. Se implementaran los siguientes metodos: Al azar, comparando la contraseña del usuario mediante contraseñas comunes y comparando caracter por caracter (fuerza bruta). Referencias: https://www.youtube.com/watch?v=7U-RbOKanYs, https://www.youtube.com/watch?v=3NjQ9b3pgIg
## Algoritmo
1. Desplegar presentacion, introduccion y objetivo del programa
2. user_password = Pedir al usuario la contraseña.
3. Mostrar explicación sobre la funcion que compara la lista de contraseñas y la contraseña del ususario
4. Llamar a comprare_with_list(user_password) y mostrar su respuesta. 
5. Mostrar la explicación de la funcion brute_force y desplegar las opciones para correr la función
6. brute_force_option = get_brute_force option
7. start_time //empezar a tomar tiempo de ejecucion de la función brute_force
8. Mostrar el resultado de brute_force(user_password, brute_force_option)
9. end_time //detener el tiempo de dejecución de la funcion brute_force 
10. tiempo_total = end_time - start_time
Mostrar "Tiempo para adivinar tu contraseña : {tiempo_total}s""
## Password database
Las contraseñas para comparar estan guardadas en el archivo passwords.txt, asegurate de tenerlo en el mismo directorio que ProyectoA01206671.py 
## Instrucciones 
1. Descargar los arvhivos Passwords.txt y ProyectoA01206671.py.
2. Correr en terminal con:
    python3 ProyetoA01206671.py
3. Proporcionar una contraseña de maximo 5 caracteres. 
4. El programa comparara la contraseña con la lista de contraseñas (Passwords.txt). Te dara un mensaje dependiendo de si la encontro en el archivo o no. 
5. Seleccionar la opcion con la que se quiera hacer la busqueda de la contraseña mediante brute force. Las opciones son las siguientes:
  Minusculas
  Números
  Mayusculas
  Todos los characters
6. El programa encontrara la contraseña mediante fuerza bruta. El problema trabaja con contraseñas de 5 caracteres, pero debido a la metodología utilizada, esta puede tomar varios minutos. 
7. El programa le proprocionara el tiempo que tardo en encontrar su contraseña mediante fuerza bruta y le dara la contraseña desarrollada.


## Gracias por utilizar este adivinador de contraseñas