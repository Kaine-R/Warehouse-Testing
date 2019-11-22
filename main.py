#"""C:\Users\Kaine's PC\Documents\GitHub\Warehouse-Testing\Warehouse\pylint.exe"""
import pygame
from settings import Settings
import createMenu
import gameFunction as gf

def runWarehouse():
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    pygame.display.set_caption("Warehouse Game")
    lastAction = ["menu"]
    lastGraph = ["list"]
    pageNum = [0]

    warehouse = [5, 5, 5] # Testing, size is always 5, 5, 5

    boxList = []
    backOrder = []
    objectList = []

    createMenu.createBG(settings, objectList)
    createMenu.createMainMenu(settings, objectList)
    createMenu.getList(objectList, boxList, pageNum)
    img = pygame.image.load("warehouseLogo.png")


    repeat = True
    while repeat:
        screen.fill((0, 0, 0))

        i = 0
        for item in objectList:
            i = item.layer if item.layer > i else i
            item.draw(screen)
        if i == 2:
            screen.blit(img, (460, 250))

        gf.checkEvents(objectList, boxList, backOrder, warehouse, lastAction, lastGraph, pageNum)

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

def getBoxList(boxList):
    if len(boxList) == 0:
        print("Box List is empty!")
    else:
        for x in range(len(boxList)):
            print("ID:" + str(x + 1), end="")
            print(" Name: " + str(boxList[x][0]) + ", Size: ", end="")
            print(boxList[x][2])
            if boxList[x][1] != "":
                print(boxList[x][1])
            print("")

def askSize(item):
    group = []
    print("Enter Width of " + item + ": ", end="")
    group.append(checkInt())
    print("Enter Length of " + item + ": ", end="")
    group.append(checkInt())
    print("Enter Height of " + item + ": ", end="")
    group.append(checkInt())
    return group

def checkInt(minNum=0, maxNum=999):
    try:
        choice = int(input())
        assert choice > minNum
        assert choice <= maxNum
    except AssertionError:
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
        assert choice != ""
    except:
        print("Something wrong with input string. Enter another: ", end="")
        return checkStr()
    else:
        return choice


    # raise Exception("help: choice was {}".format(choice))
    # assert (choice >= 0), "choice was not larger than 0"

runWarehouse()
