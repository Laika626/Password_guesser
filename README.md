 dificiles de adivinar. Este proyecto explorara que tan facil y rapido es adivinar una contraseña mediante diferentes metodos. Se implementaran los siguientes metodos: Al azar, comparando la contraseña del usuario mediante contraseñas comunes y comparando caracter por caracter (fuerza bruta). 
- Referencias: https://www.youtube.com/watch?v=7U-RbOKanYs, https://www.youtube.com/watch?v=3NjQ9b3pgIg

------------

#### Algoritmo
    Desplegar presentacion, introduccion y objetivo del programa
    user_password = Pedir al usuario la contraseña.
    Mostrar explicación sobre la funcion que compara la lista de contraseñas y la contraseña del ususario
    Llamar a comprare_with_list(user_password) y mostrar su respuesta.
    Mostrar la explicación de la funcion brute_force y desplegar las opciones para correr la función
    brute_force_option = get_brute_force option
    start_time //empezar a tomar tiempo de ejecucion de la función brute_force
    Mostrar el resultado de brute_force(user_password, brute_force_option)
    end_time //detener el tiempo de dejecución de la funcion brute_force
    tiempo_total = end_time - start_time Mostrar "Tiempo para adivinar tu contraseña : {tiempo_total}s""
	

------------

#### Password Database
Las contraseñas para comparar estan guardadas en el archivo passwords.txt, asegurate de tenerlo en el mismo directorio que ProyectoA01206671.py

------------

#### Módulos Utilizados

Este módulo proporciona funciones que trabajan con el tiempo,. 
La función time.perf_counter() devuelve el valor actual de un contador de alta precisión, expresado en segundos (puede incluir fracciones), que sirve para medir intervalos de tiempo con gran exactitud. Su valor inicial no tiene referencia real (no indica una hora), por lo que solo la diferencia entre dos llamadas permite conocer la duración exacta de un proceso o bloque de código.
Referencias:
https://docs.python.org/es/3.10/library/time.html

------------

#### Instrucciones
1. Descargar los arvhivos Passwords.txt y ProyectoA01206671.py.
2. Correr en terminal con: python3 ProyetoA01206671.py
3. Proporcionar una contraseña de maximo 5 caracteres.
4. El programa comparara la contraseña con la lista de contraseñas (Passwords.txt). Te dara un mensaje dependiendo de si la encontro en el archivo o no.
5. Seleccionar la opcion con la que se quiera hacer la busqueda de la contraseña mediante brute force. Las opciones son las siguientes: Minusculas Números Mayusculas Todos los characters
6. El programa encontrara la contraseña mediante fuerza bruta. El problema trabaja con contraseñas de 5 caracteres, pero debido a la metodología utilizada, esta puede tomar varios minutos.
7. El programa le proprocionara el tiempo que tardo en encontrar su contraseña mediante fuerza bruta y le dara la contraseña desarrollada.
