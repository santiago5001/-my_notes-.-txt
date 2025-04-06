# Escritura de archivo de texto
# Creamos un nuevo archivo llamado "my_notes.txt" y escribimos tres líneas en él

with open("my_notes.txt", "w") as archivo:  # Modo "w" para escribir (crea o sobrescribe el archivo)
    archivo.write("Estas son mis notas personales:\n")
    archivo.write("1. Estudiar para el examen de programación.\n")
    archivo.write("2. Repasar estructuras de datos y archivos en Python.\n")
    archivo.write("3. Subir este código a mi repositorio en GitHub.\n")

# Lectura del archivo línea por línea
# Abrimos el archivo en modo lectura y mostramos su contenido línea por línea

with open("my_notes.txt", "r") as archivo:  # Modo "r" para leer
    print("Contenido del archivo my_notes.txt:\n")
    linea = archivo.readline()  # Lee una línea
    while linea:  # Mientras exista una línea
        print(linea.strip())  # Imprime la línea sin saltos de línea adicionales
        linea = archivo.readline()  # Lee la siguiente línea

print ("Saludos")
