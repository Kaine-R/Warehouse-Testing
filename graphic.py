"""graphic.py, For creating items(graphical boxes/text for user interaction)"""
import pygame

class Basic:
    def __init__(self, settings, layer, fill=True):
        """Create Basic for other on screen objects"""
        self.type = "basic"
        self.action = ""
        self.settings = settings
        self.layer = layer
        self.rect = pygame.Rect((0, 0), (50, 50))
        self.color = settings.GRAY4
        self.border = 0
        self.fill = fill

    def setSize(self, width, height):
        """Set Size of graphical box"""
        self.rect.width, self.rect.height = width, height

    def setPos(self, tempX, tempY):
        """Set Position for graphical box on screen"""
        self.rect.x, self.rect.y = tempX, tempY

    def getPos(self):
        """Returns graphical box's position on screen"""
        return self.rect.x, self.rect.y

    def nudge(self, xNudge=0, yNudge=0, widNudge=0, heiNudge=0):
        """Allows for changes in position(xNudge, yNudge) and size(weiNudge, heiNudge)"""
        self.rect.x += xNudge
        self.rect.y += yNudge
        self.rect.width += widNudge
        self.rect.height += heiNudge

    def draw(self,  screen):
        pygame.draw.rect(screen, self.color, self.rect, self.border)


class Text(Basic):
    def __init__(self, settings, layer, text, realTime=False, size=21):
        Basic.__init__(self, settings, layer)
        self.font = pygame.font.SysFont(None, size, False, False)
        self.image = None
        self.textRect = None
        self.type = "text"
        self.msg = text
        self.alignment = "left"
        self.realTime = realTime
        self.focus = False
        self.prep()
        self.editTextSpace()

    def createBtn(self):
        self.type = "button"

    def createInput(self, align="left"):
        self.type = "input"
        self.realTime = True
        self.alignment = align
        self.color = self.settings.GREEN

    def changeTextSize(self, size=22):
        self.font = pygame.font.SysFont(None, size, False, False)
        self.prep()

    def prep(self):
        self.image = self.font.render(self.msg, True, self.settings.BLACK)
        self.textRect = self.image.get_rect()

    def setTextRect(self, pos):
        self.textRect.x, self.textRect.y = pos[0], pos[1]

    def getTextRect(self):
        return self.textRect.x, self.textRect.y

    def textPadding(self, xPadding=2, yPadding=0):
        """Adds extra space in graphical box to let text have padding"""
        if xPadding != 0:
            # self.rect.x -= xPadding/2
            self.rect.width += xPadding + 10
        if yPadding != 0:
            # self.rect.y -= yPadding/2
            self.rect.height += yPadding

    def editTextSpace(self):
        oldTextWid = self.textRect.width
        oldWidth, oldHeight = self.rect.width, self.rect.height
        self.prep()
        self.rect.width = oldWidth + (self.textRect.width - oldTextWid)
        self.rect.height = oldHeight
        if self.alignment == "right":
            self.rect.x -= (self.textRect.width - oldTextWid)
        elif self.alignment == "center":
            self.rect.x -= (self.textRect.width - oldTextWid)/2

    def centerText(self):
        """Center text within the graphical box"""
        self.textRect.x = self.rect.x + (self.rect.width - self.textRect.width) / 2
        self.textRect.y = self.rect.y + (self.rect.height - self.textRect.height) / 2

    def draw(self, screen):
        if self.realTime:
            self.editTextSpace()
        if self.focus:
            pygame.draw.rect(screen, self.settings.YELLOW, self.rect, self.border)
        elif self.fill:
            pygame.draw.rect(screen, self.color, self.rect, self.border)
        self.centerText()
        screen.blit(self.image, self.textRect)

class Polygon(Basic):
    def __init__(self, settings, layer, polyCords=""):
        Basic.__init__(self, settings, layer)
        self.polyCords = polyCords

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.polyCords)


class Holder(Basic):  # Can not put inputs within the holder, possibly skipped if placed inside
    def __init__(self, settings, layer):
        Basic.__init__(self, settings, layer)
        self.type = "hold"
        self.basicList = []  # [0] is the main anchor for other "basics"

    def addItems(self, items):
        self.basicList.extend(items)

    def printList(self):
        for i in self.basicList:
            print(i.__class__)

    def draw(self, screen):
        for i in self.basicList:
            i.draw(screen)
