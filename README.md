# PicoYPlaca-Exercise  
# Instructions  
Using the language that you feel most proficient in, we’d like you to write a "Pico y Placa" predictor. The inputs should be a license plate number (the full number, not the last digit), a date (as a String), and a time, and the program will return whether or not that car can be on the road.  
To develop this application you need to consider the past rules of the Pico&Placa. (Hours: 7:00am - 9:30am / 16:00pm - 19:30)  
Note: This are the restrictions:  
1. Monday: License Plate number ending with 1 or 2 can't circulate  
2. Tuesday: License Plate number ending with 3 or 4 can't circulate  
3. Wednesday: License Plate number ending with 5 or 6 can't circulate  
4. Thursday: License Plate number ending with 7 or 8 can't circulate  
5. Friday: License Plate number ending with 9 or 0 can't circulate  
6. On Saturday and Sunday everyone can go out
# Unit tests  
To run unit tests on VSCode you will have to follow the following steps:  
1.- Open Command Palette (Ctrl+Shift+P)  
2.- Type "Python:Configure tests"  
3.- Select pytest from the list  
4.- On the app.py file comment the last code line to run the tests 
