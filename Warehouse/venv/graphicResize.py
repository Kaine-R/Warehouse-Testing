def listHor(parent, box, num, outOf, size=1, resizeX=True, resizeY=True):
    box.rect.x = parent.rect.x + ((parent.rect.width / outOf) * num)
    box.rect.y = parent.rect.y
    if resizeX:
        box.rect.width = (parent.rect.width / outOf) * size
    if resizeY:
        box.rect.height = parent.rect.height

def listVer(parent, box, num, outOf, size=1, resizeX=True, resizeY=True):
    box.rect.x = parent.rect.x
    box.rect.y = parent.rect.y + ((parent.rect.width / outOf) * num)
    if resizeX:
        box.rect.width = parent.rect.height
    if resizeY:
        box.rect.height = (parent.rect.width / outOf) * size

def setLeft(parent, box, padding = 0, resize=False, percentX = 50, percentY = 100):
    box.rect.x = parent.rect.x + padding
    box.rect.y = parent.rect.y + padding
    if resize:
        box.rect.width = (parent.rect.width * (percentX/100)) - padding
        box.rect.height = (parent.rect.height * (percentY/100)) - padding

def setRight(parent, box, padding = 0, resize=False, percentX = 50, percentY = 100):
    box.rect.x = parent.rect.x + (parent.rect.width * (percentX/100)) + padding
    box.rect.y = parent.rect.y
    if resize:
        box.rect.width = (parent.rect.width * (percentX/100))
        box.rect.height = (parent.rect.height * (percentY/100))

def setUp(parent, box, padding=5, resize=False, percentX=100, percentY=50):
    box.rect.x = parent.rect.x + padding
    box.rect.y = parent.rect.y + padding
    if resize:
        box.rect.width = (parent.rect.width * (percentX / 100))
        box.rect.height = (parent.rect.height * (percentY / 100))

def setDown(parent, box, padding=5, resize=False, percentX=100, percentY=50):
    box.rect.x = parent.rect.x
    box.rect.y = parent.rect.y + parent.rect.height + padding
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


