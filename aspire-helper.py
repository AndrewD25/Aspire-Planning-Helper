"""
Automation
Student Project
Project Title: Aspire Camp Schedule Planning Helper
"""

## -- Setup -- ##

#Library
import random 

#Variables
blue_floor_open = ""
obstacles_open = ""
ninja_open = ""
bouncer_open = ""
beams_open = ""
tumbletrak_open = ""
tumblestrip_open = ""
rod1_open = ""
rod2_open = ""
pit_open = ""
bars_open = ""
boys_equip_open = ""
double_mini_open = ""
tramps_open = ""
xbox_open = ""
upstairs_open = ""

## -- Intro -- ##

#Welcome message
print("Hello Coach! Welcome to Aspire!")
print("If you're having trouble reading your schedule, you're not alone.")
print("This program will help you keep track of open stations and even help you come up with game ideas.")
print()

#### --- Part 1: Station Planning --- ###

## -- Calculate how many stations are open -- ##

#Create total stations variable
total_stations = 16

#Decrement by user input
total_stations -= int(input("How many coaches (besides you) are scheduled to work today? "))
print()

#Print number of open stations
if total_stations > 1:
    print("There should be " + str(total_stations) + " stations open today for you to go to.")
else:
    print("There should be 1 station open today for you to go to.")
print()

## -- Find which stations are open -- ##

#Ask if anyone is at each station
blue_floor_open = input("Is the blue floor open right now? ")
obstacles_open = input("Is obstacles open right now? ")
ninja_open = input("Is ninja open right now? ")
bouncer_open = input("Is bouncer open right now? ")
beams_open = input("Is beams open right now? ")
tumbletrak_open = input("Is tumbletrak open right now? ")
tumblestrip_open = input("Is tumblestrip open right now? ")
rod1_open = input("Is rod 1 open right now? ")
rod2_open = input("Is rod 2 open right now? ")
pit_open = input("Is pit open right now? ")
bars_open = input("Is bars open right now? ")
boys_equip_open = input("Is boys equipment open right now? ")
double_mini_open = input("Is double mini open right now? ")
tramps_open = input("Is tramps open right now? ")
xbox_open = input("Is Xbox open right now? ")
upstairs_open = input("Is upstairs open right now? ")

#Set each variable to a boolean
blue_floor_open = blue_floor_open == "y" or blue_floor_open == "yes" or blue_floor_open == "Yes"
obstacles_open = obstacles_open == "y" or obstacles_open == "yes" or obstacles_open == "Yes"
ninja_open = ninja_open == "y" or ninja_open == "yes" or ninja_open == "Yes"
bouncer_open = bouncer_open == "y" or bouncer_open == "yes" or bouncer_open == "Yes"
beams_open = beams_open == "y" or beams_open == "yes" or beams_open == "Yes"
tumbletrak_open = tumbletrak_open == "y" or tumbletrak_open == "yes" or tumbletrak_open == "Yes"
tumblestrip_open = tumblestrip_open == "y" or tumblestrip_open == "yes" or tumblestrip_open == "Yes"
rod1_open = rod1_open == "y" or rod1_open == "yes" or rod1_open == "Yes"
rod2_open = rod2_open == "y" or rod2_open == "yes" or rod2_open == "Yes"
pit_open = pit_open == "y" or pit_open == "yes" or pit_open == "Yes"
bars_open = bars_open == "y" or bars_open == "yes" or bars_open == "Yes"
boys_equip_open = boys_equip_open == "y" or boys_equip_open == "yes" or boys_equip_open == "Yes"
double_mini_open = double_mini_open == "y" or double_mini_open == "yes" or double_mini_open == "Yes"
tramps_open = tramps_open == "y" or tramps_open == "yes" or tramps_open == "Yes"
xbox_open = xbox_open == "y" or xbox_open == "yes" or xbox_open == "Yes"
upstairs_open = upstairs_open == "y" or upstairs_open == "yes" or upstairs_open == "Yes"

#Print available stations
print()
print("Here are the available stations: ")

if blue_floor_open:
    print("- Blue Floor")
    
if obstacles_open:
    print("- Obstacles")
    
if ninja_open:
    print("- Ninja")
    
if bouncer_open:
    print("- Bouncer")

if beams_open:
    print("- Beams")
    
if tumbletrak_open:
    print("- Tumbletrak")
    
if tumblestrip_open:
    print("- Tumblestrip")
    
if rod1_open:
    print("- Rod 1")

if rod2_open:
    print("- Rod 2")
    
if pit_open:
    print("- Pit")
    
if bars_open:
    print("- Bars")
    
if boys_equip_open:
    print("- Boys Equipment")

if double_mini_open:
    print("- Double Mini")
    
if tramps_open:
    print("- Tramps")
    
if xbox_open:
    print("- Xbox")
    
if upstairs_open:
    print("- Upstairs")

nothing = not blue_floor_open and not obstacles_open and not ninja_open and not bouncer_open and not beams_open and not tumbletrak_open and not tumblestrip_open and not rod1_open and not rod2_open and not pit_open and not bars_open and not boys_equip_open and not double_mini_open and not tramps_open and not xbox_open and not upstairs_open

if nothing:
    print("Looks like no stations are open right now. How about you ask to share a station with another coach?")
    
print()

#### --- Part 2: Activity Planning --- ####

#Set up variables
rod1 = ""
rod2 = ""
tumblestrip = ""
blue_floor = ""

#Ask which station they would like to go to
station = input("Which station would you like to go to? ")

#Set variables to booleans
rod1 = station == "rod 1" or station == "rod1" or station == "Rod 1"
rod2 = station == "rod 2" or station == "rod2" or station == "Rod 2"
tumblestrip = station == "tumblestrip" or station == "Tumblestrip" or station == "ts"
blue_floor = station == "blue floor" or station == "Blue Floor" or station == "Blue floor" or station == "bluefloor"

#Ask if they would like help if they are going to a rod floor, tumblestrip, or blue floor
if rod1 or rod2 or tumblestrip or blue_floor:
    help = input("Would you like help planning an activity at your station? ")
    print()

    ## -- If they would like help 
    if help == "yes" or help == "y" or help == "Yes" or help == "YES":
        
        ## -- Set up variables for 'help' section -- ##
        random = random.randint(1,2)
        kids = int(input("How many kids are in your group today? "))
        print()
                   
        #Set a variable for if kids is an even number
        even_kids = kids % 2
        even_kids = even_kids == 0
    
        ## -- Calculate An Activity based on the station they chose -- ##
        
        if rod1 or rod2:
            if kids <= 4:
                if random == 1:
                    print("You could ask them about their weekend or about school.")
                else:
                    print("You could take turns telling stories with the kids.")
            elif kids <= 10:
                if random == 1:
                    print("You could play Duck, Duck, Goose.")
                else:
                    print("You could play Down by the Banks.")
            else: #More than 10 kids
                if random == 1:
                    print("You could play the daily activity for " + station)
                else:
                    print("You could play Statues.")
                          
        elif tumblestrip:
            if kids <= 10:
                if random == 1:
                    print("You could play Red Light, Green Light.")
                else:
                    print("You could play Telephone.")
            else: #More than 10 kids
                if random == 1:
                    print("You could play What Time is it Mr. Fox?")
                else:
                    print("You could tell the kids to show you their coolest tricks.")
            
        else: #choice is blue floor
            if kids <= 10:
                if random == 1:
                    print("You could have the kids play with the parachute.")
                else:
                    print("You could have the kids play Sharks and Minnows.")
            else: #More than 10 kids
                if even_kids:
                    print("You could have the kids play Cat and Mouse tag since there is an even number of kids.")
                else:
                    print("You could have the kids play Crab Tag.")
        
    #Print a message if they would not like help
    else:
        print("Good job being creative and coming up with an idea by yourself!")

#Print a conclusion/encouragement message
print()
print("Have fun at " + station + "!")
