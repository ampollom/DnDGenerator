import random
import pandas as pd
import pyarrow
from functools import lru_cache

arr = []
name_num = 1007
item_num = 21

#checks if input is an integer
def is_integer(n):
    return isinstance(n,int)

#generates a psuedo-random number between 1 and 20 and puts it in an array
def roll_dice(input_string, filename, dict):

    #filename = ""
    if is_integer(input_string) != True:
        print("Is not a digit")
        roll_dice()
    else:
        #pickasheet = input("What are you rolling for? Names or Items?: ").lower()
        if (filename == 'names.xlsx'):
            #filename = "names.xlsx"
            while input_string != 0:
                dice_value = random.randrange(1, name_num)
                arr.append(dice_value)
                input_string = input_string - 1

        elif (filename == "gold.xlsx" or filename == "randomencounters.xlsx"):
            while input_string != 0:
                dice_value = random.randrange(1, item_num)
                arr.append(dice_value)
                input_string = input_string - 1

    #print(arr)
    read_spreadsheet(arr, filename, dict)
    #return arr


#@lru_cache(maxsize=100)
#reads and pulls items from spreadsheet
def read_spreadsheet(arr, filename, dict):

    df = pd.read_excel(filename)
    items = []
    dict_keys =dict.keys()
    dict_values = dict.values()
    #print(dict_keys)
    #print(dict_values)

    while len(arr) != 0:
        for (i,j) in zip(dict_keys, dict_values):
            #print(i)
            #print(j)
            key= i
            counter = j
            #print(counter)
            while counter != 0:
                num = arr[0]
                s = df.loc[num-1,key]
                #print(s)
                items.append(s)
                counter = counter-1
                del arr[0]
    print_items(items)
    #return items

#prints items
def print_items(items):
    print("********************")
    for item in items:
        print(item)
    print("********************\n")
    #reroll_dice()

def reroll_dice():
    s = input("Would you like to reroll [y/N]: ")
    s = s.lower()

    if s == 'y':
        run_program()
    elif s == 'n':
        print("Thanks for rolling!")
        exit(0)
    else:
        print("Not a valid option")
        reroll_dice()


#def run_program():
    #num_of_dice = int(input("How many dice do you want to roll?: "))
    #roll_dice(num_of_dice)





#sg.Button('Ok'), sg.Button('Cancel')]