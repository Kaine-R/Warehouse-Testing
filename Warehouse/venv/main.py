import pygame
import string
from settings import Settings
import createMenu
import gameFunction as gf
import graphic
import graphicResize as gr

def runWarehouse():
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    pygame.display.set_caption("Warehouse Game")
    lastAction = ["menu"]

    warehouse = [5, 5, 5] # Testing, size is always 5, 5, 5

    boxList = []
    backOrder = []
    #print("Please enter Dimentions for Warehouse. ")
    #warehouse = askSize("Warehouse")

    # for i in range(5):
    #     temp = ["box" + str(i), "comment", [i, i, i]]
    #     boxList.append(temp)

    objectList = []
    createMenu.createBG(settings, objectList)
    createMenu.createMainMenu(settings, objectList)

    repeat = True
    while repeat == True:
        screen.fill((250,250,250))

        for object in objectList:
            object.draw(screen)

        gf.checkEvents(objectList, boxList, backOrder, warehouse, lastAction)

        pygame.display.flip()







def menu(boxList):
    print("Welcome the warehouse menu!")
    print("Enter 1 to add boxes \nEnter 2 to remove boxes \nEnter 3 for list\nEnter 4 to leave")
    choice = checkInt()
    if choice == 1:
        addBox(boxList)
    elif choice == 2:
        removeBox(boxList)
    elif choice == 3:
        getBoxList(boxList)
    elif choice == 4:
        return False
    else:
        print("more options are coming soon.")
    return True

def addBox(boxList):
    tempBox = []
    print("Enter the name of box: ", end="")
    tempBox.append(checkStr())
    print("Enter comments (optional)")
    tempBox.append(input())
    print("Enter the size of box (int only): ")
    tempBox.append(askSize("box"))
    boxList.append(tempBox)

def removeBox(boxList):
    print("would you like to delete a box?")
    getBoxList(boxList)
    print("If so, enter the object number: ", end="")
    num = checkInt()
    boxList.pop(int(num)-1)

def getBoxList(list):
    if len(list) == 0:
        print("Box List is empty!")
    else:
        for x in range(len(list)):
            print("ID:" + str(x + 1), end="")
            print(" Name: " + str(list[x][0]) + ", Size: ", end="")
            print(list[x][2])
            if list[x][1] != "":
                print(list[x][1])
            print("")

def askSize(object):
    group = []
    print("Enter Width of " + object + ": ", end="")
    group.append(checkInt())
    print("Enter Length of " + object + ": ", end="")
    group.append(checkInt())
    print("Enter Height of " + object + ": ", end="")
    group.append(checkInt())
    return group


def checkInt(min=0, max=999):
    try:
        choice = int(input())
        assert (choice > min)
        assert (choice <= max)
    except AssertionError as Error:
        print("Variable is either too small or too large")
        print("Please enter another int:", end="")
        return checkInt()
    except:
        print("Problem with entered variable.")
        print("Please enter another int:", end="")
        return checkInt()
    else:
        return choice

def checkStr():
    try:
        choice = input()
        assert (choice != "")
    except:
        print("Something wrong with input string. Enter another: ", end="")
        return checkStr()
    else:
        return choice


    # raise Exception("help: choice was {}".format(choice))
    # assert (choice >= 0), "choice was not larger than 0"

runWarehouse()
