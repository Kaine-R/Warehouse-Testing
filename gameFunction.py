"""Main functions, (key presses, placing boxes in warehouse, check collisions)"""
import sys
import pygame
import createMenu


def checkEvents(objectList, boxList, backOrder, warehouse, lastAction, lastGraph, pageNum):
    """Checks if keyboard/mouse pressed"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            createMenu.removeMenu(objectList, 9)
            checkClicks(objectList, boxList, backOrder, warehouse, pygame.mouse.get_pos(),
                        lastAction, lastGraph, pageNum)
        elif event.type == pygame.KEYDOWN:
            createMenu.removeMenu(objectList, 9)
            addChar(objectList, event)

def createList(objectList, currentList, pageNum, lastGraph, typeOfGraph, warehouse=""):
    """Creates List based on typeOfGraph"""
    lastGraph[0] = typeOfGraph
    pageNum[0] = 0
    createMenu.removeMenu(objectList, 1)
    if typeOfGraph == "list":
        createMenu.getList(objectList, currentList, pageNum)
    elif typeOfGraph == "graph":
        createMenu.getGraph(objectList, currentList, warehouse)
    elif typeOfGraph == "backOrder":
        createMenu.getList(objectList, currentList, pageNum)

def updateList(objectList, boxList, backOrder, warehouse, lastGraph, pageNum):
    """Called when action need the list display to also be updated"""
    if lastGraph[0] == "list":
        createMenu.removeMenu(objectList, 1)
        createMenu.getList(objectList, boxList, pageNum)
    elif lastGraph[0] == "graph":
        createMenu.removeMenu(objectList, 1)
        createMenu.getGraph(objectList, boxList, warehouse)
    else:
        createMenu.removeMenu(objectList, 1)
        createMenu.getList(objectList, backOrder, pageNum)


def checkClicks(objectList, boxList, backOrder, warehouse, mousePos, lastAction, lastGraph, pageNum):
    """Checks what mouse clicked on"""
    for item in objectList:
        if pygame.Rect.collidepoint(item.rect, mousePos[0], mousePos[1]):
            if item.type == "add":
                createMenu.removeMenu(objectList, getLastLayer(objectList))
                createMenu.addBox(objectList[0].settings, objectList)
                updateList(objectList, boxList, backOrder, warehouse, lastGraph, pageNum)
                lastAction[0] = "addBox"
            elif item.type == "remove":
                createMenu.removeMenu(objectList, getLastLayer(objectList))
                createMenu.removeBox(objectList)
                lastAction[0] = "removeBox"
            elif item.type == "list":
                createList(objectList, boxList, pageNum, lastGraph, "list")
            elif item.type == "graph":
                createList(objectList, boxList, pageNum, lastGraph, "graph", warehouse)
            elif item.type == "backOrder":
                createList(objectList, backOrder, pageNum, lastGraph, "backOrder")
            elif item.type == "button":
                pickAction(lastAction, objectList, boxList, backOrder, warehouse)
                updateList(objectList, boxList, backOrder, warehouse, lastGraph, pageNum)
            elif item.type == "option":
                lastAction[0] = "option"
            elif item.type == "input":
                for checkItem in objectList:
                    checkItem.focus = False
                item.focus = True
            elif item.type == "yes":
                print("yes")
            elif item.type == "pageUp":
                pageNum[0] += 1 if (pageNum[0] + 1) * 10 < len(boxList) else 0
                updateList(objectList, boxList, backOrder, warehouse, lastGraph, pageNum)
            elif item.type == "pageDown":
                pageNum[0] -= 1 if pageNum[0] >= 1 else 0
                updateList(objectList, boxList, backOrder, warehouse, lastGraph, pageNum)
            elif item.type == "back":
                if item.layer > 1:
                    createMenu.removeMenu(objectList, item.layer)
                if getLastLayer(objectList) == 2:
                    createMenu.createMainMenu(objectList[0].settings, objectList)
            elif item.type == "clearAll":
                boxList.clear()
                updateList(objectList, boxList, backOrder, warehouse, lastGraph, pageNum)

def pickAction(lastAction, objectList, boxList, backOrder, warehouse):
    """When done btn clicked, lastAction is used to see what to do next"""
    lastLayer = getLastLayer(objectList)
    boxInfo = []
    isGood = True
    if lastAction[0] == "addBox":
        for item in objectList:
            if item.layer == lastLayer:
                if item.type == "input":
                    boxInfo.append(item.msg)

        isGood = isGood if checkText(boxInfo[0], objectList, False) else False
        isGood = isGood if checkText(boxInfo[1], objectList, True, False, 15) else False
        isGood = isGood if checkText(boxInfo[2], objectList, False, True, 4) else False
        isGood = isGood if checkText(boxInfo[3], objectList, False, True, 4) else False
        isGood = isGood if checkText(boxInfo[4], objectList, False, True, 4) else False

        if isGood:
            size = [int(boxInfo[2]), int(boxInfo[3]), int(boxInfo[4])]
            for i in range(3):  # Pops off the last 3 text fields(size), since they are stored in a list
                boxInfo.pop(2)
            boxInfo.append(size)
            if not searchForRoom(warehouse, boxList, boxInfo):  # if room wasn't found, It'll append to backOrder
                boxInfo.append([0, 0, 0])
                backOrder.append(boxInfo)
    elif lastAction[0] == "removeBox":
        for item in reversed(objectList):
            if item.layer == lastLayer and item.type == "input":
                if checkText(item.msg, objectList, False, True, 10, len(boxList) - 1):
                    print("Removed box #" + str(int(item.msg) - 1))
                    if int(item.msg) - 1 < len(boxList):
                        boxList.pop(int(item.msg) - 1)


def checkBoxInWarehouse(warehouse, boxInfo):
    """Returns if boxSize is larger that warehouse size"""
    for boxSize in boxInfo[2]:
        for warehouseSize in warehouse:
            if boxSize > warehouseSize:
                return False
    return True

def sortBox(boxList, box):
    """Sorts boxes to it appears fine when displayed"""  # Still has a bit of issues
    added = False
    for i in range(len(boxList)):
        if box[3][2] >= boxList[i][3][2]:
            if box[3][1] <= boxList[i][3][1]:
                if box[3][0] < boxList[i][3][0]:
                    boxList.insert(i, box)
                    added = True
                    break
    if not added:
        boxList.append(box)

def searchForRoom(warehouse, boxList, boxInfo):
    """Goes thru warehouse to see if box fits, uses nextSpot and hitBox functions"""
    if len(boxList) == 0:
        boxList.append(boxInfo)
        boxInfo.append([0, 0, 0])
        return True
    else:
        first = True  # Makes sure that "nextSpot()" only happens once
        spotAvailable = True  # if it hit box, tells program to check next spot
        pos = [0, 0, 0]
        while pos[2] < warehouse[2] - boxInfo[2][2]+1:  # extremely inefficient
            for h in range(boxInfo[2][2]):
                for l in range(boxInfo[2][1]):
                    for w in range(boxInfo[2][0]):
                        spotAvailable = False if hitBox(boxList, pos) else spotAvailable
                        if not spotAvailable and first:
                            nextSpot(pos, boxInfo, warehouse)  # If box hit, move pos to check next spot
                            first = False

            if spotAvailable:
                boxInfo.append(pos)
                boxList.append(boxInfo)
                return True
            else:
                first = True
                spotAvailable = True
    return False


def nextSpot(pos, boxInfo, warehouse):
    """Move pos to next spot"""
    pos[0] += boxInfo[2][0]
    if pos[0] > warehouse[0] - boxInfo[2][0]:
        pos[0] = 0
        pos[1] += 1
    if pos[1] > warehouse[1] - boxInfo[2][1]:
        pos[0], pos[1] = 0, 0
        pos[2] += 1

def hitBox(boxList, pos):
    """Checks to see if pos collides with any boxes"""
    for i in boxList:
        for bh in range(i[3][2], i[2][2] + i[3][2]):
            for bl in range(i[3][1], i[2][1] + i[3][1]):
                for bw in range(i[3][0], i[2][0] + i[3][0]):
                    print("shot Checked: " + str((bw, bl, bh)))
                    if pos == [bw, bl, bh]:
                        print("Spot hit: " + str(pos))
                        return True
    return False

def checkText(text, objectList, allowedBlank=False, intOnly=False, charLimit=10, numMax=9999, numMin=0):
    """Check user Input to fit current setting, char limit/int only..."""
    isGood = True
    if not allowedBlank:
        if text == "":
            isGood = False
            createMenu.createWarning(objectList, "Can't be blank.")
    if isGood and intOnly:
        if not text.isdigit():
            isGood = False
            createMenu.createWarning(objectList, "Only enter Integers")
        elif int(text) - 1 > numMax:
            isGood = False
            createMenu.createWarning(objectList, "Integer is too large")
        elif int(text) - 1 < numMin:
            isGood = False
            createMenu.createWarning(objectList, "Integer is too small")
    if isGood and len(text) > charLimit:
        isGood = False
        createMenu.createWarning(objectList, "Over char limit of \"" + str(charLimit) + "\"")

    return isGood


def addChar(objectList, event):
    """Adds char to the textBox.msg as text storage"""
    for item in objectList:
        if item.type == "input" and item.focus:
            if event.key == pygame.K_BACKSPACE:
                item.msg = item.msg[0:-1]
            elif event.key == pygame.K_SPACE:
                item.msg += " "
            elif checkNumPad(event):
                item.msg += str(pygame.key.name(event.key))[1:2]
            else:
                item.msg += str(pygame.key.name(event.key))[0:1]


def checkNumPad(event):
    """if numpad hit it will send number char instead of [numpad num]"""
    if str(pygame.key.name(event.key))[0:1] == "[":
        return True
    return False


def getLastLayer(objectList):
    """Return the last menu layer from objectList"""
    temp = 2
    for item in objectList:
        if item.layer > temp and item.layer != 9:
            temp = item.layer
    return temp
