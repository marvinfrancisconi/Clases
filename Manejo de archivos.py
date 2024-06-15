# Utilidad: Manejo de archivos

# Objetivo principal: Descargar un fichero, acomodarlo, y ajustarlo a sus necesidades.
# Utilizar además un manejo de diccionario adecuado.

# Importar desde las librerías de Python, el formato del archivo que quieres descargar.
import csv

# Abrir el archivo en cuestión
def obtener_Lista():
    lista = []
    with open(r"/home/marvin/Downloads/calificaciones.csv", "r", newline="") as calificaciones:
        lector_CSV = csv.reader(calificaciones, delimiter=";")
        pos = 0
        for linea in lector_CSV:
            if pos != 0:
                for i in range(2, len(linea)):
                    if linea[i] == "":
                        linea[i] = "0,0"
            
                apellidos = linea[0]
                nombre = linea[1]
                asistencia = float((linea[2]).replace("%", ""))
                parcial1 = float((linea[3]).replace(",", "."))
                parcial2 = float((linea[4]).replace(",", "."))
                ordinario1 = float((linea[5]).replace(",", "."))
                ordinario2 = float((linea[6]).replace(",", "."))
                practicas = float((linea[7]).replace(",", "."))
                ordinario_Practicas = float((linea[8]).replace(",", "."))
                lista.append({
                    "apellidos":apellidos, 
                    "nombre":nombre,
                    "asistencia":asistencia,
                    "parcial1":parcial1,
                    "parcial2":parcial2,
                    "ordinario1":ordinario1,
                    "ordinario2":ordinario2, 
                    "practicas":practicas,
                    "ordinario_Practicas":ordinario_Practicas
                })
                print(lista)    
            else: 
                pos = 1
    return lista

obtener_Lista()