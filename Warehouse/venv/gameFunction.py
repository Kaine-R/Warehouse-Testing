import sys
import pygame
import createMenu

def checkEvents(objectList, boxList, backOrder, warehouse, lastAction):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            createMenu.removeMenu(objectList, 9)
            checkClicks(objectList, boxList, backOrder, warehouse, pygame.mouse.get_pos(), lastAction)
        elif event.type == pygame.KEYDOWN:
            createMenu.removeMenu(objectList, 9)
            addChar(objectList, event)
        elif event.type == pygame.KEYUP:
            pass

def checkClicks(objectList, boxList, backOrder, warehouse, mousePos, lastAction):
    for object in objectList:
        if pygame.Rect.collidepoint(object.rect, mousePos[0], mousePos[1]):
            if object.action == "add":
                createMenu.removeMenu(objectList, getLastLayer(objectList))
                createMenu.addBox(objectList[0].settings, objectList, boxList)
                lastAction.clear()
                lastAction.append("addBox")
            elif object.action == "remove":
                createMenu.removeMenu(objectList, getLastLayer(objectList))
                createMenu.removeBox(objectList, boxList)
                lastAction.clear()
                lastAction.append("removeBox")
            elif object.action == "button":
                pickAction(lastAction, objectList, boxList, backOrder, warehouse)
            elif object.action == "list":
                createMenu.removeMenu(objectList, 2)
                createMenu.getList(objectList, boxList)
            elif object.action == "graph":
                createMenu.removeMenu(objectList, 2)
                createMenu.getGraph(objectList, boxList,warehouse)
            elif object.action == "backOrder":
                createMenu.removeMenu(objectList, 2)
                createMenu.getList(objectList, backOrder)
            elif object.action == "option":
                lastAction.clear()
                lastAction.append("option")
            elif object.action == "input":
                for item in objectList:
                    item.focus = False
                object.focus = True
            elif object.action == "yes":
                print("yes")
            elif object.action == "back":
                if getLastLayer(objectList) > 0:
                    createMenu.removeMenu(objectList)
                    if getLastLayer(objectList) == 1:
                        createMenu.createMainMenu(objectList[0].settings, objectList)

def pickAction(lastAction, objectList, boxList, backOrder, warehouse):
    lastLayer = getLastLayer(objectList)
    boxInfo = []
    isGood = True
    if lastAction[0] == "addBox":
        for item in objectList:
            if item.layer == lastLayer:
                if item.action == "input":
                    boxInfo.append(item.msg)

        isGood = isGood if checkText(boxInfo[0], objectList, False) else False
        isGood = isGood if checkText(boxInfo[1], objectList, True, False, 15) else False
        isGood = isGood if checkText(boxInfo[2], objectList, False, True, 4) else False
        isGood = isGood if checkText(boxInfo[3], objectList, False, True, 4) else False
        isGood = isGood if checkText(boxInfo[4], objectList, False, True, 4) else False

        if isGood:
            size = [int(boxInfo[2]), int(boxInfo[3]), int(boxInfo[4])]
            for i in range(3):
                boxInfo.pop(2)
            boxInfo.append(size)
            if checkBoxInWarehouse(warehouse, boxInfo, backOrder):
                searchForRoom(warehouse, boxList, boxInfo)
            else:
                backOrder.append(boxInfo)

def checkBoxInWarehouse(warehouse, boxInfo, backOrder):
    for boxSize in boxInfo[2]:
        for warehouseSize in warehouse:
            if boxSize > warehouseSize:
                return False
    return True

def searchForRoom(warehouse, boxList, boxInfo):
    stay = True
    if len(boxList) == 0:
        boxList.append(boxInfo)
        boxInfo.append([0, 0, 0])
        print("Adding First Box")
        print("***********************")
    else:
        oldSpot = [0,0,0]
        newSpot = [0,0,0]
        while newSpot[2] < warehouse[2] - boxInfo[2][2] and stay:
            for box in boxList:
                temp = hitBox(box, newSpot)
                newSpot[0] += temp
                if newSpot[0] > warehouse[0] - boxInfo[2][0]:
                    print("Move to next Length")
                    newSpot[1] += 1
                    newSpot[0] = 0
                    break
                if newSpot[1] > warehouse[1] - boxInfo[2][1]:
                    print("Move to next Height")
                    newSpot[2] += 1
                    newSpot[0], newSpot[1] = 0, 0
                    break
            if newSpot == oldSpot:
                boxInfo.append(oldSpot)
                boxList.append(boxInfo)
                print("Adding " + boxInfo[0] +" to " + str(boxInfo[3]))
                print("****************************")
                break
            else:
                oldSpot = newSpot

            #CURRENTLY HAS ISSUES MOVING PAST THE FIRST BLOCK WHEN TRYING TRYING TO PLACE BLOCKS

def hitBox(box1, spot):
    for k in range(box1[2][2]):
        for j in range(box1[2][1]):
            for i in range(box1[2][0]):
                if spot == [box1[3][0]+i, box1[3][1]+j, box1[3][2]+k]:
                    print(box1[0] + "| Spot Hit at: " + str(spot))
                    return box1[2][0]
    return 0

def checkText(text, objectList, allowedBlank=False, intOnly=False, charLimit=10):
    isGood = True
    if not allowedBlank:
        if text == "":
            isGood == False
            createMenu.createWarning(objectList, "Can't be blank.")
    if isGood and intOnly:
        if not text.isdigit():
            isGood = False
            createMenu.createWarning(objectList, "Only enter Integers")
    if isGood and len(text) > charLimit:
        isGood = False
        createMenu.createWarning(objectList, "Over char limit of \"" + str(charLimit) + "\"")
    return isGood

def addChar(objectList, event):
    for object in objectList:
        if object.focus:
            if event.key == pygame.K_BACKSPACE:
                if len(object.msg) > 1:
                    object.msg = object.msg[0:-1]
                else:
                    object.msg = ""
                    object.prep("    ")
            elif event.key == pygame.K_SPACE:
                object.msg += " "
            elif checkNumPad(event):
                object.msg += str(pygame.key.name(event.key))[1:2]
            else:
                object.msg += str(pygame.key.name(event.key))[0:1]

def checkNumPad(event):
    if str(pygame.key.name(event.key))[0:1] == "[":
        return True
    else:
        False

def getLastLayer(objectList):
    for object in objectList:
        temp = 1
        if object.layer > temp and object.layer != 9:
            temp = object.layer
        return temp