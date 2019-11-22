import pygame


class item:
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
        self.focus = False
        self.text = True
        self.fill = fill
        self.msg = msg
        self.font = pygame.font.SysFont(None, 22, False, False)
        self.prep(msg)
        self.textPadding(5)

    def setImage(self):
        self.image = pygame.image.load("warehouseLogo.jpg")
        self.rect = self.image.get_rect()

    def setSize(self, width, height):
        self.rect.width, self.rect.height = width, height

    def setPos(self, tempX, tempY):
        self.rect.x, self.rect.y = tempX, tempY

    def getPos(self):
        return self.rect.x, self.rect.y

    def nudge(self, xNudge=0, yNudge=0, widNudge=0, heiNudge=0):
        self.rect.x += xNudge
        self.rect.y += yNudge
        self.rect.width += widNudge
        self.rect.height += heiNudge

    def resetFontSize(self, fontSize):
        self.font = pygame.font.SysFont(None, fontSize, False, False)
        self.prep(self.msg)

    def textPadding(self, xPadding, yPadding=0):
        self.rect.x -= xPadding
        self.rect.width += xPadding + xPadding
        self.rect.y -= yPadding
        self.rect.height += yPadding + yPadding
        self.centerText()

    def centerText(self):
        self.textRect.x = self.rect.x + (self.rect.width - self.textRect.width) / 2
        self.textRect.y = self.rect.y + (self.rect.height - self.textRect.height) / 2

    def prep(self, msg=""):
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
        self.poly = polygonCords

    def draw(self, screen):
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
    def __init__(self, parent=""):
        if parent == "":
            self.rect = pygame.Rect(50, 50, 50, 50)
        else:
            self.rect = parent

    def setSize(self, width, height):
        self.rect.width, self.rect.height = width, height

    def getSize(self):
        return self.rect.width, self.rect.height

    def setPos(self, tempX, tempY):
        self.rect.x, self.rect.y = tempX, tempY

    def getPos(self):
        return self.rect.x, self.rect.y

    def nudge(self, xNudge=0, yNudge=0, widNudge=0, heiNudge=0):
        self.rect.x += xNudge
        self.rect.y += yNudge
        self.rect.width += widNudge
        self.rect.height += heiNudge

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
