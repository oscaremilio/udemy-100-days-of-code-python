
# Programa 'Generador de nombres de Bandas'.
# Crea el nombre a partir de los nombres de tu ciudad y de tu mascota.
# Se requiere un salto de línea antes de que el usuario introduzca los datos.

print("Hola. Bienvenido al 'Generador de nombres de bandas'\n")

ciudad = input("¿De qué ciudad eres? \n")
mascota = input("¿El nombre de tu mascota?\n")
banda = ciudad + " " + mascota

print("El nombre de tu banda podría ser " + '"' + banda + '"')