import pygame

class item:
    def __init__(self, settings, layer=10, msg="", edit=False, fill=False, keepMsg=False):
        self.settings = settings
        self.layer = layer
        self.text = False
        self.border = 0
        self.color = settings.GRAY4
        self.action = ""
        self.rect = pygame.Rect((0, 0), (50, 50))
        if msg != "":
            self.setText(msg, edit, fill)
        if not keepMsg:
            self.msg = ""

    def setText(self, msg, edit=False, fill=False):
        self.fill = fill
        self.focus = False
        self.text = True
        self.msg = msg
        self.font = pygame.font.SysFont(None, 20, False, False)
        self.image = self.font.render(msg, True, self.settings.BLACK)
        self.rect = self.image.get_rect()

    def setSize(self, width, height):
        self.rect.width, self.rect.height = width, height

    def setPos(self, tempX, tempY):
        self.rect.x, self.rect.y = tempX, tempY

    def resetFontSize(self, fontSize):
        self.font = pygame.font.SysFont(None, fontSize, False, False)

    def prep(self, msg=""):
        tempPos = (self.rect.x, self.rect.y)
        if msg == "":
            self.image = self.font.render(self.msg, True, self.settings.BLACK)
        else:
            self.image = self.font.render(msg, True, self.settings.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = tempPos[0], tempPos[1]

    def draw(self, screen):
        if self.text:
            if self.msg != "":
                self.prep()
            if self.focus:
                pygame.draw.rect(screen, self.settings.YELLOW, self.rect, self.border)
            elif self.fill:
                pygame.draw.rect(screen, self.color, self.rect, self.border)
            screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect, self.border)

