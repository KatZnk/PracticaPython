import random

# Modificacion 3. Añado las categorías.
coding = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

countries = [
    "argentina",
    "chile",
    "uruguay",
    "italia",
    "china"
]

subjects = [
    "matematicas",
    "literatura",
    "historia",
    "geografia",
    "biologia"
]

categories = {
    "programacion": coding,
    "paises": countries,
    "materias": subjects,
}

guessed = []
attempts = 6
score = 0 

print("¡Bienvenido al Ahorcado!\n")
print("Categorías: ")

for clave in categories:
    print(">", clave.capitalize()) # Muestro en mayúscula.

# Ingreso la palabra y la fuerzo a que sea igual a la del diccionario con el .lower().
# Muestro un mensaje si el usuario tiene un error de tipeo y vuelvo a pedir la categoría hasta que se ingrese una real.
while True:
    category = input("\nIngresa el nombre de la categoría a jugar: ").lower() 
    if category in categories:
        word = random.choice(categories[category]) 
        break
    else: 
        print(f"Error, la categoría '{category}' no existe.")

print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        score += 6
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    
    letter = input("Ingresá una letra: ").lower()
    
    if len(letter) != 1 or not letter.isalpha(): 
        print ("\nEntrada no válida.\n")
        continue 
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        score-= 1
        print("Esa letra no está en la palabra.")
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    score = 0

print(f"Puntaje: {score}")