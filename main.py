#tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
#pillow
from PIL import Image, ImageTk
#random int lib
import random
#json
import json

class item:
    name = "Dull Sword"
    value = 1

dullSword = item()
dullSword.name = "Dull Sword"
dullSword.value = 1

crown = item()
crown.name = "Crown"
crown.value = 5

#resources
class resources:
    def __init__(self, gold, subjects, soldiers, lumber, stone, castles, towns, taxRate):
        self.gold = gold
        self.subjects = subjects
        self.soldiers = soldiers
        self.lumber = lumber
        self.stone = stone
        self.castles = castles
        self.towns = towns
        self.taxRate = taxRate

playerResources = resources(15, 15, 10, 10, 10, 1, 1, 1)
prepAction = "doNothing"

def turn():
    global prepAction
    if(prepAction == "doNothing"):
        message1.config(text = "You have not selected an action, my liege.")
        return
    elif(prepAction == "mine"):
        mineAction()
    elif(prepAction == "log"):
        loggingAction()
    elif(prepAction == "buildTown"):
        buildTownAction()
    elif(prepAction == "buildCastle"):
        buildCastleAction()
    elif(prepAction == "tax"):
        taxAction()
    elif(prepAction == "crusade"):
        crusadeAction()

    playerResources.gold = playerResources.gold + (playerResources.towns + round(playerResources.subjects / 3))
    playerResources.subjects = playerResources.subjects - ((playerResources.towns * playerResources.taxRate) ** 2)
    if(playerResources.subjects < 0):
        playerResources.subjects = 0
    playerResources.subjects = playerResources.subjects + round(random.randint(0, playerResources.subjects) / 2)

    prepAction = "doNothing"
    updateResources()
    message1.config(text = "What would you like to do next turn, my lord?")

def mineAction():
    playerResources.gold = playerResources.gold - 5
    playerResources.subjects = playerResources.subjects - random.randint(1, 2)
    playerResources.gold = playerResources.gold + random.randint(1, 5)
    playerResources.stone = playerResources.stone + random.randint(10, 20)
    updateResources()

def mineActionPrep():
    if(playerResources.gold < 5):
        message1.config(text = "You do not have the gold to begin a mining expedition, my lord.")
    elif(playerResources.subjects < 2):
        message1.config(text = "You do not have the subjects to begin a mining expedition, my lord.")
    else:
        message1.config(text = "Yes, my lord. We will begin mining when you end your turn.")
        global prepAction
        prepAction = "mine"

def loggingAction():
    playerResources.gold = playerResources.gold - 3
    playerResources.subjects = playerResources.subjects - random.randint(1, 2)
    playerResources.lumber = playerResources.lumber + random.randint(10, 20)
    updateResources()

def loggingActionPrep():
    if(playerResources.gold < 3):
        message1.config(text = "You do not have the gold to begin a logging expedition, my lord.")
    elif(playerResources.subjects < 2):
        message1.config(text = "You do not have the subjects to begin a logging expedition, my lord.")
    else:
        message1.config(text = "Yes, my lord. We will begin logging when you end your turn.")
        global prepAction
        prepAction = "log"

def buildTownAction():
    playerResources.subjects = playerResources.subjects + random.randint(5, 15)
    playerResources.lumber = playerResources.lumber - 50
    playerResources.stone = playerResources.stone - 25
    playerResources.towns = playerResources.towns + 1
    updateResources()

def buildTownActionPrep():
    if(playerResources.lumber < 50):
        message1.config(text = "You do not have the lumber to build a town, my lord.")
    elif(playerResources.stone < 25):
        message1.config(text = "You do not have the stone to build a town, my lord.")
    else:
        message1.config(text = "Yes, my lord. We will build a town when you end your turn.")
        global prepAction
        prepAction = "buildTown"

def taxActionRaise():
    playerResources.taxRate = playerResources.taxRate + 1
    updateResources()

def taxActionLower():
    if(playerResources.taxRate > 0):
        playerResources.taxRate = playerResources.taxRate - 1
    else:
        message1.config(text = "The tax rate cannot be lower than 0, my lord.")
    updateResources()


def buildCastleAction():
        playerResources.subjects = playerResources.subjects - 15
        playerResources.lumber = playerResources.lumber - 30
        playerResources.stone = playerResources.stone - 50
        playerResources.soldiers = playerResources.soldiers + 15
        playerResources.castle = playerResources.castle + 1
        updateResources()

def buildCastleActionPrep():
    if(playerResources.stone < 50):
        message1.config(text = "You do not have enough stone to build a castle, my lord.")
    elif(playerResources.lumber < 30):
        message1.config(text = "You do not have enough lumber to build a castle, my lord.")
    elif(playerResources.subjects < 15):
        message1.config(text = "You do not have enough subjects to train, my lord.")
    else:
        message1.config(text = "Yes, my lord. We will build a castle when you end your turn.")
        global prepAction
        prepAction = "buildCastle"

def crusadeAction():
        playerResources.soldiers = playerResources.soldiers - random.randint(0, 15)
        playerResources.gold = playerResources.gold + random.randint(15, 45)
        updateResources()

def crusadeActionPrep():
    if(playerResources.soldiers < 15):
        message1.config(text = "You do not have enough soldiers to start a crusade, my lord.")
    else:
        message1.config(text = "Yes, my lord. We will begin a crusade when you end your turn.")
        global prepAction
        prepAction = "buildCastle"

def debugWinAction():
    playerResources.gold = 1000
    updateResources()


inventory = [dullSword, crown]

xPrev = 1
def clickResponse():
    x = random.randint(1, 5)
    global xPrev
    if(x == xPrev):
        x = x + 1
    if(x == 1):
        customText = "Many monarchy."
    elif(x == 2):
        customText = "So regal."
    elif(x == 3):
        customText = "Much kingly."
    elif(x == 4):
        customText = "Very fantasy."
    else:
        customText = inventory[random.randint(0, (len(inventory) - 1))].name + "."
    message1.config(text = customText)
    xPrev = x

def advisorNameGen():
    advisorNameList = ["Emphion", "Corvo", "Parvati", "Eliza", "Glados", "Morokei", "Poppy", "Burch", "Alex", "Emily", "Colville", "Meganz", "Leslie", "Ramos"]
    x = random.randint(0, (len(advisorNameList) - 1))
    return advisorNameList[x]

#root/main window geometry and setup
root = tk.Tk()
root.title("mainProgram")
root.iconbitmap('assets\squids\squid.ico')
root.rowconfigure(0, weight = 2)
root.rowconfigure(1, weight = 5)
upperFrame = ttk.Frame(root)
lowerFrame = ttk.Frame(root)
upperFrame.grid(column = 0, row = 0)
lowerFrame.grid(column = 0, row = 1)

#grid geometry for the lowerFrame
lowerFrame.rowconfigure(0, weight = 1)
lowerFrame.rowconfigure(1, weight = 1)
lowerFrame.rowconfigure(2, weight = 1)
lowerFrame.rowconfigure(3, weight = 1)
lowerFrame.columnconfigure(0, weight = 1)
lowerFrame.columnconfigure(1, weight = 1)
lowerFrame.columnconfigure(2, weight = 1)
lowerFrame.columnconfigure(3, weight = 1)
lowerFrame.columnconfigure(4, weight = 1)

#messages
advisorName = "Bren"
advisorName = advisorNameGen()
message = ttk.Label(upperFrame, text = "Local Lord")
message.pack()
message1 = ttk.Label(upperFrame, text = "Why haven't you pressed me yet?")
message1.pack()
message2 = ttk.Label(upperFrame, text = "I am " + advisorName + " the advisor. At your service, my liege.")
message2.pack()
resourceDescription = ttk.Label(upperFrame, text = "Gold = " + str(playerResources.gold) + "\nSubjects = " + str(playerResources.subjects) + "\nSoldiers = " + str(playerResources.soldiers) + "\nLumber = " + str(playerResources.lumber) + "\nStone = " + str(playerResources.stone))
resourceDescription.pack(
    expand = True,
    side = "left"
)
resourceDescription2 = ttk.Label(upperFrame, text = "Castles = " + str(playerResources.castles) + "\nTowns = " + str(playerResources.towns) + "\nTax Rate = " + str(playerResources.taxRate))
resourceDescription2.pack(
    expand = True,
    side = "left"
)

def gameEnd():
        mineButton.grid_forget()
        loggingButton.grid_forget()
        buildTownButton.grid_forget()
        buildCastleButton.grid_forget()
        taxRaiseButton.grid_forget()
        taxLowerButton.grid_forget()
        turnButton.grid_forget()
        crusadeButton.grid_forget()

def updateResources():
    resourceDescription.config(text = "Gold = " + str(playerResources.gold) + "\nSubjects = " + str(playerResources.subjects) + "\nSoldiers = " + str(playerResources.soldiers) + "\nLumber = " + str(playerResources. lumber) + "\nStone = " + str(playerResources.stone))
    resourceDescription2.config(text = "Castles = " + str(playerResources.castles) + "\nTowns = " + str(playerResources.towns) + "\nTax Rate = " + str(playerResources.taxRate))
    if((playerResources.gold <= 0 ) or (playerResources.subjects <= 0)):
        gameEnd()
        message1.config(text = "Your kingdom is in ruins. You lose.")
        return
    elif(playerResources.gold > 999):
        gameEnd()
        message1.config(text = "Congratulations! You win.")
        return

decisionButton = ttk.Button(
    lowerFrame,
    text = "Make decisions.",
    command = clickResponse,
    compound = tk.LEFT
)
decisionButton.grid(
    column = 0,
    row = 0,
    sticky = tk.EW
)

debugWinButton = ttk.Button(
    lowerFrame,
    text = "Win. (DEBUG)",
    command = debugWinAction,
    compound = tk.LEFT
)
debugWinButton.grid(
    column = 0,
    row = 1,
    sticky = tk.EW
)

mineButton = ttk.Button(
    lowerFrame,
    text = "Mine.",
    command = mineActionPrep,
    compound = tk.LEFT
)

mineButton.grid(
    column = 1,
    row = 0,
    sticky = tk.EW
)

loggingButton = ttk.Button(
    lowerFrame,
    text = "Chop Trees.",
    command = loggingActionPrep,
    compound = tk.LEFT
)

loggingButton.grid(
    column = 1,
    row = 1,
    sticky = tk.EW
)

buildTownButton = ttk.Button(
    lowerFrame,
    text = "Build town.",
    command = buildTownActionPrep,
    compound = tk.LEFT
)

buildTownButton.grid(
    column = 1,
    row = 2,
    sticky = tk.EW
)

taxRaiseButton = ttk.Button(
    lowerFrame,
    text = "Raise Taxes.",
    command = taxActionRaise,
    compound = tk.LEFT
)

taxRaiseButton.grid(
    column = 2,
    row = 0,
    sticky = tk.EW
)

taxLowerButton = ttk.Button(
    lowerFrame,
    text = "Lower Taxes.",
    command = taxActionLower,
    compound = tk.LEFT
)

taxLowerButton.grid(
    column = 2,
    row = 1,
    sticky = tk.EW
)

buildCastleButton = ttk.Button(
    lowerFrame,
    text = "Build Castle.",
    command = buildCastleActionPrep,
    compound = tk.LEFT
)

buildCastleButton.grid(
    column = 2,
    row = 2,
    sticky = tk.EW
)

crusadeButton = ttk.Button(
    lowerFrame,
    text = "Launch Crusade.",
    command = crusadeActionPrep,
    compound = tk.LEFT
)

crusadeButton.grid(
    column = 2,
    row = 3,
    sticky = tk.EW
)

turnButton = ttk.Button(
    lowerFrame,
    text = "End Turn.",
    command = turn,
    compound = tk.LEFT
)

turnButton.grid(
    column = 3,
    row = 0,
    rowspan = 3,
    sticky = tk.EW
)

#closeProgramButton
quitButton = ttk.Button(
    lowerFrame,
    text = "Quit Program.",
    command = lambda: root.quit()
)
quitButton.grid(
    column = 4,
    row = 3,
    sticky = tk.EW
)

root.mainloop()
