#!/usr/bin/env python

# SCRIPT DE PYTHON | @GottaGetAGripM8


print "  _____       _          _             __ _  _    "
print " |  __ \     | |        (_)           /_ | || |   "
print " | |__) |   _| |__  _ __ _  ___ __ _   | | || |_  "
print " |  _  / | | | '_ \| '__| |/ __/ _` |  | |__   _| "
print " | | \ \ |_| | |_) | |  | | (_| (_| |  | |  | |   "
print " |_|  \_\__,_|_.__/|_|  |_|\___\__,_|  |_|  |_|   "                                              
print ""
print "Javier Pardos Blesa | SGE | Python"
print ""


# Variables para las coincidencias
# y el num de lineas del archivo 
numLineas, numPalabras = 0,0
palEnLineaActual = 0

# Se le pasa el archivo
myTextFile = raw_input("Archivo que desea leer: ")

print ""

# Se abre para lectura
ficheroAbierto = open(myTextFile, "r")

# Se define la palabra a buscar
myWord = raw_input("Palabra que desea buscar: ")

print ""

lineasTotales = ficheroAbierto.readlines()

for i in lineasTotales:
	for palEnLineaActual in i.split():
		if palEnLineaActual == myWord:
			numLineas +=1
			numPalabras +=1
			print "Encontrada una coincidencia en la linea " + str(numLineas) + "."

print ""

ficheroAbierto.close()

print ""
print "La palabra " + myWord + " ha aparecido en " + str(numLineas) + " lineas."
print ""
print "Lineas totales del archivo " + str(len(lineasTotales)) + "."



