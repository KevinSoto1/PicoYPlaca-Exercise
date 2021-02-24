import pytest
from app import picoYPlaca
from app import ingresarPlaca
import datetime

#Las placas terminadas en 1 y 2 no podrían circular los Lunes entre las 7:00 - 9:30 y 16:00 - 19:30
def test_picoYPlacaLunes():
    
    assert picoYPlaca("ABC1111",datetime.datetime.strptime("22/02/2021", "%d/%m/%Y"),datetime.datetime.strptime("9:00", "%H:%M"))==False

def test_picoYPlacaLunes2():
    assert picoYPlaca("ABC1112",datetime.datetime.strptime("22/02/2021", "%d/%m/%Y"),datetime.datetime.strptime("19:31", "%H:%M"))==True
#Las placas terminadas en 3 y 4 no podrían circular los Martes entre las 7:00 - 9:30 y 16:00 - 19:30
def test_picoYPlacaMartes():
    
    assert picoYPlaca("ABC1113",datetime.datetime.strptime("23/02/2021", "%d/%m/%Y"),datetime.datetime.strptime("9:00", "%H:%M"))==False

def test_picoYPlacaMartes2():
    assert picoYPlaca("ABC1114",datetime.datetime.strptime("23/02/2021", "%d/%m/%Y"),datetime.datetime.strptime("19:31", "%H:%M"))==True

#Las placas terminadas en 5 y 6 no podrían circular los Miercoles entre las 7:00 - 9:30 y 16:00 - 19:30
def test_picoYPlacaMiercoles():
    
    assert picoYPlaca("ABC1115",datetime.datetime.strptime("24/02/2021", "%d/%m/%Y"),datetime.datetime.strptime("9:00", "%H:%M"))==False

def test_picoYPlacaMiercoles2():
    assert picoYPlaca("ABC1116",datetime.datetime.strptime("24/02/2021", "%d/%m/%Y"),datetime.datetime.strptime("19:31", "%H:%M"))==True

#Las placas terminadas en 7 y 8 no podrían circular los Jueves entre las 7:00 - 9:30 y 16:00 - 19:30
def test_picoYPlacaJueves():
    
    assert picoYPlaca("ABC1117",datetime.datetime.strptime("25/02/2021", "%d/%m/%Y"),datetime.datetime.strptime("9:00", "%H:%M"))==False

def test_picoYPlacaJueves2():
    assert picoYPlaca("ABC1118",datetime.datetime.strptime("25/02/2021", "%d/%m/%Y"),datetime.datetime.strptime("19:31", "%H:%M"))==True

#Las placas terminadas en 9 y 0 no podrían circular los Viernes entre las 7:00 - 9:30 y 16:00 - 19:30
def test_picoYPlacaViernes():
    
    assert picoYPlaca("ABC1119",datetime.datetime.strptime("26/02/2021", "%d/%m/%Y"),datetime.datetime.strptime("9:00", "%H:%M"))==False

def test_picoYPlacaViernes2():
    assert picoYPlaca("ABC1110",datetime.datetime.strptime("26/02/2021", "%d/%m/%Y"),datetime.datetime.strptime("19:31", "%H:%M"))==True

#Todas las placas pueden circular los sábados y domingos sin restricciones 
def test_picoYPlacaSábado():
    assert picoYPlaca("ABC1111",datetime.datetime.strptime("27/02/2021", "%d/%m/%Y"),datetime.datetime.strptime("9:00", "%H:%M"))==True

def test_picoYPlacaDomingo():
    assert picoYPlaca("ABC1118",datetime.datetime.strptime("28/02/2021", "%d/%m/%Y"),datetime.datetime.strptime("19:15", "%H:%M"))==True