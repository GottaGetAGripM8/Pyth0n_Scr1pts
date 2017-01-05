#!/usr/bin/env python

# SCRIPT DE PYTHON | @GottaGetAGripM8


from datetime import date, datetime
import math

print "  _____       _          _             __   __   "
print " |  __ \     | |        (_)           /_ | / /   "
print " | |__) |   _| |__  _ __ _  ___ __ _   | |/ /_   "
print " |  _  / | | | '_ \| '__| |/ __/ _` |  | | '_ \  " 
print " | | \ \ |_| | |_) | |  | | (_| (_| |  | | (_) | "
print " |_|  \_\__,_|_.__/|_|  |_|\___\__,_|  |_|\___/  "                                                                                      
print ""
print "Javier Pardos Blesa | SGE | Python"
print ""

#Formato para la fechas 
dateFormat = "%d/%m/%Y";

#FECHA DEL USUARIO #20/06/2016
rawMyBirthDay = raw_input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ");

#Se saca la fecha asi 20/06/1996 00:00:00
complexMBD = datetime.strptime(rawMyBirthDay, dateFormat);

#FECHA ACTUAL
rawActualDate = date.today(); #26/12/2016

complexAD = datetime.strftime(rawActualDate, dateFormat);

print "";

#Con .strftime(dateFormat) se le quitan las horas minutos segundos 
print "Fecha introducida: " + str(complexMBD.strftime(dateFormat));
print "Fecha actual: " + str(complexAD);

print ""

#RESTA DE LAS FECHAS

#Se calculan los dias horas minutos y segundos 
remainingDays = datetime.today() - complexMBD;

print "Diferencia en dias entre las dos fechas: ";
print str(remainingDays.days) + " dias";

print "";

#FUNCION CALCULO

def calculatePercentage(daysToCalculate, typeOfBiorhythm):

    percentageToCalc = math.sin((2*math.pi*daysToCalculate.days)/typeOfBiorhythm)*100;
    roundedPercentage = round(percentageToCalc, 0);
    return roundedPercentage;
    
#PRINT DEL RESULTADO
print "Tus biorritmos a fecha actual (" + str(complexAD) + ") son:";
print "";  
print "Ciclo Fisico: " + str(calculatePercentage(remainingDays, 23)) + "%";
print "Ciclo Emocional: " + str(calculatePercentage(remainingDays, 28)) + "%";
print "Ciclo Intelectual: " + str(calculatePercentage(remainingDays, 33)) + "%";







