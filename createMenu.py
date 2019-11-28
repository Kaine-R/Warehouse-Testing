"""
Functions that create menus, (main menu, add/remove box, make list graph)
Background layer = 0, List/Graph menu layer = 1, Add/remove/main menu = 2, Warning text layer = 9
"""
import random
import graphic
import graphicResize as gr

def createBG(settings, objectList):
    """Create background layout (only called once)"""
    leftBox = graphic.Basic(settings, 0)
    leftBox.setPos(0, 0)
    leftBox.setSize(settings.screenWidth/2-2, settings.screenHeight)
    leftBox.color = settings.BGGRAY
    rightBox = graphic.Basic(settings, 0)
    rightBox.setPos(leftBox.rect.right +4, leftBox.rect.y+58)
    rightBox.setSize(settings.screenWidth/2-2, settings.screenHeight-58)
    rightBox.color = settings.GRAY3
    hotBar = graphic.Basic(settings, 9)
    hotBar.setPos(leftBox.rect.right, 0)

    backBtn = graphic.Text(settings, 0, "Back Log")
    backBtn.color = settings.GRAY4
    backBtn.type = "backOrder"
    listBtn = graphic.Text(settings, 0, "List")
    listBtn.color = settings.GRAY2
    listBtn.type = "list"
    graphBtn = graphic.Text(settings, 0, "Graph")
    graphBtn.color = settings.GRAY3
    graphBtn.type = "graph"
    objectList.extend([leftBox, rightBox])

    listBtn.setSize(133, 55)
    hotBar.nudge(4)
    gr.allSameSize([listBtn, backBtn, graphBtn])
    gr.easyListH(hotBar.getPos(), [listBtn, backBtn, graphBtn], objectList, 0)


def createMainMenu(settings, objectList):
    """Create add/remove box buttons"""
    addBox = graphic.Text(settings, 2, "Add Box", True)
    addBox.type = "add"
    removeBox = graphic.Text(settings, 2, "Remove Box", True)
    removeBox.type = "remove"
    # options = graphic.item(settings, 2, "Options", True)
    # options.type = "option"

    placeholder = graphic.Basic(settings, 9)
    placeholder.rect = objectList[1].rect.copy()
    placeholder.nudge(60, 70)
    addBox.rect.width += 200
    gr.easyListV(placeholder.getPos(), [addBox, removeBox], objectList)


def addBox(settings, objectList):
    """Creates menu for box input (includes getSize)"""
    lastLayer = getLastLayer(objectList)+1
    name = graphic.Text(settings, lastLayer, "Name")
    inputName = graphic.Text(settings, lastLayer, "    ", True)
    inputName.createInput()
    inputName.textPadding(0, -10)
    comment = graphic.Text(settings, lastLayer, "Comments")
    inputComment = graphic.Text(settings, lastLayer, "    ", True)
    inputComment.textPadding(0, -10)
    inputComment.createInput()

    placeholder = graphic.Basic(settings, 9)
    placeholder.rect = objectList[1].rect.copy()
    placeholder.nudge(30, 30)
    gr.easyListV(placeholder.getPos(), [name, inputName, comment, inputComment], objectList, -15)

    placement = graphic.Basic(settings, lastLayer)
    gr.setDown(inputComment, placement)
    placement.rect.y += 50
    placement.rect.x += 50
    backBtn(objectList, lastLayer)
    getSize(settings, objectList, placement, lastLayer)

def getSize(settings, objectList, parent, layer):
    """Get Width, Length, Height input boxes"""
    width = graphic.Text(settings, layer, "Width")
    inputWidth = graphic.Text(settings, layer, "0", True)
    inputWidth.createInput()

    length = graphic.Text(settings, layer, "Length")
    inputLength = graphic.Text(settings, layer, "0", True)
    inputLength.createInput()

    height = graphic.Text(settings, layer, "Height")
    inputHeight = graphic.Text(settings, layer, "0", True)
    inputHeight.createInput()

    gr.easyListV(parent.getPos(), [width, length, height], objectList)
    gr.setRight(width, inputWidth)
    gr.setRight(length, inputLength)
    gr.setRight(height, inputHeight)
    inputWidth.nudge(30)
    inputLength.nudge(30)
    inputHeight.nudge(30)
    objectList.extend([inputWidth, inputLength, inputHeight, doneBtn(height, layer)])

def removeBox(objectList):
    """Create menu to remove box"""
    prompt = graphic.Text(objectList[0].settings, getLastLayer(objectList)+1, "Enter Box's ID to remove.")
    gr.center(objectList[1], prompt)
    prompt.rect.x -= 20
    prompt.rect.y -= 150
    uInput = graphic.Text(objectList[0].settings, getLastLayer(objectList)+1, "0", True)
    uInput.createInput()
    gr.setDown(prompt, uInput)

    backBtn(objectList, getLastLayer(objectList)+1)
    objectList.extend([prompt, uInput, doneBtn(uInput, uInput.layer)])

def getList(objectList, boxList, pageNum): #creating and placing boxes in list
    """Create graphical list based on whats on boxList"""
    if len(boxList) != 0:
        lenBoxList = len(boxList)
        tempBoxes = []
        tempBoxNames = []
        tempBoxSizes = []
        tempBoxComments = []
        SS = objectList[0].getPos()

        i = pageNum[0]*8
        if (pageNum[0]+1)*8 < lenBoxList:
            lenBoxList = (pageNum[0]+1)*8
        while i < (lenBoxList):
            tempBox = graphic.Basic(objectList[0].settings, 1)
            gr.setLeft(objectList[0], tempBox, True, 100, 10)
            tempBoxName = graphic.Text(objectList[0].settings, 1, "#"+str(i+1)+"  "+str(boxList[i][0]))
            tempBoxName.center = False
            tempBoxSize = graphic.Text(objectList[0].settings, 1, "Size: "+str(boxList[i][2])+"  Pos:"+str(boxList[i][3]))
            tempBoxSize.center = False
            tempBoxCom = graphic.Text(objectList[0].settings, 1, "Comments:  "+str(boxList[i][1]))
            tempBoxCom.center = False
            tempBoxes.append(tempBox)
            tempBoxNames.append(tempBoxName)
            tempBoxComments.append(tempBoxCom)
            tempBoxSizes.append(tempBoxSize)
            i += 1

        gr.easyListV(objectList[0].getPos(), tempBoxes, objectList)
        gr.easyListV((SS[0]-5, SS[1]-15), tempBoxNames, objectList, 10)
        gr.easyListV((SS[0]-5, SS[1]+10), tempBoxComments, objectList, 10)
        gr.easyListV((SS[0]+180, SS[1]-15), tempBoxSizes, objectList, 10)

        tempBackG = graphic.Text(objectList[0].settings, 1, "", True)
        gr.setLeft(objectList[0], tempBackG, True, 100, 15)
        tempBackG.color = objectList[0].settings.GRAY3
        tempBackG.rect.y += 470
        tempLess = graphic.Text(objectList[0].settings, 1, "  <  ", True)
        tempLess.color = objectList[0].settings.GRAY5
        tempLess.type = "pageDown"
        tempPage = graphic.Text(objectList[0].settings, 1, str(pageNum), True)
        tempPage.color = objectList[0].settings.GRAY5
        tempGreat = graphic.Text(objectList[0].settings, 1, "  >  ", True)
        tempGreat.color = objectList[0].settings.GRAY5
        tempGreat.type = "pageUp"
        objectList.append(tempBackG)
        gr.easyListH((tempBackG.rect.x+90, tempBackG.rect.y+20), [tempLess, tempPage, tempGreat], objectList, 15)
    else:
        temp = graphic.Text(objectList[0].settings, 1, "Nothing in List.", True)
        temp.color = temp.settings.RED
        gr.setLeft(objectList[0], temp, True, 100, 10)
        objectList.append(temp)

def getGraph(objectList, boxList, warehouseSize):
    """Create base for 3D graph"""
    warehouseCords = [(200, 350)]
    warehouseCords.append((warehouseCords[0][0]-170, warehouseCords[0][1]+50))
    warehouseCords.append((warehouseCords[1][0]+170, warehouseCords[1][1]+50))
    warehouseCords.append((warehouseCords[2][0]+170, warehouseCords[2][1]-50))
    warehouse = graphic.Polygon(objectList[0].settings, 1)
    warehouse.border = -1
    warehouse.color = warehouse.settings.RED
    warehouse.polyCords = warehouseCords
    print(warehouseCords)
    objectList.append(warehouse)
    drawGraph(objectList, boxList, (170, 170, 400), warehouseSize)


def drawGraph(objectList, boxList, parent, warehouseSize):
    """Create 3D graph based on whats on boxList, appears above getGraph"""
    warehouseRes = (parent[0] / warehouseSize[0], parent[1] / warehouseSize[1], parent[2] / warehouseSize[2])
    boxesPerLvl = warehouseSize[0] * warehouseSize[1]
    boxCount = len(boxList)-1
    lvl = 1
    i = len(boxList)-1 if len(boxList)-1 < boxesPerLvl else boxesPerLvl-1
    while boxCount >= 0:
        print(i)
        box = boxList[i]
        rect = graphic.Polygon(objectList[0].settings, 1)
        rectCords = []
        rectCords.append((200-(box[3][0]*warehouseRes[0])+(box[3][1]*warehouseRes[1]), 450-(box[3][0]*10)-(box[3][1]*10)-(box[3][2]*50))) #point0
        temp = getBasePoint(warehouseRes, [box[2][0]])
        rectCords.append((rectCords[0][0]-temp[0], rectCords[0][1]-temp[1])) #point1
        temp = getTopPoint(warehouseRes, [box[2][2]])
        rectCords.append((rectCords[1][0], rectCords[1][1]-temp[1])) #point2
        temp = getBasePoint(warehouseRes, [box[2][1]])
        rectCords.append((rectCords[2][0]+temp[0], rectCords[2][1]-temp[1])) #point3
        temp = getBasePoint(warehouseRes, [box[2][0]])
        rectCords.append((rectCords[3][0]+temp[0], rectCords[3][1]+temp[1])) #point4
        temp = getTopPoint(warehouseRes, [box[2][2]])
        rectCords.append((rectCords[4][0], rectCords[4][1]+temp[1])) #point5

        rect.color = setRandColor()
        rect.polyCords = rectCords
        objectList.append(rect)

        if i%boxesPerLvl <= 0:
            print("List Size: " + str(len(boxList)-1) + "  |  lvl: "+ str(lvl))
            lvl += 1
            i = (boxesPerLvl*lvl)-1 if (boxesPerLvl*lvl)-1 < len(boxList)-1 else len(boxList)-1
        else:
            i -= 1
        boxCount -= 1


def getBasePoint(warehouseRes, size):
    """Returns the calculations for bottom/top plane on a 3D item"""
    return (warehouseRes[0]*size[0], 10*size[0]) #raw input instead of passing var

def getTopPoint(warehouseRes, size):
    """Returns the calculations for the points that move from bottom plane to top plane"""
    return (warehouseRes[0]*size[0], 50*size[0])

def setRandColor():
    """Select random color for 3D graph boxes"""
    return (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))

def removeMenu(objectList, layer=-1):
    """Removes a menu layer to clear space for next menu"""
    lastLayer = layer if layer != -1 else getLastLayer(objectList)
    if lastLayer > 0:
        for i in reversed(range(len(objectList))):
            if objectList[i].layer == lastLayer:
                objectList.pop(i)


def confirm(objectList): # Currently unused --------------------------------
    """Confirm dialog, not currently used"""
    border = graphic.Basic(objectList[0].settings, 9)
    border.border, border.color = 3, objectList[0].settings.BLACK
    border.setSize(300+border.border, 200+border.border)
    bg = graphic.Basic(objectList[0].settings, 9)
    bg.setSize(300, 200)
    text = graphic.Text(objectList[0].settings, 9, "Are you Sure?")
    yes = graphic.Text(objectList[0].settings, 9, "Yes")
    yes.type = "yes"
    no = graphic.Text(objectList[0].settings, 9, "No")
    no.type = "back"

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
    """Done Btn to progress user input"""
    done = graphic.Text(parent.settings, layer, "Done", True)
    done.color = parent.settings.GRAY2
    gr.setDown(parent, done)
    gr.centerHor(parent, done)
    done.rect.y += 25
    done.type = "button"
    return done

def backBtn(objectList, lastLayer):
    """Back btn to return to previous layer"""
    back = graphic.Text(objectList[0].settings, lastLayer, "Back")
    back.color = objectList[0].settings.RED
    back.type = "back"
    gr.setDown(objectList[4], back, False)
    back.nudge(0, 5, 80, -10)

    objectList.append(back)

def createWarning(objectList, msg):
    """Create red text warning that disappears on any key press"""
    warning = graphic.Text(objectList[0].settings, 9, "Warning: " + msg, True)
    warning.changeTextSize(17)
    warning.textPadding(0, -10)
    warning.text = msg
    warning.color = warning.settings.RED
    if objectList[-1].layer == 9:
        gr.setDown(objectList[-1], warning)
    else:
        warningList = graphic.Text(warning.settings, 9, "Error List:", True)
        warningList.color = warning.settings.RED
        gr.setDown(objectList[2], warningList)
        gr.setDown(warningList, warning)
        objectList.append(warningList)
    warning.nudge(0, 2)
    objectList.append(warning)

def getLastLayer(objectList):
    """Returns last menu layer"""
    temp = 2
    for item in objectList:
        if item.layer > temp and item.layer != 9:
            temp = item.layer
    return temp
