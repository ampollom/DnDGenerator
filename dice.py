#from curses.ascii import isdigit
import random
import pandas as pd
import openpyxl
arr = []

#checks if input is an integer
def is_integer(n):
    return isinstance(n,int)

#generates a psuedo-random number between 1 and 20 and puts it in an array
def roll_dice(input_string):

    if is_integer(input_string) != True:
        print("Is not a digit")
    else:

        while input_string != 0:
            dice_value = random.randrange(1, 21)
            arr.append(dice_value)
            input_string = input_string - 1
    print(arr)
    read_spreadsheet(arr)

def read_spreadsheet(arr):
    df = pd.read_excel('gold.xlsx')
    items = []

    while len(arr) != 0:
        num = arr[0]
        column_input = input("What column are you looking for? gold, weapons, random_items, food, or spell_scrolls: ")
        s = df.loc[num-1, column_input]
        items.append(s)
        del arr[0]
    print()
    for i in items:
        print(i)


num_of_dice = int(input("How many dice do you want to roll?: "))
roll_dice(num_of_dice)
