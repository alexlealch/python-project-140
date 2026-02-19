import random


def run_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds_count = 0
    while rounds_count < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ")

        expected_answer = "yes" if number % 2 == 0 else "no"

        if answer == expected_answer:
            print("Correct!")
            rounds_count += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{expected_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    run_game()


if __name__ == "__main__":
    main()


# Explicación paso a paso para el estudiante:
#
# 1. Importación de módulos:
#    - `import random`: Importamos el módulo `random` para generar números aleatorios.
#
# 2. Definición de la función `run_game()`:
#    - Esta función encapsula toda la lógica del juego.
#    - `print("Welcome to the Brain Games!")`: Muestra el mensaje de bienvenida.
#    - `print("May I have your name?")`: Solicita el nombre del usuario.
#    - `name = input()`: Lee el nombre ingresado por el usuario y lo guarda en la variable `name`.
#    - `print(f"Hello, {name}!")`: Saluda al usuario usando su nombre.
#    - `print(...)`: Muestra las instrucciones del juego ("yes" si es par, "no" si es impar).
#
# 3. Bucle del juego:
#    - `rounds_count = 0`: Inicializamos un contador de rondas ganadas en 0.
#    - `while rounds_count < 3:`: Iniciamos un bucle que se ejecutará mientras el usuario no haya ganado 3 rondas.
#        - `number = random.randint(1, 100)`: Generamos un número aleatorio entre 1 y 100.
#        - `print(f"Question: {number}")`: Mostramos el número al usuario.
#        - `answer = input("Your answer: ")`: Solicitamos la respuesta del usuario.
#
# 4. Lógica de verificación (Par o Impar):
#    - `expected_answer = 'yes' if number % 2 == 0 else 'no'`: Determinamos la respuesta correcta.
#      Si el residuo de dividir por 2 es 0 (`number % 2 == 0`), el número es par ('yes'), de lo contrario es impar ('no').
#
# 5. Comprobación de la respuesta:
#    - `if answer == expected_answer:`: Comparamos la respuesta del usuario con la esperada.
#        - Si es correcta: Imprimimos "Correct!" y aumentamos `rounds_count` en 1.
#        - Si es incorrecta (`else`):
#            - Imprimimos el mensaje de error mostrando la respuesta incorrecta y la correcta.
#            - Imprimimos "Let's try again, {name}!".
#            - `return`: Terminamos la función (y por lo tanto el juego) inmediatamente.
#
# 6. Victoria:
#    - Si el bucle termina porque `rounds_count` llega a 3, se ejecuta `print(f"Congratulations, {name}!")`.
#
# 7. Ejecución del script:
#    - `if __name__ == "__main__":`: Bloque estándar en Python para ejecutar `main()` solo si el archivo se ejecuta directamente.
