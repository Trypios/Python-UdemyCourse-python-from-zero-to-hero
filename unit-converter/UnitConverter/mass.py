def mass():
    '''to_convert lists 4 things: unit1, unit2, unit1 quantity, unit2 quantity'''
    unit_list = ['metric ton', 'kilogram', 'gram', 'milligram', 'microgram', 'imperial ton', 'US ton', 'stone', 'pound', 'ounce']
    to_convert = []
    while True: # Unit1
        try:
            mass_from = input('\nChoose a unit for conversion.\n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}\n> '.format(unit_list[0],unit_list[1],unit_list[2],unit_list[3],unit_list[4],unit_list[5],unit_list[6],unit_list[7],unit_list[8],unit_list[9]))
            if mass_from[0:3].lower() == 'met':
                unit_list.pop(0)
                to_convert.append('metric ton')
                break
            elif mass_from[0:3].lower() == 'kil':
                unit_list.pop(1)
                to_convert.append('kilogram')
                break
            elif mass_from[0:3].lower() == 'gra':
                unit_list.pop(2)
                to_convert.append('gram')
                break
            elif mass_from[0:3].lower() == 'mil':
                unit_list.pop(3)
                to_convert.append('milligram')
                break
            elif mass_from[0:3].lower() == 'mic':
                unit_list.pop(4)
                to_convert.append('microgram')
                break
            elif mass_from[0:3].lower() == 'imp':
                unit_list.pop(5)
                to_convert.append('imperial ton')
                break
            elif mass_from[0:2].lower() == 'us':
                unit_list.pop(6)
                to_convert.append('US ton')
                break
            elif mass_from[0:3].lower() == 'sto':
                unit_list.pop(7)
                to_convert.append('stone')
                break
            elif mass_from[0:3].lower() == 'pou':
                unit_list.pop(8)
                to_convert.append('pound')
                break
            elif mass_from[0:3].lower() == 'oun':
                unit_list.pop(9)
                to_convert.append('ounce')
                break
            else:
                print('Invalid input, please try again...')
        except:
            print('Invalid input, please try again...')
    while True: # Unit2
        try:
            mass_to = input('\nChoose a unit to convert {}s to.\n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}, \n - {}\n> '.format(to_convert[-1],unit_list[0],unit_list[1],unit_list[2],unit_list[3],unit_list[4],unit_list[5],unit_list[6],unit_list[7],unit_list[8]))
            if mass_from[0:3].lower() != mass_to[0:3].lower():
                if mass_to[0:3].lower() == 'met':
                    to_convert.append('metric ton')
                    break
                elif mass_to[0:3].lower() == 'kil':
                    to_convert.append('kilogram')
                    break
                elif mass_to[0:3].lower() == 'gra':
                    to_convert.append('gram')
                    break
                elif mass_to[0:3].lower() == 'mil':
                    to_convert.append('milligram')
                    break
                elif mass_to[0:3].lower() == 'mic':
                    to_convert.append('microgram')
                    break
                elif mass_to[0:3].lower() == 'imp':
                    to_convert.append('imperial ton')
                    break
                elif mass_to[0:2].lower() == 'us':
                    to_convert.append('US ton')
                    break
                elif mass_to[0:3].lower() == 'sto':
                    to_convert.append('stone')
                    break
                elif mass_to[0:3].lower() == 'pou':
                    to_convert.append('pound')
                    break
                elif mass_to[0:3].lower() == 'oun':
                    to_convert.append('ounce')
                    break
                else:
                    print('Invalid input, please try again...')
            elif mass_from[0:3].lower() == mass_to[0:3].lower():
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

def mass_calc():
    conversion = mass()
    units = conversion[2]
    while conversion[0] == 'metric ton': # From Metric Ton to all other units
        if conversion[1] == 'kilogram':
            conversion.append(units * 1000)
            return conversion
        elif conversion[1] == 'gram':
            conversion.append(units * 1e6)
            return conversion
        elif conversion[1] == 'milligram':
            conversion.append(units * 1e9)
            return conversion
        elif conversion[1] == 'microgram':
            conversion.append(units * 1e12)
            return conversion
        elif conversion[1] == 'imperial ton':
            conversion.append(units / 1.016)
            return conversion
        elif conversion[1] == 'US ton':
            conversion.append(units * 1.102)
            return conversion
        elif conversion[1] == 'stone':
            conversion.append(units * 157.473)
            return conversion
        elif conversion[1] == 'pound':
            conversion.append(units * 2204.623)
            return conversion
        elif conversion[1] == 'ounce':
            conversion.append(units * 35273.962)
            return conversion
    while conversion[0] == 'kilogram': # From Kilogram to all other units
        if conversion[1] == 'metric ton':
            conversion.append(units / 1000)
            return conversion
        elif conversion[1] == 'gram':
            conversion.append(units * 1000)
            return conversion
        elif conversion[1] == 'milligram':
            conversion.append(units * 1e6)
            return conversion
        elif conversion[1] == 'microgram':
            conversion.append(units * 1e9)
            return conversion
        elif conversion[1] == 'imperial ton':
            conversion.append(units / 1016.047)
            return conversion
        elif conversion[1] == 'US ton':
            conversion.append(units / 907.185)
            return conversion
        elif conversion[1] == 'stone':
            conversion.append(units / 6.35)
            return conversion
        elif conversion[1] == 'pound':
            conversion.append(units * 2.205)
            return conversion
        elif conversion[1] == 'ounce':
            conversion.append(units * 35.274)
            return conversion
    while conversion[0] == 'gram': # From Gram to all other units
        if conversion[1] == 'metric ton':
            conversion.append(units / 1e6)
            return conversion
        elif conversion[1] == 'kilogram':
            conversion.append(units / 1000)
            return conversion
        elif conversion[1] == 'milligram':
            conversion.append(units * 1000)
            return conversion
        elif conversion[1] == 'microgram':
            conversion.append(units * 1e6)
            return conversion
        elif conversion[1] == 'imperial ton':
            conversion.append(units / 1.016e6)
            return conversion
        elif conversion[1] == 'US ton':
            conversion.append(units / 907184.74)
            return conversion
        elif conversion[1] == 'stone':
            conversion.append(units / 6350.293)
            return conversion
        elif conversion[1] == 'pound':
            conversion.append(units / 453.592)
            return conversion
        elif conversion[1] == 'ounce':
            conversion.append(units / 28.35)
            return conversion
    while conversion[0] == 'milligram': # From Milliram to all other units
        if conversion[1] == 'metric ton':
            conversion.append(units / 1e9)
            return conversion
        elif conversion[1] == 'kilogram':
            conversion.append(units / 1e6)
            return conversion
        elif conversion[1] == 'gram':
            conversion.append(units / 1000)
            return conversion
        elif conversion[1] == 'microgram':
            conversion.append(units * 1e6)
            return conversion
        elif conversion[1] == 'imperial ton':
            conversion.append(units / 1.016e9)
            return conversion
        elif conversion[1] == 'US ton':
            conversion.append(units / 9.072e8)
            return conversion
        elif conversion[1] == 'stone':
            conversion.append(units / 6.35e6)
            return conversion
        elif conversion[1] == 'pound':
            conversion.append(units / 453592.37)
            return conversion
        elif conversion[1] == 'ounce':
            conversion.append(units / 28349.523)
            return conversion
    while conversion[0] == 'microgram': # From Microgram to all other units
        if conversion[1] == 'metric ton':
            conversion.append(units / 1e12)
            return conversion
        elif conversion[1] == 'kilogram':
            conversion.append(units / 1e9)
            return conversion
        elif conversion[1] == 'gram':
            conversion.append(units / 1e6)
            return conversion
        elif conversion[1] == 'milligram':
            conversion.append(units / 1000)
            return conversion
        elif conversion[1] == 'imperial ton':
            conversion.append(units / 1.016e12)
            return conversion
        elif conversion[1] == 'US ton':
            conversion.append(units / 9.072e11)
            return conversion
        elif conversion[1] == 'stone':
            conversion.append(units / 6.35e9)
            return conversion
        elif conversion[1] == 'pound':
            conversion.append(units / 4.536e8)
            return conversion
        elif conversion[1] == 'ounce':
            conversion.append(units / 2.835e7)
            return conversion
    while conversion[0] == 'imperial ton': # From Imperial Ton to all other units
        if conversion[1] == 'metric ton':
            conversion.append(units * 1.016)
            return conversion
        elif conversion[1] == 'kilogram':
            conversion.append(units * 1016.047)
            return conversion
        elif conversion[1] == 'gram':
            conversion.append(units * 1.016e6)
            return conversion
        elif conversion[1] == 'milligram':
            conversion.append(units * 1.016e9)
            return conversion
        elif conversion[1] == 'microgram':
            conversion.append(units * 1.016e12)
            return conversion
        elif conversion[1] == 'US ton':
            conversion.append(units * 1.12)
            return conversion
        elif conversion[1] == 'stone':
            conversion.append(units * 160)
            return conversion
        elif conversion[1] == 'pound':
            conversion.append(units * 2240)
            return conversion
        elif conversion[1] == 'ounce':
            conversion.append(units * 35840)
            return conversion
    while conversion[0] == 'US ton': # From US Ton to all other units
        if conversion[1] == 'metric ton':
            conversion.append(units / 1.102)
            return conversion
        elif conversion[1] == 'kilogram':
            conversion.append(units * 907.185)
            return conversion
        elif conversion[1] == 'gram':
            conversion.append(units * 907184.74)
            return conversion
        elif conversion[1] == 'milligram':
            conversion.append(units * 9.072e8)
            return conversion
        elif conversion[1] == 'microgram':
            conversion.append(units * 9.072e11)
            return conversion
        elif conversion[1] == 'imperial ton':
            conversion.append(units / 1.12)
            return conversion
        elif conversion[1] == 'stone':
            conversion.append(units * 142.857)
            return conversion
        elif conversion[1] == 'pound':
            conversion.append(units * 2000)
            return conversion
        elif conversion[1] == 'ounce':
            conversion.append(units * 32000)
            return conversion
    while conversion[0] == 'stone': # From Stone to all other units
        if conversion[1] == 'metric ton':
            conversion.append(units / 157.473)
            return conversion
        elif conversion[1] == 'kilogram':
            conversion.append(units * 6.35)
            return conversion
        elif conversion[1] == 'gram':
            conversion.append(units * 6350.293)
            return conversion
        elif conversion[1] == 'milligram':
            conversion.append(units * 6.35e6)
            return conversion
        elif conversion[1] == 'microgram':
            conversion.append(units * 6.35e9)
            return conversion
        elif conversion[1] == 'imperial ton':
            conversion.append(units / 160)
            return conversion
        elif conversion[1] == 'US ton':
            conversion.append(units / 142.857)
            return conversion
        elif conversion[1] == 'pound':
            conversion.append(units * 14)
            return conversion
        elif conversion[1] == 'ounce':
            conversion.append(units * 224)
            return conversion
    while conversion[0] == 'pound': # From Pound to all other units
        if conversion[1] == 'metric ton':
            conversion.append(units / 2204.623)
            return conversion
        elif conversion[1] == 'kilogram':
            conversion.append(units / 2.205)
            return conversion
        elif conversion[1] == 'gram':
            conversion.append(units * 453.592)
            return conversion
        elif conversion[1] == 'milligram':
            conversion.append(units * 453592.37)
            return conversion
        elif conversion[1] == 'microgram':
            conversion.append(units * 4.536e8)
            return conversion
        elif conversion[1] == 'imperial ton':
            conversion.append(units / 2240)
            return conversion
        elif conversion[1] == 'US ton':
            conversion.append(units / 2000)
            return conversion
        elif conversion[1] == 'stone':
            conversion.append(units / 14)
            return conversion
        elif conversion[1] == 'ounce':
            conversion.append(units * 16)
            return conversion
    while conversion[0] == 'ounce': # From Ounce to all other units
        if conversion[1] == 'metric ton':
            conversion.append(units / 35273.962)
            return conversion
        elif conversion[1] == 'kilogram':
            conversion.append(units / 35.274)
            return conversion
        elif conversion[1] == 'gram':
            conversion.append(units * 28.35)
            return conversion
        elif conversion[1] == 'milligram':
            conversion.append(units * 28349.523)
            return conversion
        elif conversion[1] == 'microgram':
            conversion.append(units * 2.835e7)
            return conversion
        elif conversion[1] == 'imperial ton':
            conversion.append(units / 35840)
            return conversion
        elif conversion[1] == 'US ton':
            conversion.append(units / 32000)
            return conversion
        elif conversion[1] == 'stone':
            conversion.append(units / 224)
            return conversion
        elif conversion[1] == 'pound':
            conversion.append(units / 16)
            return conversion

def mass_conv():
    print('\nYou have chosen MASS\n')
    x = mass_calc()
    print('\nRESULT:\n  {:.2f} {} = {:.2f} {}:'.format(x[2],x[0],x[3],x[1]))