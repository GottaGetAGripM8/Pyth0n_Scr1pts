#!/usr/bin/env python

# SCRIPT DE PYTHON | @GottaGetAGripM8

import sys, os
import eyed3
import sqlite3
import datetime

eyed3.log.setLevel("ERROR")

conn = sqlite3.connect('MP3_DB.db')
connCursor = conn.cursor()

connCursor.execute("CREATE TABLE IF NOT EXISTS mp3Data (title TEXT, artist TEXT, genre TEXT, duration CHAR(10))")

print "  _____       _          _             __ _____   "
print " |  __ \     | |        (_)           /_ | ____|  "
print " | |__) |   _| |__  _ __ _  ___ __ _   | | |__    "
print " |  _  / | | | '_ \| '__| |/ __/ _` |  | |___ \   "
print " | | \ \ |_| | |_) | |  | | (_| (_| |  | |___) |  "
print " |_|  \_\__,_|_.__/|_|  |_|\___\__,_|  |_|____/   "
print ""
print "Javier Pardos Blesa | SGE | Python"
print ""                        

raw_input("\nPulsa cualquier tecla para empezar...")

def showMenu():  
    os.system('clear')
    print "\nBienvenido al gestor de canciones mp3, seleccione una opcion:"
    print ""
    print "\n1. Anadir una nueva cancion a la BD (introduce una cancion)"
    print "\n2. Listar todos los generos musicales de la BD"
    print "\n3. Lisar todas las canciones de un interprete (introduce un interprete)"
    print "\n4. Listar todas las canciones de un genero musical (introduce un genero)"
    print "\n5. Listar todas las canciones de la BD"
    print "\n6. Eliminar una cancion de la BD (introduce titulo e interprete)"
    print "\n0. Salir del script"
    print ""

def showOpt0():
    print "\nSaliendo del script..."
    conn.close()
    quit()
    
def showOpt1():
    songPath = (raw_input("\nIntroduce una cancion de esta directorio (cancion.mp3) o escribe la ruta a una (/home/cancion.mp3)..."))
    songFile = eyed3.load(songPath)
    
    conn.execute("INSERT INTO mp3Data (title, artist, genre, duration) VALUES ('" 
                 + str(songFile.tag.title) + "', '" 
                 + str(songFile.tag.artist) + "', '" 
                 + str(songFile.tag.genre.name) + "', '" 
                 + str(secs_to_MS(songFile.info.time_secs)) + "')")
    
    print "    Titulo: " + str(songFile.tag.title)
    print "    Interprete: " + str(songFile.tag.artist)
    print "    Duracion: " + str(secs_to_MS(songFile.info.time_secs)) + "( " + str(songFile.info.time_secs) + " secs)"
    print "    Genero: " + str(songFile.tag.genre.name)
    print ""
    conn.commit()
    print "La cancion ha sido insertada en la DB exitosamente";
    
    comebackToMenu()
     
def showOpt2():
    print "\nListando todos los generos de la BD..."
    connCursor = conn.execute("SELECT title, artist, genre, duration FROM mp3Data ORDER BY genre ASC")
    
    for row in connCursor:
        print "    " + str(row[2]) 
    print "Los generos han sido listados exitosamente"
    
    comebackToMenu()

def showOpt3():
    artistToFind = (raw_input("\nIntroduce un interprete..."))
    connCursor = conn.execute("SELECT title, artist, genre, duration FROM mp3Data WHERE artist='" 
                              + artistToFind + "' ORDER BY artist ASC")
    for row in connCursor:
        print "    " + str(row[1]) + " - " + str(row[0]) +  " | " + str(row[2]) + " | " + str(row[3])
    print "Se ha listado por el interprete: " + artistToFind + " exitosamente"
    
    comebackToMenu()

def showOpt4():
    genreToFind = (raw_input("\nIntroduce un genero..."))
    connCursor = conn.execute("SELECT title, artist, genre, duration FROM mp3Data WHERE genre='" 
                              + genreToFind + "' ORDER BY genre ASC")
    for row in connCursor:
        print "    " + str(row[0]) + " - " + str(row[1]) + " | " + str(row[2])
    print "Se ha listado por el genero: " + genreToFind + " exitosamente"
    
    comebackToMenu()
     
def showOpt5():
    print "\nListando todas las canciones de la BD..."
    connCursor = conn.execute("SELECT title, artist, genre, duration FROM mp3Data ORDER BY title ASC")
    for row in connCursor:
        print "    " + str(row[0])
    print "Se han listado todas las canciones exitosamente";
    
    comebackToMenu()
    
def showOpt6():  
    titleToDelete = (raw_input("\nTitulo de la cancion a eliminar..."))
    artistToDelete = (raw_input("\nInterprete de la cancion a eliminar..."))
    connCursor = conn.execute("DELETE FROM mp3Data WHERE title='" + titleToDelete + "' AND artist='" + artistToDelete + "'")
    conn.commit()
    if conn.total_changes == 1:
        print "Se ha eliminado la cancion:" + titleToDelete + " - " + artistToDelete + " existosamente"
    else:
        print "***ERROR en la eliminacion, pruebe otra vez***"
        showOpt6()
    
    comebackToMenu()

def processOption(usrOption): 
    if usrOption == 1:
        showOpt1()
    elif usrOption == 2:
        showOpt2()
    elif usrOption == 3:
        showOpt3()
    elif usrOption == 4:
        showOpt4()
    elif usrOption == 5:
        showOpt5()
    elif usrOption == 6:
        showOpt6()
    elif usrOption == 0:
        showOpt0()
    else :
        print"\n***ERROR - Elige una opcion de la lista***"
        showMenu();

def secs_to_MS(secs):
    return datetime.datetime.fromtimestamp(secs).strftime('%M:%S')

def comebackToMenu():
    raw_input("\nPulsa cualquier tecla para volver al menu del script...")
    mainLogic()

def mainLogic():
    showMenu()    
    userOption = int(raw_input("\n>> "))
    processOption(userOption)    
    
mainLogic()
    