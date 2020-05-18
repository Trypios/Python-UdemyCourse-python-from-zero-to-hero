def distance():
    '''to_convert lists 4 things: unit1, unit2, unit1 quantity, unit2 quantity'''
    unit_list = ['kilometer', 'meter', 'centimeter', 'millimeter', 'micrometer', 'nanometer', 'mile', 'yard', 'foot', 'inch']
    to_convert = []
    while True: # Unit1
        try:
            dist_from = input('\nChoose a unit for conversion.\n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}\n> '.format(unit_list[0],unit_list[1],unit_list[2],unit_list[3],unit_list[4],unit_list[5],unit_list[6],unit_list[7],unit_list[8],unit_list[9]))
            if dist_from[0:4].lower() == 'kilo':
                unit_list.pop(0)
                to_convert.append('kilometer')
                break
            elif dist_from[0:4].lower() == 'mete':
                unit_list.pop(1)
                to_convert.append('meter')
                break
            elif dist_from[0:4].lower() == 'cent':
                unit_list.pop(2)
                to_convert.append('centimeter')
                break
            elif dist_from[0:4].lower() == 'mill':
                unit_list.pop(3)
                to_convert.append('millimeter')
                break
            elif dist_from[0:4].lower() == 'micr':
                unit_list.pop(4)
                to_convert.append('micrometer')
                break
            elif dist_from[0:4].lower() == 'nano':
                unit_list.pop(5)
                to_convert.append('nanometer')
                break
            elif dist_from[0:4].lower() == 'mile':
                unit_list.pop(6)
                to_convert.append('mile')
                break
            elif dist_from[0:4].lower() == 'yard':
                unit_list.pop(7)
                to_convert.append('yard')
                break
            elif dist_from[0:4].lower() == 'foot':
                unit_list.pop(8)
                to_convert.append('foot')
                break
            elif dist_from[0:4].lower() == 'inch':
                unit_list.pop(9)
                to_convert.append('inch')
                break
            else:
                print('Invalid input, please try again...')
        except:
            print('Invalid input, please try again...')
    while True: # Unit2
        try:
            dist_to = input('\nChoose a unit to convert {}s to.\n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}\n> '.format(to_convert[-1],unit_list[0],unit_list[1],unit_list[2],unit_list[3],unit_list[4],unit_list[5],unit_list[6],unit_list[7],unit_list[8]))
            if dist_from[0:4].lower() != dist_to[0:4].lower():
                if dist_to[0:4].lower() == 'kilo':
                    to_convert.append('kilometer')
                    break
                elif dist_to[0:4].lower() == 'mete':
                    to_convert.append('meter')
                    break
                elif dist_to[0:4].lower() == 'cent':
                    to_convert.append('centimeter')
                    break
                elif dist_to[0:4].lower() == 'mill':
                    to_convert.append('millimeter')
                    break
                elif dist_to[0:4].lower() == 'micr':
                    to_convert.append('micrometer')
                    break
                elif dist_to[0:4].lower() == 'nano':
                    to_convert.append('nanometer')
                    break
                elif dist_to[0:4].lower() == 'mile':
                    to_convert.append('mile')
                    break
                elif dist_to[0:4].lower() == 'yard':
                    to_convert.append('yard')
                    break
                elif dist_to[0:4].lower() == 'foot':
                    to_convert.append('foot')
                    break
                elif dist_to[0:4].lower() == 'inch':
                    to_convert.append('inch')
                    break
                else:
                    print('Invalid input, please try again...')
            elif dist_from[0:4].lower() == dist_to[0:4].lower():
                print('You have selected the same unit, please select a different one...')
        except:
            print('Invalid input, please try again...')
    print(to_convert)
    while True: # Unit1 quantity
        try:
            units = float(input('\nHow many units of {} do you want to convert to units of {}?'.format(to_convert[0],to_convert[1])))
            to_convert.append(units)
            return to_convert
        except:
            print('Invalid input, please try again...')

def distance_calc():
    conversion = distance()
    units = conversion[2]
    while conversion[0] == 'kilometer': # From Kilometer to all other units
        if conversion[1] == 'meter':
            conversion.append(units * 10**3)
            return conversion
        elif conversion[1] == 'centimeter':
            conversion.append(units * 10**5)
            return conversion
        elif conversion[1] == 'millimeter':
            conversion.append(units * 10**6)
            return conversion
        elif conversion[1] == 'micrometer':
            conversion.append(units * 10**9)
            return conversion
        elif conversion[1] == 'nanometer':
            conversion.append(units * 10**12)
            return conversion
        elif conversion[1] == 'mile':
            conversion.append(units / 1.609)
            return conversion
        elif conversion[1] == 'yard':
            conversion.append(units * 1093.613)
            return conversion
        elif conversion[1] == 'foot':
            conversion.append(units * 3280.84)
            return conversion
        elif conversion[1] == 'inch':
            conversion.append(units * 39370.079)
            return conversion

    while conversion[0] == 'meter': # From Meter to all other units
        if conversion[1] == 'kilometer':
            conversion.append(units / 1000)
            return conversion
        elif conversion[1] == 'centimeter':
            conversion.append(units * 100)
            return conversion
        elif conversion[1] == 'millimeter':
            conversion.append(units * 1000)
            return conversion
        elif conversion[1] == 'micrometer':
            conversion.append(units * 10**6)
            return conversion
        elif conversion[1] == 'nanometer':
            conversion.append(units * 10**9)
            return conversion
        elif conversion[1] == 'mile':
            conversion.append(units / 1609.344)
            return conversion
        elif conversion[1] == 'yard':
            conversion.append(units * 1.094)
            return conversion
        elif conversion[1] == 'foot':
            conversion.append(units * 3.281)
            return conversion
        elif conversion[1] == 'inch':
            conversion.append(units * 39.37)
            return conversion

    while conversion[0] == 'centimeter': # From centimeter to all other units
        if conversion[1] == 'kilometer':
            conversion.append(units / 10**5)
            return conversion
        elif conversion[1] == 'meter':
            conversion.append(units / 100)
            return conversion
        elif conversion[1] == 'millimeter':
            conversion.append(units * 10)
            return conversion
        elif conversion[1] == 'micrometer':
            conversion.append(units * 10**4)
            return conversion
        elif conversion[1] == 'nanometer':
            conversion.append(units * 10**7)
            return conversion
        elif conversion[1] == 'mile':
            conversion.append(units / 160934.4)
            return conversion
        elif conversion[1] == 'yard':
            conversion.append(units / 91.44)
            return conversion
        elif conversion[1] == 'foot':
            conversion.append(units / 30.48)
            return conversion
        elif conversion[1] == 'inch':
            conversion.append(units / 2.54)
            return conversion

    while conversion[0] == 'millimeter': # From Millimeter to all other units
        if conversion[1] == 'kilometer':
            conversion.append(units / 10**6)
            return conversion
        elif conversion[1] == 'meter':
            conversion.append(units / 1000)
            return conversion
        elif conversion[1] == 'centimeter':
            conversion.append(units / 10)
            return conversion
        elif conversion[1] == 'micrometer':
            conversion.append(units * 1000)
            return conversion
        elif conversion[1] == 'nanometer':
            conversion.append(units * 10**6)
            return conversion
        elif conversion[1] == 'mile':
            conversion.append(units / (1.609 * 10**6))
            return conversion
        elif conversion[1] == 'yard':
            conversion.append(units / 914.4)
            return conversion
        elif conversion[1] == 'foot':
            conversion.append(units / 304.8)
            return conversion
        elif conversion[1] == 'inch':
            conversion.append(units / 25.4)
            return conversion

    while conversion[0] == 'micrometer': # From Micrometer to all other units
        if conversion[1] == 'kilometer':
            conversion.append(units / 10**9)
            return conversion
        elif conversion[1] == 'meter':
            conversion.append(units / 10**6)
            return conversion
        elif conversion[1] == 'centimeter':
            conversion.append(units / 10**4)
            return conversion
        elif conversion[1] == 'millimeter':
            conversion.append(units / 1000)
            return conversion
        elif conversion[1] == 'nanometer':
            conversion.append(units * 1000)
            return conversion
        elif conversion[1] == 'mile':
            conversion.append(units / (1.609 * 10**9))
            return conversion
        elif conversion[1] == 'yard':
            conversion.append(units / 914400)
            return conversion
        elif conversion[1] == 'foot':
            conversion.append(units / 304800)
            return conversion
        elif conversion[1] == 'inch':
            conversion.append(units / 25400)
            return conversion

    while conversion[0] == 'nanometer': # From Nanometer to all other units
        if conversion[1] == 'kilometer':
            conversion.append(units / 10**12)
            return conversion
        elif conversion[1] == 'meter':
            conversion.append(units / 10**9)
            return conversion
        elif conversion[1] == 'centimeter':
            conversion.append(unit7 / 10**6)
            return conversion
        elif conversion[1] == 'millimeter':
            conversion.append(units / 10**6)
            return conversion
        elif conversion[1] == 'micrometer':
            conversion.append(units / 1000)
            return conversion
        elif conversion[1] == 'mile':
            conversion.append(units / (1.609 * 10**12))
            return conversion
        elif conversion[1] == 'yard':
            conversion.append(units / (9.144 * 10**8))
            return conversion
        elif conversion[1] == 'foot':
            conversion.append(units / (3.048 * 10**8))
            return conversion
        elif conversion[1] == 'inch':
            conversion.append(units / (2.54 * 10**7))
            return conversion

    while conversion[0] == 'mile': # From Mile to all other units
        if conversion[1] == 'kilometer':
            conversion.append(units * 1.609)
            return conversion
        elif conversion[1] == 'meter':
            conversion.append(units * 1609.344)
            return conversion
        elif conversion[1] == 'centimeter':
            conversion.append(units * 160934.4)
            return conversion
        elif conversion[1] == 'millimeter':
            conversion.append(units * 1.609 * 10**6)
            return conversion
        elif conversion[1] == 'micrometer':
            conversion.append(units * 1.609 * 10**9)
            return conversion
        elif conversion[1] == 'nanometer':
            conversion.append(units * 1.609 * 10**12)
            return conversion
        elif conversion[1] == 'yard':
            conversion.append(units * 1760)
            return conversion
        elif conversion[1] == 'foot':
            conversion.append(units * 5280)
            return conversion
        elif conversion[1] == 'inch':
            conversion.append(units * 63360)
            return conversion

    while conversion[0] == 'yard': # From Yard to all other units
        if conversion[1] == 'kilometer':
            conversion.append(units / 1093.613)
            return conversion
        elif conversion[1] == 'meter':
            conversion.append(units / 1.094)
            return conversion
        elif conversion[1] == 'centimeter':
            conversion.append(units * 91.44)
            return conversion
        elif conversion[1] == 'millimeter':
            conversion.append(units * 9.144 * 10**2)
            return conversion
        elif conversion[1] == 'micrometer':
            conversion.append(units * 9.144 * 10**5)
            return conversion
        elif conversion[1] == 'nanometer':
            conversion.append(units * 9.144 * 10**8)
            return conversion
        elif conversion[1] == 'mile':
            conversion.append(units / 1760)
            return conversion
        elif conversion[1] == 'foot':
            conversion.append(units * 3)
            return conversion
        elif conversion[1] == 'inch':
            conversion.append(units * 36)
            return conversion

    while conversion[0] == 'foot': # From Foot to all other units
        if conversion[1] == 'kilometer':
            conversion.append(units / 3280.84)
            return conversion
        elif conversion[1] == 'meter':
            conversion.append(units / 3.281)
            return conversion
        elif conversion[1] == 'centimeter':
            conversion.append(units * 30.48)
            return conversion
        elif conversion[1] == 'millimeter':
            conversion.append(units * 304.8)
            return conversion
        elif conversion[1] == 'micrometer':
            conversion.append(units * 3.048 * 10**5)
            return conversion
        elif conversion[1] == 'nanometer':
            conversion.append(units * 3.048 * 10**8)
            return conversion
        elif conversion[1] == 'mile':
            conversion.append(units / 5280)
            return conversion
        elif conversion[1] == 'yard':
            conversion.append(units / 3)
            return conversion
        elif conversion[1] == 'inch':
            conversion.append(units * 12)
            return conversion

    while conversion[0] == 'inch': # From Inch to all other units
        if conversion[1] == 'kilometer':
            conversion.append(units / 39370.079)
            return conversion
        elif conversion[1] == 'meter':
            conversion.append(units / 39.37)
            return conversion
        elif conversion[1] == 'centimeter':
            conversion.append(units * 2.54)
            return conversion
        elif conversion[1] == 'millimeter':
            conversion.append(units * 25.4)
            return conversion
        elif conversion[1] == 'micrometer':
            conversion.append(units * 25400)
            return conversion
        elif conversion[1] == 'nanometer':
            conversion.append(units * 2.54 * 10**7)
            return conversion
        elif conversion[1] == 'mile':
            conversion.append(units / 63360)
            return conversion
        elif conversion[1] == 'yard':
            conversion.append(units / 36)
            return conversion
        elif conversion[1] == 'foot':
            conversion.append(units /12)
            return conversion

def distance_conv():
    print('\nYou have chosen DISTANCE\n')
    x = distance_calc()
    print('\nRESULT:\n  {:.2f} units of {} = {:.2f} units of {}:'.format(x[2],x[0],x[3],x[1]))
