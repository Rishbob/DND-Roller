# -----------------------------------------------------------------------------
# Name:        DNDRoller (main.py)
# Purpose:     Rolls all possible dice needed for a DnD campaign, including specific amounts of a certain die.
#
# Author:      813403
# Created:     03-05-2020
# Updated:     03-13-2020
# -----------------------------------------------------------------------------
from random import randint  # imports random number generation
import time
import sys
import re

max_dice_values = ['4', '6', '8', '10', '12', '20', '100']  # contains maximum values for each die type
wild_magic_list = ["A random creature within 60 feet of you becomes poisoned for 1d4 hours.", "Up to three creatures you choose within 30 feet of you take 4d10 lightning damage.", "Your height changes by 1d10 inches equal to the roll. If the roll is odd, you shrink. If the roll is even, you grow.", "You cast Magic Missile as a 5th-level spell."]
menu_dice_values = ['1','2','3','4','5','6','7'] # contains menu values of dice
monster_class = ["DRAGON","BEAST",'ANGEL',"DEMON"]
enemy_list = []
roll_natural = bool # Determines whether to append "Natural" to result

def DiceRoll(max_dice,roll_status): #Function to determine the roll value, input is the maximum dice value
    roll_natural = False
    max_dice_int = int(max_dice)  # Converts maximum dice value (previously a string) into an int
    roll_value = randint(1, max_dice_int)# Rolls the dice, with the upper limit being the the highest value on the selected dice
    damage_sum = roll_value
    if roll_status in ["advantage", "Advantage"]: # If the roller wishes to have advantage on the roll
      roll_value_2 = randint(1,max_dice_int)
      print ("Roll 1:", roll_value)
      print ("Roll 2:", roll_value_2)
      if roll_value_2 > roll_value:
        roll_value = roll_value_2
        damage_sum = roll_value_2
    elif roll_status in ["disadvantage", "Disadvantage"]: # If the roller wishes to have disadvantage on the roll
      roll_value_2 = randint(1,max_dice_int)
      damage_sum = roll_value_2
      print ("Roll 1:", roll_value)
      print ("Roll 2:", roll_value_2)
      if roll_value_2 < roll_value:
        roll_value = roll_value_2
        damage_sum = roll_value_2
    if roll_value == 1 or roll_value == max_dice_int:
        roll_natural = True
    roll_value = str(roll_value) + "," + str(damage_sum)
    return roll_value  # Returns the value of the roll


#Ask for CR of target monster, ask general type of monster: draws string from list containing monsters
def battleline(challenge_rating, type, damage):
    challenge_rating = str(challenge_rating)
    damage = str(damage)
    action = str()
    type = str(type)
    if type in monster_class:
        action = "You hit " + challenge_rating +" "+ type.lower() + "(s) for " + (str(int(int(damage) / int(challenge_rating)))) + " damage each."
    return action
65
#Dice input function (while input is invalid, keep looping)
def dice_selector(dice_input):
  if re.findall("[^1-7]",dice_input):
      print("Invalid input. Please re-enter.")
      dice_input = input("What type of dice do you wish to roll?\n1. D4\n2. D6\n3. D8\n4. D10\n5. D12\n6. D20\n7. D100").lstrip()
      dice_input = dice_selector(dice_input)
  dice_input = int(dice_input)
  return dice_input

def wild_magic(dice_roll, roll_confirm): #Add roll confirmation value
    i = 1 #iterator for certain inputs
    dice_roll = int(dice_roll)
    roll_confirm = roll_confirm.lower()
    result_dice = 0
    result = str
    if 1 <= dice_roll <= 25: #1 if and 3 elif statements to determine what out come will occur: 1-25 poisons, 26-50 deals lighting damage, 51-75 changes size and 76-100 throws darts.
        result = (wild_magic_list[0])
        if roll_confirm.find('y') == 0: #If player wishes to roll, program will do so automatically
            result_dice = randint(1,4)
            result = result[:60]
            result = result + str(" ") + str(i) + str(" hour(s).") #Slices result_dice into result
    elif 26 <= dice_roll <= 50:
        result = (wild_magic_list[1])
        if roll_confirm.find("y") == 0:
            while i <= 4:
                result = result[:60]
                result_dice = randint(1,10) + result_dice
                i = i+1
            result = result + str(result_dice) + str(" lighting damage.")
    elif 51 <= dice_roll <= 75:
        result = (wild_magic_list[2])
        if roll_confirm.find("y") == 0:
            result = result[:10]
            result_dice = randint(1,10)
            if result_dice % 2 == 0:
                result = result + str(" grow ") + str(result_dice) + str(" inches (") + str(float(result_dice*2.54)) + str("cm).")
            else:
                result = result + str(" shrink ") + str(result_dice) + str(" inches (") + str(float(result_dice * 2.54)) + str("cm).")
    elif 76 <= dice_roll <= 100:
        result = (wild_magic_list[3])
        if roll_confirm.find("y") == 0:
            while i <= 5:
                result_dice = randint(1,4) + result_dice + 1
                i = i+1
        result = result + str(" It does ") + str(result_dice) + str(" damage.")
    return(result)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Program start
dice_max_int = str
looper = str("Yes")
dice_type = ""
damage_sum = 0
print("Initializing...")
time.sleep(0.5)
print("Dice Roller initialized.")
while looper in ["Yes", "Y"]:
    tutorial_confirm = input("Do you want a tutorial?").lower() #Tutorial: shows how program works and gives definitions for user
    while tutorial_confirm in ("yes", "y"):
        print("Terms:\nDice Naming Convention: 'D' stands for dice, and the number stands for the number of sides (ie. a D6 has 6 sides).\nAdvantage: When rolling for something, you roll two dice and take the higher.\nDisadvantage: When rolling for something, you roll two dice and take the lower.\nNatural: Used to describe when you roll the highest or lowest possible value on a dice (ie. a D20 can roll a Natural 1 and a Natural 20).\nClass/Archetype: Your character's specific abilities. For the purposes of this program it only matters if you are a Wild Magic Sorcerer.\nEnemy Types: The enemies that this program accepts are dragon, beast, angel or demon.")
        print("")
        demo_confirm = input("Do you want to see a demo?").lower()
        if demo_confirm in ("yes", "y"):
            print("This demo assumes the following:\nType of Dice Being Rolled: D8\nNumber of Dice Being Rolled: 1\nAdvantage on all rolls\nClass is not a Wild Magic Sorcerer\nOpponents are 3 dragons.")
            print("")
            demo_start = input("Do you want to start?")
            if demo_start in ("yes", "y"):
                demo = (str(DiceRoll(8,"Advantage")))
                demo = demo[:1]
                if demo in ("1", "8"):
                    print("Natural " + demo)
                print("Roll Value =", demo)
                demo2 = wild_magic(int(demo),"y")
                print(demo2)
                demo3 = battleline(3,"DRAGON",int(demo))
                print(demo3)
                print("")
                tutorial_confirm = input("Do you wish to see this again?")
    dice_max_str = str
    while dice_max_str not in menu_dice_values:
        dice_type = input("What type of dice do you wish to roll?\n1. D4\n2. D6\n3. D8\n4. D10\n5. D12\n6. D20\n7. D100\n ").lstrip() #Startup menu
        dice_max_str = str(dice_selector(dice_type))
        dice_max_int = int(max_dice_values[int(dice_max_str) - 1])
    dice_number = input("How many dice do you wish to roll?")  # Determines how many times the die needs to be rolled
    while re.findall("[^1234567890]", dice_number) or dice_number in [""]:
        dice_number = input("Invalid input. Please input an integer next time. How many dice do you wish to roll?")
    dice_number = int(dice_number)
    advantage_stat = input("Advantage/Disadvantage on rolls?") #Determines if whether the user has advantage or distadvantage on rolls (Roll 2 dice, take higher for advantage and lower for distadvantage)
    n = int(1);  # iterator variable set
    for n in range(0, dice_number):  # Loops the DiceRoll function for the number of dice requested
        result = (DiceRoll(dice_max_int,advantage_stat)) #Search string to remove the second number set (they are seperated by a comma)
        comma_place = result.find(",") #Splits result string based on position of comma
        comma_place = comma_place + 1
        damage_sum = damage_sum + int(result[comma_place:]) #Damage sum increases with each dice roll
        comma_place = comma_place - 1
        result = result[:comma_place] #Removes all values beyond comma before printing dice value (the values beyond the comma are total damage)
        if result in ["1", str(dice_max_int)]:
            print("Natural",result)
        else:
            print(result)
            print("Total Damage: ", damage_sum)
        n = n + 1  # Iterator increases
    dice_max_int = int(dice_max_int)
    if dice_max_int == 100 and dice_number == 1: #Begins to check if wild_magic function should run
        user_class = input("What is your class and archetype?").lower().replace(" ","")
        if user_class.find("wildmagic") >= 0:
            wild_magic_roll_confirmation = input("Do want to automatically roll for damage?")
            print(wild_magic(result,wild_magic_roll_confirmation))
    n = input("Do you want to see what EXACTLY happens?").upper()
    if n in ["YES","Y"]:
        cr = input("How many enemies are there?")
        enemy = input("What type of enemy is being attacked?").upper()
        line = battleline(cr,enemy,damage_sum)
        print(line)
    looper = input("Do you wish to continue?").upper()
    if looper in ["YES", "Y"]:  # Resets the dice type chosen and the number of dice rolled if the user wishes to continue rolling
        dice_type = "Invalid Input: Please input a proper term."#Reset all values for next loop
        dice_number = 0
        dice_max_int = int
        dice_max_str = str
        damage_sum = 0
    else:  # Exit program actions
        print("Shutting down...")
        time.sleep(0.5)
        print("Closed")
        sys.exit()