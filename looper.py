import csv 
from tkinter import *
from tkinter import filedialog

location_name = input('Enter you locations: ')
locations = location_name.split(' ' or ',')
location_type = 'Work in progress'
facility = 'Augusta'

isShipping= input("IsShipping? True or False? Type T or F: ").lower().strip()
if isShipping == 't':
    isShipping = 'True'
elif isShipping == 'f':
    isShipping = 'False'
else:
    print('Error: Input must be T or F')
    exit()

isReceiving = input("IsReceiving? True or False? Type T or F: ").lower().strip()
if isReceiving == 't':
    isReceiving = 'True'
elif isReceiving == 'f':
    isReceiving = 'False'
else:
    print('Error: Input must be T or F')
    exit()

specifics = input('No specific details? True or False? Type T or F: ').lower().strip()
if specifics == 't':
    isRepair = 'False'
    isHarvest = 'False'
    isHarvestPMove = 'False'
    isHarvestCMove = 'False'
elif specifics == 'f':
    isRepair = input("IsRepair? True or False? Type T or F: ").lower().strip()
    if isRepair== 't':
        isRepair = 'True'
    elif isRepair == 'f':
        isRepair = 'False'
    else:
        print('Error: Input must be T or F')
        exit()

    isHarvest = input("IsHarvest? True or False? Type T or F: ").lower().strip()
    if isHarvest == 't':
        isHarvest = 'True'
    elif isHarvest == 'f':
        isHarvest = 'False'
    else:
        print('Error: Input must be T or F')
        exit()

    isHarvestPMove = input("IsHarvestParentMove? True or False? Type T or F: ").lower().strip()
    if isHarvestPMove == 't':
        isHarvestPMove = 'True'
    elif isHarvestPMove == 'f':
        isHarvestPMove = 'False'
    else:
        print('Error: Input must be T or F')
        exit()

    isHarvestCMove = input("IsHarvestComponentMove? True or False? Type T or F: ").lower().strip()
    if isHarvestCMove == 't':
        isHarvestCMove = 'True'
    elif isHarvestCMove == 'f':
        isHarvestCMove = 'False'
    else:
        print('Error: Input must be T or F')
        exit()
else: 
    print('Error: Input must be T or F')
    exit()

increments = input('Increment by: ')
increments_int = int(increments)
answer = []
for i in range(len(locations)):
    single = locations[i]
    name_split = single.split("-")
    converted_num = int(name_split[3])
    print(single)
    f = open('template.csv', 'a', newline='')
    writer = csv.writer(f)
    writer.writerow([single, single, location_type, facility, isShipping, isReceiving, isHarvest, isHarvestPMove, isHarvestCMove])
    for converted_num in range(increments_int):
        num = converted_num + 1
        double_digit = f'{num:02d}'
        name_split[3] = double_digit
        answer = '-'.join(name_split)
        # with open('test.csv', 'a') as f:
        #     writer = csv.writer(f)
        #     writer.writerow([answer])
        writer.writerow([answer, answer, location_type, facility, isShipping, isReceiving, isHarvest, isHarvestPMove, isHarvestCMove])
        print(answer)
    f.close()
        

        

