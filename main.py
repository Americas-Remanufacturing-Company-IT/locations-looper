import PySimpleGUI as sg
from tkinter import filedialog
import csv
result_arr = []

location_types = ['Other', 'Finished Goods', 'Parts', 'Return To Vendor', 'Work In Progress', 'Scrapped']

facilities = ['Augusta', 'IndBlvd', 'MH', 'NS', 'OR', 'Other' ]

headers = ['Location', 'Description', 'LocationType', 'Facility', 'IsShipping', 'IsReceiving', 'IsRepair', 'IsHarvest', 'IsHarvestParentMove', 'IsHarvestComponentMove']

beginning = ['WA', 'IB', 'OR', 'GH', 'NS']

ToF = ['True', 'False']

sg.theme('BlueMono')
POPUP_CENTER_X = 200
POPUP_CENTER_Y = 50

top_array = {'-A1-': sg.Input(key='-A1-', size=(3, 1),enable_events=True),
     '-H1-' : sg.Text('-', font=(None, 20)), 
     '-A2-' : sg.Input(key='-A2-', pad=(0, 0), size=(3, 1),enable_events=True), 
     '-H2-' : sg.Text('-', font=(None, 20)), 
     '-A3-': sg.Input(key='-A3-', pad=(0,0), size=(3, 1), enable_events=True), 
     '-H3-' : sg.Text('-', font=(None, 20)),  
     '-A4-' : sg.Input(key='-A4-', pad=(0,0), size=(3, 1), enable_events=True), 
     '-H4-' : sg.Text('-', font=(None, 20)), 
     '-A5-' : sg.Input(key='-A5-', pad=(0,0), size=(3, 1), enable_events=True)}
bottom_array = {'-B1-' : sg.Input(key='-B1-', size=(3, 1), enable_events=True, readonly=True),
     '-H1-' : sg.Text('-', font=(None, 20)), 
     '-B2-' : sg.Input(key='-B2-', pad=(0, 0), size=(3, 1), enable_events=True), 
     '-H2-' : sg.Text('-', font=(None, 20)), 
     '-B3-' : sg.Input(key='-B3-', pad=(0,0), size=(3, 1), enable_events=True), 
     '-H3-' : sg.Text('-', font=(None, 20)), 
     '-B4-' : sg.Input(key='-B4-', pad=(0,0), size=(3, 1), enable_events=True), 
     '-H4-' : sg.Text('-', font=(None, 20)), 
     '-B5-' : sg.Input(key='-B5-', pad=(0,0), size=(3, 1), enable_events=True)}
layout = [[*top_array.values()],
 [*bottom_array.values()],
 [sg.Text('Location: ', font=(None, 12), size=(13, 1)), sg.Text('Facility: ', font=(None, 12))],
 [sg.Combo(location_types, key='-locType-', size=(17, 1), default_value='Other', readonly=True), sg.Combo(facilities, key='-facility-', size=(17, 1), default_value='Augusta', readonly=True)], 
 [sg.Text('Shipping: ', font=(None, 12), size=(13, 1)), sg.Text('Receiving: ', font=(None, 12))],
 [sg.Combo(ToF, key='-shipping-', size=(17, 1), default_value='False', readonly=True), sg.Combo(ToF, key='-receiving-', size=(17, 1), default_value='False', readonly=True)], 
 [sg.Text('Repair: ', font=(None, 12), size=(13, 1)), sg.Text('Harvest: ', font=(None, 12))],
 [sg.Combo(ToF, key='-repair-', size=(17, 1), default_value='False', readonly=True), sg.Combo(ToF, key='-harvest-', size=(17, 1), default_value='False', readonly=True)],
 [sg.Text('Harvest Parent: ', font=(None, 12), size=(14, 1)), sg.Text('Harvest Component: ', font=(None, 12), size=(20, 1))],
 [sg.Combo(ToF, key='-harvestP-', size=(17, 1), default_value='False', readonly=True), sg.Combo(ToF, key='-harvestC-', size=(17, 1), default_value='False', readonly=True)],
 [sg.Button('Generate Locations', pad=(0, 10)), sg.Exit()]]

window = sg.Window('Location Looper', layout, keep_on_top=True, enable_close_attempted_event=True)

def main():
    while True:

        event, values = window.read()

        loc_type = values['-locType-']
        facility = values['-facility-']
        shipping = values['-shipping-']
        receiving = values['-receiving-']
        repair = values['-repair-']
        harvest = values['-harvest-']
        harvestP = values['-harvestP-']
        harvestC = values['-harvestC-']
        if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, 'Exit') and sg.popup_yes_no('Are you sure you want to quit?',title='',location=window.CurrentLocation(), relative_location=(POPUP_CENTER_X,POPUP_CENTER_Y),keep_on_top=True) == 'Yes':
            break

        elif event == '-A1-':
            a1_value = window[event].get()
            b1_input = window['-B1-']
            b1_input.update(value=a1_value.replace('-A', '-B'))
        elif event == '-A2-':
            a2_value = window[event].get()
            b2_input = window['-B2-']
            char_list = list(a2_value)
            if char_list:
                char_list.pop()
                new_string = ''.join(char_list).replace('-A', '-B', 1)
                b2_input.update(value=new_string)
            else:
                b2_input.update(value='')
        elif event == '-A5-':
            a1_value = window[event].get()
            b1_input = window['-B5-']
            b1_input.update(value=a1_value.replace('-A', '-B'))
        elif event == 'Generate Locations':
            a2_value = values['-A2-'].upper()
            b2_value = values['-B2-'].upper()
            a2_list = list(a2_value)
            b2_list = list(b2_value)
            start = ord(a2_list.pop())
            end = ord(b2_list.pop())
            for i in range(start, end+1):
                letter = chr(i)
                a2_list.append(letter)
                joinStr = ''.join(a2_list)
                a2_list.pop()
                # print(joinStr)
                a3_value = int(values['-A3-'])
                b3_value = int(values['-B3-'])
                for j in range(a3_value, b3_value+1):
                    if j < 10:
                        j_str = '0' + str(j)
                    else:
                        j_str = str(j)
                    # print(j_str)
                    a4_value = int(values['-A4-'])
                    b4_value = int(values['-B4-'])
                    for k in range(a4_value, b4_value+1):
                        full_loc = []
                        inner_arr = []
                        if k < 10:
                            k_str = '0' + str(k)
                        else:
                            k_str = str(k)
                        full_loc.append(values['-A1-'])
                        full_loc.append(joinStr)
                        full_loc.append(j_str)
                        full_loc.append(k_str)
                        full_loc.append(values['-A5-'])
                        name_join = '-'.join(full_loc)
                        # print(name_join)
                        inner_arr.append(name_join)
                        inner_arr.append(name_join)
                        inner_arr.append(loc_type)
                        inner_arr.append(facility)
                        inner_arr.append(shipping)
                        inner_arr.append(receiving)
                        inner_arr.append(repair)
                        inner_arr.append(harvest)
                        inner_arr.append(harvestP)
                        inner_arr.append(harvestC)
                        result_arr.append(inner_arr)
            # print(result_arr)
            if event == 'Generate Locations' and sg.popup_yes_no('Do you want to generate more locations',title='',location=window.CurrentLocation(), relative_location=(POPUP_CENTER_X,POPUP_CENTER_Y),keep_on_top=True) == 'Yes':
                for x in ['-A1-', '-A2-', '-A3-', '-A4-', '-A5-', '-B1-', '-B2-', '-B3-', '-B4-', '-B5-']:
                 window[x].update('')
            else:
                file_path = filedialog.asksaveasfilename(defaultextension='.csv')
                with open(file_path, 'w', newline='') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow(headers)
                    for x in result_arr:
                        writer.writerow(x) 

            

if __name__  == '__main__':
    main()