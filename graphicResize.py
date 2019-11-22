def listHor(parent, box, num, outOf, size=1, resizeX=False, resizeY=False):
    box.rect.x = parent.rect.x + ((parent.rect.width / outOf) * num)
    box.rect.y = parent.rect.y
    if resizeX:
        box.rect.width = (parent.rect.width / outOf) * size
    if resizeY:
        box.rect.height = parent.rect.height

def listVer(parent, box, num, outOf, size=1, resizeX=False, resizeY=False):
    box.rect.x = parent.rect.x
    box.rect.y = parent.rect.y + ((parent.rect.width / outOf) * num)
    if resizeX:
        box.rect.width = parent.rect.height
    if resizeY:
        box.rect.height = (parent.rect.width / outOf) * size

def easyListV(startPoint, group, objectList, padding=5):
    tempSpot = ""
    for i in range(len(group)):
        if i == 0:
            group[0].rect.x, group[0].rect.y = startPoint[0], startPoint[1]
        else:
            group[i].rect.x, group[i].rect.y = tempSpot[0], tempSpot[1] + padding
        group[i].rect.width = group[0].rect.width
        tempSpot = group[i].rect.x, group[i].rect.y + group[i].rect.height
        objectList.append(group[i])

def easyListH(startPoint, group, objectList, padding=5):
    tempSpot = ""
    for i in range(len(group)):
        if i == 0:
            group[0].rect.x, group[0].rect.y = startPoint[0], startPoint[1]
        else:
            group[i].rect.x, group[i].rect.y = tempSpot[0] + padding, tempSpot[1]
        group[i].rect.height = group[0].rect.height
        tempSpot = group[i].rect.x + group[i].rect.width, group[i].rect.y
        objectList.append(group[i])

def allSameSize(group):
    first = group[0]
    for obj in group:
        obj.rect.width = first.rect.width
        obj.rect.height = first.rect.height


def setLeft(parent, box, resize=False, percentX = 50, percentY = 100):
    box.rect.x = parent.rect.x
    box.rect.y = parent.rect.y
    if resize:
        box.rect.width = (parent.rect.width * (percentX/100))
        box.rect.height = (parent.rect.height * (percentY/100))

def setRight(parent, box, resize=False, percentX = 50, percentY = 100):
    box.rect.x = parent.rect.x + (parent.rect.width * (percentX/100))
    box.rect.y = parent.rect.y
    if resize:
        box.rect.width = (parent.rect.width * (percentX/100))
        box.rect.height = (parent.rect.height * (percentY/100))

def setUp(parent, box, resize=False, percentX=100, percentY=50):
    box.rect.x = parent.rect.x
    box.rect.y = parent.rect.y
    if resize:
        box.rect.width = (parent.rect.width * (percentX / 100))
        box.rect.height = (parent.rect.height * (percentY / 100))

def setDown(parent, box, resize=False, percentX=100, percentY=50):
    box.rect.x = parent.rect.x
    box.rect.y = parent.rect.y + parent.rect.height
    if resize:
        box.rect.width = (parent.rect.width * (percentX / 100))
        box.rect.height = (parent.rect.height * (percentY / 100))

def centerHor(parent, box):
    remainder = (parent.rect.width - box.rect.width)/2
    box.rect.x = parent.rect.x + remainder

def centerVer(parent, box):
    remainder = (parent.rect.height - box.rect.height)/2
    box.rect.y = parent.rect.y + remainder

def center(parent, box):
    centerHor(parent, box)
    centerVer(parent, box)


