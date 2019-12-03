"""graphic.py, For creating items(graphical boxes/text for user interaction)"""
import pygame


class Basic:
    """Most Basic display box (no text or actions)"""
    def __init__(self, settings, layer, fill=True):
        """Create Basic for other on screen objects"""
        self.type = "basic"
        self.action = ""
        self.settings = settings
        self.layer = layer
        self.rect = pygame.Rect((0, 0), (40, 40))
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

    def draw(self, screen):
        """Draws the box based on rect"""
        pygame.draw.rect(screen, self.color, self.rect, self.border)


class Text(Basic):
    """Uses "Basic() and adds text to it (can be used to make btns/user Input)"""
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
        self.rect.width = self.textRect.width + 20 if self.textRect.width > self.rect.width else self.rect.width

    def createBtn(self):
        """changes some values to be a button"""
        self.color = self.settings.GRAY3
        self.type = "button"

    def createInput(self, align="left"):
        """Changes some values to take input"""
        self.type = "input"
        self.realTime = True
        self.alignment = align
        self.color = self.settings.GREEN

    def createTitle(self):
        """Change the look of the text"""
        self.changeTextSize(26, False, True)
        self.fill = False

    def changeTextSize(self, size=22, bold=False, italic=False):
        """Changes the Size of text"""
        self.font = pygame.font.SysFont(None, size, bold, italic)
        self.prep()

    def prep(self):
        """Redefines image that gets displayed on screen based on textRect position"""
        self.image = self.font.render(self.msg, True, self.settings.BLACK)
        self.textRect = self.image.get_rect()

    def setTextRect(self, pos):
        """sets textRect cords (where the text will display)"""
        self.textRect.x, self.textRect.y = pos[0], pos[1]

    def getTextRect(self):
        """get textRect position (x, y)"""
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
        """When text edited, changes box to match text change width"""
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
        """Updates text if input, then draws Basic and text"""
        if self.realTime:
            self.editTextSpace()
        if self.focus:
            pygame.draw.rect(screen, self.settings.YELLOW, self.rect, self.border)
        elif self.fill:
            pygame.draw.rect(screen, self.color, self.rect, self.border)
        self.centerText()
        screen.blit(self.image, self.textRect)


class Polygon(Basic):
    """For displaying the boxList in a 3D space"""
    def __init__(self, settings, layer, polyCords=""):
        Basic.__init__(self, settings, layer)
        self.polyCords = polyCords

    def draw(self, screen):
        """Draws the polygon onto screen"""
        pygame.draw.polygon(screen, self.color, self.polyCords)


class Holder(Basic):  # Can not put inputs within the holder, possibly skipped if placed inside
    """Container for Basic and Text. May not work with inputs or btns"""
    def __init__(self, settings, layer):
        Basic.__init__(self, settings, layer)
        self.type = "hold"
        self.color = settings.GRAY5
        self.basicList = []  # [0] is the main anchor for other "basics"

    def addItems(self, items):
        """Add items to holder list"""
        self.basicList.extend(items)

    def printList(self):
        """Prints whats currently on list"""
        for i in self.basicList:
            print(i.__class__)

    def draw(self, screen):
        """Draws all objects in basicList"""
        Basic.draw(self, screen)
        for i in self.basicList:
            i.draw(screen)
