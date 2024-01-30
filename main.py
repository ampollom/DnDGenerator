import dice
import PySimpleGUI as sg




keys_to_clear = ['gnames', 'bnames', 'gold', 'weapons', 'sscrolls', 'ritems', 'nitems']
girl_names = 0
boy_names = 0
gold = 0
sscrolls = 0
food = 0
weapons = 0
ritems = 0
nitems = 0
rfoes = 0
nfoes = 0

# sg.preview_all_look_and_feel_themes()

# GUI Theme
sg.theme('darkgreen1')

# SPIN Counter
num_of_dice = [i for i in range(1, 21)]
dicenum = sg.Spin(num_of_dice, initial_value=1,
                  readonly=True, size=5, enable_events=True, key='-DICE-')

# Layout of Initial GUI
layout = [[sg.Text("DnD Generator:")],
          [sg.Radio("Names", "RADIO1", enable_events=True, key='R1', default=False),
           sg.Radio("Loot", "RADIO1", enable_events=True, key='R2', default=False),
           sg.Radio("Encounters", "RADIO1", enable_events=True, key='R3', default=False)],
           [sg.HorizontalSeparator(color=None)],
          [sg.Text("How many dice are you rolling?"), dicenum],
          [sg.HorizontalSeparator(color=None)],
          [sg.Checkbox("Girl Names", default=False, enable_events=True, key="gnames"),
           sg.Checkbox("Boy Names", default=False, enable_events=True, key="bnames")],
            [sg.Checkbox("Gold", default=False, enable_events=True, key="gold"),
           sg.Checkbox("Spell Scrolls", default=False, enable_events=True, key="sscrolls"),
           sg.Checkbox("Food", default=False, enable_events=True, key="food"),
           sg.Checkbox("Random Items", default=False, enable_events=True, key="ritems"),
           sg.Checkbox("Weapons", default=False, enable_events=True, key="weapons"),
           sg.Checkbox("Nice Items", default=False, enable_events=True, key="nitems")],
            [sg.Checkbox("Random Encounters", default=False, enable_events=True, key="rfoes"),
            sg.Checkbox("Number of Foes", default=False, enable_events=True, key="nfoes")],
          [sg.HorizontalSeparator(color=None)],
          [sg.Text("Here is what we found:")], [sg.Output(size=[20, 5])],
          [sg.Button("OK"), sg.Button("Reroll"), sg.Button("Exit")]]


# GUI Window
window = sg.Window("Dungeons and Dragons Generator", layout)

# Events
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "OK":
        dicerolled = int(values['-DICE-'])
        if values['R1'] == True:
            filename = "names.xlsx"
            if values['gnames'] == True:
                girl_names = int(sg.popup_get_text("How Many Girls?: "))
            if values['bnames'] == True:
                boy_names = int(sg.popup_get_text("How Many Boys? "))
            #else:
                #sg.popup_error_with_traceback("Invalid checkbox", "You have chosen an invalid check box")
            name_dict = {"girl_names": girl_names,
                         "boy_names": boy_names}


            dice.roll_dice(dicerolled, filename, name_dict)

        elif values['R2'] == True:
            filename = "gold.xlsx"
            if values["gold"] == True:
                gold = int(sg.popup_get_text("How much gold?"))
            if values["sscrolls"] == True:
                sscrolls = int(sg.popup_get_text("How many spell scrolls?"))
            if values["food"] == True:
                food = int(sg.popup_get_text("How much food?"))
            if values["weapons"] == True:
                weapons = int(sg.popup_get_text("How many weapons?"))
            if values["ritems"] == True:
                ritems = int(sg.popup_get_text("How many random items?"))
            if values["nitems"] == True:
                nitems = int(sg.popup_get_text("How many nice items?"))
            #else:
                #sg.popup_error_with_traceback("Invalid checkbox", "You have chosen an invalid check box")
            items_dict = {"gold": gold,
                      "spell_scrolls": sscrolls,
                      "food": food,
                      "weapons_shitty": weapons,
                      "random_items_shitty": ritems,
                      "random_nice_items": nitems}
            dice.roll_dice(dicerolled, filename, items_dict)

        elif values['R3'] == True:
            filename = "randomencounters.xlsx"
            if values["rfoes"] == True:
                rfoes = int(sg.popup_get_text("How Many Types of Foes?"))
            if values["nfoes"] == True:
                nfoes = int(sg.popup_get_text("How many of each kind of foes?"))
            #else:
                #sg.popup_error_with_traceback("Invalid checkbox", "You have chosen an invalid check box")
            foes_dict = {"number": nfoes,
                      "foes_weak": rfoes}
            dice.roll_dice(dicerolled, filename, foes_dict)

    if event == "Reroll":
        for key in keys_to_clear:
            window[key]('')



window.close()
