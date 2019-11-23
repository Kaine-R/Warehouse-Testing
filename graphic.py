"""graphic.py, For creating items(graphical boxes/text for user interaction)"""
import pygame


class item:
    """Create base graphical box for menus"""
    def __init__(self, settings, layer=10, msg="", fill=False, keepMsg=False):
        self.settings = settings
        self.layer = layer
        self.rect = pygame.Rect((0, 0), (50, 50))
        self.color = settings.GRAY4
        self.text = False
        self.border = 0
        self.action = ""
        if msg != "":
            self.setText(msg, fill)
        if not keepMsg:
            self.msg = ""

    def setText(self, msg, fill=False):
        """Creates self.variables for base graphical boxes that will allow for text on screen"""
        self.focus = False
        self.text = True
        self.fill = fill
        self.msg = msg
        self.font = pygame.font.SysFont(None, 22, False, False)
        self.prep(msg)
        self.textPadding(5)

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

    def resetFontSize(self, fontSize):
        """Changes font size for graphical boxes (w/ text)"""
        self.font = pygame.font.SysFont(None, fontSize, False, False)
        self.prep(self.msg)

    def textPadding(self, xPadding, yPadding=0):
        """Adds extra space(xPadding, yPadding) in graphical box to let text have padding"""
        self.rect.x -= xPadding
        self.rect.width += xPadding + xPadding
        self.rect.y -= yPadding
        self.rect.height += yPadding + yPadding
        self.centerText()

    def centerText(self):
        """Center text within the graphical box"""
        self.textRect.x = self.rect.x + (self.rect.width - self.textRect.width) / 2
        self.textRect.y = self.rect.y + (self.rect.height - self.textRect.height) / 2

    def prep(self, msg=""):
        """Renders text to image to allow for screen blit, also updates change in text"""
        tempPos = (self.rect.x, self.rect.y)
        try:
            tempSize = (self.textRect.width, self.textRect.height)
        except:
            pass
        if msg == "":
            self.image = self.font.render(self.msg, True, self.settings.BLACK)
        else:
            self.image = self.font.render(msg, True, self.settings.BLACK)
        self.textRect = self.image.get_rect()
        self.textRect.x, self.textRect.y = tempPos[0], tempPos[1]
        try:
            self.rect.width += self.textRect.width - tempSize[0]
        except:
            self.rect.width = self.textRect.width
            self.textPadding(5)

    def addPolygon(self, polygonCords):
        """Adds self.poly, list of coordinates to create polygon for graph"""
        self.poly = polygonCords

    def draw(self, screen):
        """Draws graphical objects onto screen (boxes, text, polygons)"""
        if self.text:
            if self.msg != "":
                self.prep()
            if self.focus:
                pygame.draw.rect(screen, self.settings.YELLOW, self.rect, self.border)
            elif self.fill:
                pygame.draw.rect(screen, self.color, self.rect, self.border)
            self.centerText()
            screen.blit(self.image, self.textRect)
        else:
            pygame.draw.rect(screen, self.color, self.rect, self.border)
        try:
            pygame.draw.polygon(screen, self.color, self.poly)
        except:
            pass

class placeholder:
    """Barebone variables of graphical box, purpose to allow for size/pos to be passed to another"""
    def __init__(self, parent=""):
        if parent == "":
            self.rect = pygame.Rect(50, 50, 50, 50)
        else:
            self.rect = parent

    def setSize(self, width, height):
        """Set Size of placeholder"""
        self.rect.width, self.rect.height = width, height

    def getSize(self):
        """Return Size of placeholder"""
        return self.rect.width, self.rect.height

    def setPos(self, tempX, tempY):
        """Set Position of placeholder"""
        self.rect.x, self.rect.y = tempX, tempY

    def getPos(self):
        """Get Position of placeholder"""
        return self.rect.x, self.rect.y

    def nudge(self, xNudge=0, yNudge=0, widNudge=0, heiNudge=0):
        """Allows for changes in position(xNudge, yNudge) and size(weiNudge, heiNudge)"""
        self.rect.x += xNudge
        self.rect.y += yNudge
        self.rect.width += widNudge
        self.rect.height += heiNudge

    def draw(self, screen):
        """Draw placeholder onto screen (shouldn't be called)"""
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
