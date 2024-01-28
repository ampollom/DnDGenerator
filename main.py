from PySimpleGUI import HorizontalSeparator
import dice
import PySimpleGUI as sg
import os
from PIL import Image, ImageTk
import io


#sg.preview_all_look_and_feel_themes()
#GUI Theme
sg.theme('darkgreen1')

#SPIN Counter
num_of_dice = [i for i in range(1, 21)]
dicenum = sg.Spin(num_of_dice, initial_value=1, readonly=True,  size=5, enable_events=True, key='-DICE-')

#Layout of Initial GUI
layout = [[sg.Text("Choose your generator:")],
           [sg.Radio("Names","RADIO1", enable_events=True, key='R1', default=False),
            sg.Radio("Loot","RADIO1", enable_events=True, key='R2', default=False)],
            [sg.HorizontalSeparator(color = None)],
          [sg.Text("How many dice are you rolling?"), dicenum],
            [sg.HorizontalSeparator(color = None)],
            [sg.Checkbox("Girl Names", default=False, enable_events=True, key="gnames"),
             sg.Checkbox("Boy Names", default=False, enable_events=True, key="bnames")],
             [sg.Checkbox("Gold", default=False, enable_events=True, key="gold"),
             sg.Checkbox("Spell Scrolls", default=False, enable_events=True, key="sscrolls"),
             sg.Checkbox("Food", default=False, enable_events=True, key="food"),
             sg.Checkbox("Random Items", default=False, enable_events=True, key="ritems"),
             sg.Checkbox("Weapons", default=False, enable_events=True, key="weapons"),
             sg.Checkbox("Nice Items", default=False, enable_events=True, key="nitems")],
            [sg.HorizontalSeparator(color = None)],
          [sg.Text("Here is what we found:")],[sg.Output(size=[20,5])],
          [sg.Button("OK"), sg.Button("Reroll"), sg.Button("Exit")],],

#GUI Window

window = sg.Window("Dungeons and Dragons Generator", layout)


#Events
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "OK":
        filename = ''
        dicerolled = int(values['-DICE-'])
        if values['R1'] == True:
            filename = "names.xlsx"
            girl_names = 0
            boy_names = 0

            if values['gnames'] == True:
                girl_names = int(sg.popup_get_text("How Many Girls?: "))
            if values['bnames'] == True:
                boy_names = int(sg.popup_get_text("How Many Boys? "))
            name_dict = {"girl_names":girl_names,
                    "boy_names":boy_names}
            #print(name_list)
            dice.roll_dice(dicerolled, filename, name_dict)

        elif values['R2'] == True:
            filename = "gold.xlsx"
            gold = 0
            sscrolls = 0
            food = 0
            weapons = 0
            ritems = 0
            nitems = 0
            if values["gold"] == True:
                gold = int(sg.popup_get_text("How much gold?"))
            if values["sscrolls"] == True:
                sscrolls = int(sg.popup_get_text("How many Spell Scrolls?"))
            if values["food"] == True:
                food = int(sg.popup_get_text("How many Spell Scrolls?"))
            if values["weapons"] == True:
                weapons = int(sg.popup_get_text("How many weapons?"))
            if values["ritems"] == True:
                ritems = int(sg.popup_get_text("How many random items?"))
            if values["nitems"] == True:
                nitems = int(sg.popup_get_text("How many nice items?"))
            items_dict = {"gold": gold,
                          "spell_scrolls": sscrolls,
                          "food": food,
                          "weapons_shitty":weapons,
                          "random_items_shitty": ritems,
                          "nice_items": nitems}
            #print(items_dict)
            items = dice.roll_dice(dicerolled, filename, items_dict)
            #for item in items:
                #print(item)
            sg.popup_yes_no("Do you want to reroll?", title="Reroll?")


        #print(filename)
        #print(dicerolled)
        #dice.roll_dice(dicerolled, filename)




window.close()





#dice.run_program()
