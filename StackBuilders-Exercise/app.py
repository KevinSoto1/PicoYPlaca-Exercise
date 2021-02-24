import datetime
import re

# Función para ingresar y validar la placa
def ingresarPlaca():
    isValid = False
    while(isValid == False):
        placa = input("Ingrese la placa del vehículo (ABC1234): ").upper()
        validacion = re.compile("[A-Z]{3}[0-9]{4}")
        if(validacion.match(placa)):
            isValid = True
        else:
            print(
                "Placa incorrecta, por favor ingrese una placa con el formato ABC1234: ")
    return placa

# Función para ingresar y validar la fecha
def ingresarFecha():
    while(True):
        try:
            dayformat = "%d/%m/%Y"
            day = input("Ingrese la fecha en el formato (día/mes/año): ")
            validdate = datetime.datetime.strptime(day, dayformat)
            break
            
        except ValueError:
            print("Fecha inválida, por favor ingrese la fecha en el formato (día/mes/año): ")
            continue
    return validdate

# Función para ingresar y validar la hora
def ingresarHora():
    while(True):
        try:
            timeformat = "%H:%M"
            time = input("Ingrese la hora en la que desea circular: ")
            validtime = datetime.datetime.strptime(time, timeformat)
            break
        except ValueError:
            print("Hora invalida, por favor ingrese una hora en el formato (H:M)")
            continue
    return validtime

# Función para la comprobar si el carro puede circular o no en el pico y placa
def picoYPlaca(placa,dateString, hourString ):
    # Se obtiene la hora ingresada
    hora = datetime.time(hourString.hour, hourString.minute)
    # Se obtiene el último número de la placa
    array_placa = list(placa)
    # Se crean las horas de restricción
    restrictionA = datetime.time(7, 0)
    restrictionB = datetime.time(9, 30)
    restrictionC = datetime.time(16, 0)
    restrictionD = datetime.time(19, 30)
    canCirculate = False
    # Se comprueban todas las restricciones y se valida si puede o no circular el vehículo
    if((dateString.strftime("%A") == "Monday") and (int(array_placa[len(array_placa)-1]) == 1 or int(array_placa[len(array_placa)-1]) == 2) and ((hora >= restrictionA and hora <= restrictionB) or (hora >= restrictionC and hora <= restrictionD))):
        print("El vehículo con la placa "+str(placa) +
              " no puede circular a las "+str(hourString.strftime("%H:%M")))
    elif((dateString.strftime("%A") == "Tuesday") and (int(array_placa[len(array_placa)-1]) == 3 or int(array_placa[len(array_placa)-1]) == 4) and ((hora >= restrictionA and hora <= restrictionB) or (hora >= restrictionC and hora <= restrictionD))):
        print("El vehículo con la placa "+str(placa) +
              " no puede circular a las "+str(hourString.strftime("%H:%M")))
    elif((dateString.strftime("%A") == "Wednesday") and (int(array_placa[len(array_placa)-1]) == 5 or int(array_placa[len(array_placa)-1]) == 6) and ((hora >= restrictionA and hora <= restrictionB) or (hora >= restrictionC and hora <= restrictionD))):
        print("El vehículo con la placa "+str(placa) +
              " no puede circular a las "+str(hourString.strftime("%H:%M")))
    elif((dateString.strftime("%A") == "Thursday") and (int(array_placa[len(array_placa)-1]) == 7 or int(array_placa[len(array_placa)-1]) == 8) and ((hora >= restrictionA and hora <= restrictionB) or (hora >= restrictionC and hora <= restrictionD))):
        print("El vehículo con la placa "+str(placa) +
              " no puede circular a las "+str(hourString.strftime("%H:%M")))
    elif((dateString.strftime("%A") == "Friday") and (int(array_placa[len(array_placa)-1]) == 9 or int(array_placa[len(array_placa)-1]) == 0) and ((hora >= restrictionA and hora <= restrictionB) or (hora >= restrictionC and hora <= restrictionD))):
        print("El vehículo con la placa "+str(placa) +
              " no puede circular a las "+str(hourString.strftime("%H:%M")))
    else:
        print("El vehículo con la placa " +
              str(placa)+" puede circular")
        canCirculate = True
    return canCirculate

#Comentar para correr las pruebas
picoYPlaca(ingresarPlaca(),ingresarFecha(),ingresarHora())