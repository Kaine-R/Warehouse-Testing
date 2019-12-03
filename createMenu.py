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

    placeholder = graphic.Basic(settings, 9)
    placeholder.rect = objectList[1].rect.copy()
    placeholder.nudge(60, 70)
    addBox.rect.width += 200
    gr.easyListV(placeholder.getPos(), [addBox, removeBox], objectList)


def addBox(settings, objectList):
    """Creates menu for box input (includes getSize)"""
    lastLayer = getLastLayer(objectList)+1

    name = graphic.Text(settings, lastLayer, "Name: ")
    name.createTitle()
    inputName = graphic.Text(settings, lastLayer, "", True)
    inputName.createInput()
    comment = graphic.Text(settings, lastLayer, "Comments: ")
    comment.createTitle()
    inputComment = graphic.Text(settings, lastLayer, "", True)
    inputComment.createInput()

    body = graphic.Holder(settings, lastLayer)
    body.color = settings.GRAY5
    gr.setLeft(objectList[1], body, False, 90, 85)
    body.nudge(25, 50)

    gr.allSameSize([comment, name])
    gr.setLeft(body, name)
    name.nudge(50, 20)
    gr.setDown(name, comment)
    comment.nudge(0, 3)
    gr.setRight(name, inputName, True)
    gr.setRight(comment, inputComment, True)
    objectList.extend([body, name, inputName, comment, inputComment,
                       backBtn(objectList, getLastLayer(objectList)+1)])

    getSize(settings, objectList, (comment.rect.x, comment.rect.bottom+3), lastLayer)

def getSize(settings, objectList, parentPos, layer):
    """Get Width, Length, Height input boxes"""
    width = graphic.Text(settings, layer, "Width")
    width.fill = False
    inputWidth = graphic.Text(settings, layer, "", True)
    inputWidth.createInput()

    length = graphic.Text(settings, layer, "Length")
    length.fill = False
    inputLength = graphic.Text(settings, layer, "", True)
    inputLength.createInput()

    height = graphic.Text(settings, layer, "Height")
    height.fill = False
    inputHeight = graphic.Text(settings, layer, "", True)
    inputHeight.createInput()

    gr.easyListV(parentPos, [width, length, height], objectList)
    gr.setRight(width, inputWidth, True)
    gr.setRight(length, inputLength, True)
    gr.setRight(height, inputHeight, True)
    objectList.extend([inputWidth, inputLength, inputHeight, doneBtn(height, layer)])

def removeBox(objectList):
    """Create menu to remove box"""
    backG = graphic.Basic(objectList[0].settings, getLastLayer(objectList)+1)
    backG.nudge(0, 100, 300, 350)
    gr.centerHor(objectList[1], backG)
    prompt = graphic.Text(objectList[0].settings, getLastLayer(objectList)+1, "Enter Box's ID to remove.")
    prompt.fill = False
    gr.center(objectList[1], prompt)
    prompt.nudge(-20, -150)
    uInput = graphic.Text(objectList[0].settings, getLastLayer(objectList)+1, "0", True)
    uInput.createInput()
    gr.setDown(prompt, uInput, True)
    clearAllBtn = graphic.Text(objectList[0].settings, getLastLayer(objectList)+1, "Clear All")
    clearAllBtn.createBtn()
    gr.setDown(uInput, clearAllBtn)
    clearAllBtn.nudge(0, 100)
    clearAllBtn.type = "clearAll"

    objectList.extend([backG, prompt, uInput, doneBtn(uInput, uInput.layer),
                       backBtn(objectList, getLastLayer(objectList)+1), clearAllBtn])

def getList(objectList, boxList, pageNum): #creating and placing boxes in list
    """Create graphical list based on whats on boxList"""
    settings = objectList[0].settings
    if len(boxList) != 0:
        i = pageNum[0]*10
        while i < (pageNum[0]+1)*10 and i < len(boxList):
            tempHolder = graphic.Holder(settings, 1)
            gr.setLeft(objectList[0], tempHolder, False, 100, 8)
            tempHolder.nudge(0, (i % 10) * 47)

            tempName = graphic.Text(settings, 1, "#"+str(i+1)+"  "+str(boxList[i][0]))
            gr.setLeft(tempHolder, tempName)
            tempName.nudge(2, -10)

            tempSize = graphic.Text(settings, 1, "Size: "+str(boxList[i][2])+"  Pos:"+str(boxList[i][3]))
            gr.setRight(tempHolder, tempSize)
            tempSize.nudge(2, -10)

            tempComment = graphic.Text(settings, 1, "Comments:  "+str(boxList[i][1]))
            tempComment.changeTextSize(18)
            gr.setLeft(tempHolder, tempComment)
            tempComment.nudge(0, 10)

            tempName.fill, tempSize.fill, tempComment.fill = False, False, False
            objectList.append(tempHolder)
            tempHolder.addItems([tempName, tempSize, tempComment])
            i += 1

        tempBackG = graphic.Text(objectList[0].settings, 1, "", True)
        gr.setLeft(objectList[0], tempBackG, False, 100, 15)
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
        gr.easyListH((tempBackG.rect.x+90, tempBackG.rect.y+20),
                     [tempLess, tempPage, tempGreat], objectList, 15)
    else:
        temp = graphic.Text(objectList[0].settings, 1, "Nothing in List.", True)
        temp.color = temp.settings.RED
        gr.setLeft(objectList[0], temp, False, 100, 10)
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
    warehouseRes = (parent[0] / warehouseSize[0], parent[1] / warehouseSize[1],
                    parent[2] / warehouseSize[2])

    currentLvl = 0
    count = len(boxList)
    while count > 0:
        for i in reversed(boxList):
            if i[3][2] == currentLvl:
                rect = graphic.Polygon(objectList[0].settings, 1)
                rectCords = [(200 - (i[3][0] * warehouseRes[0]) + (i[3][1] * warehouseRes[1]),
                              450 - (i[3][0] * 10) - (i[3][1] * 10) - (i[3][2] * 50))]
                temp = getBasePoint(warehouseRes, [i[2][0]])
                rectCords.append((rectCords[0][0]-temp[0], rectCords[0][1]-temp[1])) #point1
                temp = getTopPoint(warehouseRes, [i[2][2]])
                rectCords.append((rectCords[1][0], rectCords[1][1]-temp[1])) #point2
                temp = getBasePoint(warehouseRes, [i[2][1]])
                rectCords.append((rectCords[2][0]+temp[0], rectCords[2][1]-temp[1])) #point3
                temp = getBasePoint(warehouseRes, [i[2][0]])
                rectCords.append((rectCords[3][0]+temp[0], rectCords[3][1]+temp[1])) #point4
                temp = getTopPoint(warehouseRes, [i[2][2]])
                rectCords.append((rectCords[4][0], rectCords[4][1]+temp[1])) #point5

                rect.color = setRandColor()
                rect.polyCords = rectCords
                objectList.append(rect)
                count -= 1
        currentLvl += 1


def getBasePoint(warehouseRes, size):
    """Returns the calculations for bottom/top plane on a 3D item"""
    return (warehouseRes[0]*int(size[0]), 10*int(size[0])) #raw input instead of passing var

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


def doneBtn(parent, layer=3):
    """Done Btn to progress user input"""
    done = graphic.Text(parent.settings, layer, "Done", True)
    done.color = parent.settings.GRAY2
    gr.setDown(parent, done)
    done.nudge(0, 0, 40)
    done.rect.y += 25
    done.type = "button"
    return done

def backBtn(objectList, lastLayer):
    """Back btn to return to previous layer"""
    back = graphic.Text(objectList[0].settings, lastLayer, "Back")
    back.color = objectList[0].settings.RED
    back.type = "back"
    gr.setDown(objectList[4], back, True)
    back.nudge(0, -35, 100, -10)

    return back

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
