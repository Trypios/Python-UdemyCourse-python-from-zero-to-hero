def temp():
    '''to_convert lists 4 things: unit1, unit2, unit1 quantity, unit2 quantity'''
    unit_list = ['Celsius', 'Fahrenheit', 'Kelvin']
    to_convert = []
    while True: # Unit1
        try:
            temp_from = input('\nChoose a unit for conversion.\n - {},\n - {},\n - {}\n> '.format(unit_list[0],unit_list[1],unit_list[2]))
            if temp_from[0].lower() == 'c':
                unit_list.pop(0)
                to_convert.append('Celsius')
                break
            elif temp_from[0].lower() == 'f':
                unit_list.pop(1)
                to_convert.append('Fahrenheit')
                break
            elif temp_from[0].lower() == 'k':
                unit_list.pop(2)
                to_convert.append('Kelvin')
                break
            else:
                print('Invalid input, please try again...')
        except:
            print('Invalid input, please try again...')
    while True: # Unit2
        try:
            temp_to = input('\nChoose a unit to convert {} to.\n - {}\n - {}\n> '.format(to_convert[-1],unit_list[0],unit_list[1]))
            if temp_from[0].lower() != temp_to[0].lower():
                if temp_to[0].lower() == 'c':
                    to_convert.append('Celsius')
                    break
                elif temp_to[0].lower() == 'f':
                    to_convert.append('Fahrenheit')
                    break
                elif temp_to[0].lower() == 'k':
                    to_convert.append('Kelvin')
                    break
                else:
                    print('Invalid input, please try again...')
            elif temp_from[0].lower() == temp_to[0].lower():
                print('You have selected the same unit, please select a different one...')
        except:
            print('Invalid input, please try again...')
    while True: # Unit1 quantity
        try:
            units = float(input('\nHow many units of {} do you want to convert to {}?'.format(to_convert[0],to_convert[1])))
            to_convert.append(units)
            return to_convert
        except:
            print('Invalid input, please try again...')

def temp_calc():
    conversion = temp()
    units = conversion[2]
    while conversion[0] == 'Celsius':
        if conversion[1] == 'Fahrenheit': # Celsius to Fahrenheit
            conversion.append((units * 9 / 5) + 32)
            return conversion
        elif conversion[1] == 'Kelvin': # Celsius to Kelvin
            conversion.append(units + 273.15)
            return conversion
    while conversion[0] == 'Fahrenheit':
        if conversion[1] == 'Celsius': # Fahrenheit to Celsius
            conversion.append(5/9 * (units - 32))
            return conversion
        elif conversion[1] == 'Kelvin':# Fahrenheit to Kelvin
            conversion.append((units - 32) * 5 / 9 + 273.15)
            return conversion
    while conversion[0] == 'Kelvin':
        if conversion[1] == 'Fahrenheit': # Kelvin to Fahrenheit
            conversion.append(((units - 273.15) * 9/5) + 32)
            return conversion
        elif conversion[1] == 'Celsius': # Kelvin to Celsius
            conversion.append(units - 273.15)
            return conversion

def temp_conv():
    print('\nYou have chosen TEMPERATURE\n')
    x = temp_calc()
    print('\nRESULT:\n  {:.2f} units of {} = {:.2f} units of {}:'.format(x[2],x[0],x[3],x[1]))
