# Converts various units between one another.
# The user enters the type of unit being entered, the type of unit they want to convert to and then the value.
# The program will then make the conversion.

# TEMPERATURE (Celsius, Fahrenheit, Kelvin)
# MASS (tonne, kilogram, gram, milligram, microgram, imperial tonne, us tonne, stone, pound, ounce)
# DISTANCE (kilometer, meter, centimeter, millimeter, micrometer, nanometer | mile, yard, foot, inch)

import UnitConverter.distance as ucd, UnitConverter.mass as ucm, UnitConverter.temperature as uct

def prompt_categ():
    while True:
        try:
            userinput = input('\nChoose what are you going to convert?\nTemperature / Mass / Distance...')
            if userinput[0].lower() == 't':
                return 't'
            elif userinput[0].lower() == 'm':
                return 'm'
            elif userinput[0].lower() == 'd':
                return 'd'
            else:
                print('Invalid input, please try again...')
        except:
            print('Invalid input, please try again...')

def startover():
    while True:
        try:
            x = input('Continue converting units? y/n:\n> ')
            if x[0].lower() == 'y':
                return True
            elif x[0].lower() == 'n':
                return False
            else:
                print('Invalid input, please try again...')
        except:
            print('Invalid input, please try again...')

running = True

while running:
    category = prompt_categ()
    # FOR TEMPERATURES:
    if category == 't':
        uct.temp_conv()
    # FOR MASS:
    elif category == 'm':
        ucm.mass_conv()
    # FOR DISTANCE:
    elif category == 'd':
        ucd.distance_conv()
    if not startover():
        break
