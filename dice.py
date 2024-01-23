
import random
import pandas as pd
import pyarrow

arr = []
name_num = 1006
item_num = 21

#checks if input is an integer
def is_integer(n):
    return isinstance(n,int)

#generates a psuedo-random number between 1 and 20 and puts it in an array
def roll_dice(input_string):

    filename = ""
    if is_integer(input_string) != True:
        print("Is not a digit")
        roll_dice()
    else:
        pickasheet = input("What are you rolling for? Names or Items?: ").lower()
        if (pickasheet == 'names'):
            while input_string != 0:
                dice_value = random.randrange(1, name_num)
                arr.append(dice_value)
                input_string = input_string - 1
                filename = "names.xlsx"
        else:
            while input_string != 0:
                dice_value = random.randrange(1, item_num)
                arr.append(dice_value)
                input_string = input_string - 1
                filename = "gold.xlsx"
    #print(arr)
    read_spreadsheet(arr, filename)

#reads and pulls items from spreadsheet
def read_spreadsheet(arr, filename):

    df = pd.read_excel(filename)
    items = []

    print("You can choose from the following options: girl_names, boy_names, spell_scrolls, gold"
          "random_items, weapons, or food.")

    while len(arr) != 0:
        num = arr[0]
        column_input = input("What are you looking for?: ")
        s = df.loc[num-1, column_input]
        items.append(s)
        del arr[0]
    print_items(items)

#prints items
def print_items(items):

    print()
    print("***********************************")
    print("Found following items:")
    for i in items:
        print(i)
    print("***********************************")
    print()
    reroll_dice()

def reroll_dice():
    s = input("Would you like to reroll [y/N]: ")
    s = s.lower()

    if s == 'y':
        run_program()
    elif s == 'n':
        print("Thanks for rolling!")
    else:
        print("Not a valid option")
        reroll_dice()


def run_program():
    num_of_dice = int(input("How many dice do you want to roll?: "))
    roll_dice(num_of_dice)

