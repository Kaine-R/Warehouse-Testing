import random
import pygame
import graphic
import graphicResize as gr

def createBG(settings, objectList):
    mainBox = graphic.item(settings, 0)
    mainBox.rect.x, mainBox.rect.y = 0, 0
    mainBox.setSize(settings.screenWidth, settings.screenHeight)
    mainBox.color = settings.BGGRAY
    rightBox = graphic.item(settings, 0)
    rightBox.color = settings.GRAY3
    gr.setRight(mainBox, rightBox, 0, True)
    hotBar = graphic.item(settings, 0)
    hotBar.color = settings.BLACK
    gr.setUp(rightBox, hotBar, 0, True, 100, 10)

    backBtn = graphic.item(settings, 0, "Back Log", False, True)
    backBtn.color = settings.GRAY4
    backBtn.action = "backOrder"
    listBtn = graphic.item(settings, 0, "List", False, True)
    listBtn.color = settings.GRAY2
    listBtn.action = "list"
    graphBtn = graphic.item(settings, 0, "Graph", False, True)
    graphBtn.color = settings.GRAY3
    graphBtn.action = "graph"

    gr.listHor(hotBar, listBtn, 0, 3, 1, True, True)
    gr.listHor(hotBar, graphBtn, 1, 3, 1, True, True)
    gr.listHor(hotBar, backBtn, 2, 3, 1, True, True)

    objectList.extend([mainBox, rightBox, hotBar, backBtn, listBtn, graphBtn])

def createMainMenu(settings, objectList):
    addBox = graphic.item(settings, 1, "Add Box", False, True)
    addBox.action = "add"
    addBox.border = 1
    removeBox = graphic.item(settings, 1, "Remove Box", False, True)
    removeBox.action = "remove"
    removeBox.border = 1
    options = graphic.item(settings, 1, "Options", False, True)
    options.action = "option"
    options.border = 1
    gr.center(objectList[1], addBox)
    addBox.color, removeBox.color, options.color = settings.BLACK, settings.BLACK, settings.BLACK
    addBox.rect.x -= 50
    gr.setDown(addBox, removeBox)
    gr.setDown(removeBox, options)

    objectList.append(addBox)
    objectList.append(removeBox)
    objectList.append(options)

def addBox(settings, objectList, boxList):
    lastLayer = getLastLayer(objectList)+1
    name = graphic.item(settings, lastLayer, "Name")
    inputName = graphic.item(settings, lastLayer, "    ", True, True,)
    inputName.action = "input"
    comment = graphic.item(settings, lastLayer, "Comments")
    inputComment = graphic.item(settings, lastLayer, "    ", True, True)
    inputComment.action = "input"
    inputName.color, inputComment.color = settings.GREEN, settings.GREEN


    gr.center(objectList[1], name)
    name.rect.x -= 120
    name.rect.y -= 150
    gr.setDown(name, inputName)
    gr.setDown(inputName, comment)
    gr.setDown(comment, inputComment)
    objectList.extend([name, inputName, comment, inputComment])

    placement = graphic.item(settings, lastLayer)
    gr.setDown(inputComment, placement)
    placement.rect.y += 50
    placement.rect.x += 50
    backBtn(objectList, lastLayer)
    getSize(settings, objectList, placement, lastLayer)


def getSize(settings, objectList, parent, layer):
    width = graphic.item(settings, layer, "Width")
    inputWidth = graphic.item(settings, layer, "0", True, True)
    inputWidth.color = settings.GREEN
    inputWidth.action = "input"

    length = graphic.item(settings, layer, "Length")
    inputLength = graphic.item(settings, layer, "0", True, True)
    inputLength.color = settings.GREEN
    inputLength.action = "input"

    height = graphic.item(settings, layer, "Height")
    inputHeight = graphic.item(settings, layer, "0", True, True)
    inputHeight.color = settings.GREEN
    inputHeight.action = "input"

    gr.center(parent, width)
    width.rect.x -= 50
    gr.setDown(width, length)
    gr.setDown(length, height)
    gr.setRight(width, inputWidth, 60)
    gr.setRight(length, inputLength, 60)
    gr.setRight(height, inputHeight, 60)

    objectList.extend([width, length, height, inputWidth, inputLength, inputHeight])
    objectList.append(doneBtn(height, layer))

def removeBox(objectList, boxList):
    prompt = graphic.item(objectList[0].settings, getLastLayer(objectList)+1, "Enter Box's ID to remove.")
    gr.center(objectList[1], prompt)
    prompt.rect.x -= 20
    prompt.rect.y -= 150
    uInput = graphic.item(objectList[0].settings, getLastLayer(objectList)+1, "0", True, True)
    uInput.action = "input"
    uInput.color = objectList[0].settings.GREEN
    gr.setDown(prompt, uInput)

    backBtn(objectList, getLastLayer(objectList)+1)
    objectList.extend([prompt, uInput])

def getList(objectList, boxList): #creating and placing boxes in list
    last = "Placeholder for Last box"
    if len(boxList) != 0:
        for i in range(len(boxList)):
            tempName = graphic.item(objectList[0].settings, 2, "#"+str(i+1)+"| "+boxList[i][0], False, True)
            tempName.color = tempName.settings.GRAY4
            tempSize = graphic.item(tempName.settings, 2, "temp")
            tempSize.resetFontSize(23)
            tempSize.prep("Size: "+str(boxList[i][2])+" / Pos:"+str(boxList[i][3]))
            if i == 0:
                gr.setLeft(objectList[0], tempName, 10, True, 50, 10)
                last = tempName
            else:
                gr.setDown(last, tempName, 10, True, 100, 100)
                last = tempName
            gr.setRight(tempName, tempSize)
            objectList.extend([tempName, tempSize])
    else:
        temp = graphic.item(objectList[0].settings, 2, "Nothing in List.", False, True)
        temp.color = temp.settings.RED
        gr.setLeft(objectList[0], temp, 10, True, 50, 10)
        objectList.append(temp)

def getGraph(objectList, boxList, warehouseSize):
    warehouse = graphic.item(objectList[0].settings, 2)
    warehouse.border = 3
    warehouse.color = objectList[0].settings.BLACK
    warehouse.action = "graph"
    gr.setLeft(objectList[0], warehouse, 50, True, 45, 90)
    drawGraph(objectList, boxList, warehouse, warehouseSize)
    objectList.append(warehouse)

def drawGraph(objectList, boxList, parent, warehouseSize):
    for box in boxList:
        rect = graphic.item(objectList[0].settings, 2, "", False, True)
        warehouseRes = [parent.rect.width / warehouseSize[0], parent.rect.height / warehouseSize[2]]
        rect.setSize(box[2][0]*warehouseRes[0], box[2][2]*warehouseRes[1])
        rect.setPos(parent.rect.x +(box[3][0]*warehouseRes[0]), (parent.rect.bottom) -((box[3][2]+1)*(warehouseRes[1])))
        rect.color = (random.randint(50, 200),random.randint(50, 200),random.randint(50, 200))
        objectList.append(rect)

def removeMenu(objectList, layer=-1):
    if layer == -1:
        lastLayer = objectList[-1].layer

        for i in reversed(range(len(objectList))):
            if objectList[i].layer == lastLayer:
                objectList.pop(i)
    else:
        for i in reversed(range(len(objectList))):
            if objectList[i].layer == layer:
                objectList.pop(i)

def confirm(objectList):
    border = graphic.item(objectList[0].settings, 9)
    border.border, border.color = 3, objectList[0].settings.BLACK
    border.setSize(300+border.border, 200+border.border)
    bg = graphic.item(objectList[0].settings, 9)
    bg.setSize(300, 200)
    text = graphic.item(objectList[0].settings, 9, "Are you Sure?")
    yes = graphic.item(objectList[0].settings, 9, "Yes")
    yes.action = "yes"
    no = graphic.item(objectList[0].settings, 9, "No")
    no.action = "back"

    gr.center(objectList[0], border)
    gr.center(objectList[0], bg)
    gr.center(bg, text)
    text.rect.y -= 50
    gr.listHor(bg, no, 2, 10, 1, False, False)
    gr.listHor(bg, yes, 6, 10, 1, False, False)
    yes.rect.y += 100
    no.rect.y += 100

    objectList.extend([border, bg, text, yes, no])

def doneBtn(parent, layer=3):
    done = graphic.item(parent.settings, layer, "Done", False, True)
    done.color = parent.settings.GRAY2
    gr.setDown(parent, done)
    gr.centerHor(parent, done)
    done.rect.y += 25
    done.action = "button"
    return done

def backBtn(objectList, lastLayer):
    back = graphic.item(objectList[0].settings, lastLayer, "Back", False, True)
    back.color = objectList[0].settings.RED
    back.action = "back"
    gr.setDown(objectList[3], back, 5, True)
    objectList.append(back)

def createWarning(objectList, msg):
    warning = graphic.item(objectList[0].settings, 9, "Warning: " + msg, False, True)
    warning.resetFontSize(30)
    warning.prep(msg)
    warning.color = warning.settings.RED
    if objectList[-1].layer == 9:
        gr.setDown(objectList[-1], warning)

    else:
        warningList = graphic.item(warning.settings, 9, "Error List:", False, True)
        warningList.color = warning.settings.RED
        gr.setDown(objectList[4], warningList)
        gr.setDown(warningList, warning)
        objectList.append(warningList)
    objectList.append(warning)

def getLastLayer(objectList):
    for object in objectList:
        temp = 1
        if object.layer > temp and object.layer != 9:
            temp = object.layer
        return temp