"""Kaine Rubalcava  Main.py"""
import pygame
from settings import Settings
import createMenu
import gameFunction as gf

import graphic  # for testing
import graphicResize as gr
# main.py graphicResize.py gameFunction.py createMenu.py graphic.py settings.py

def runWarehouse():
    """Main Function (init lists and starts main loop)"""
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    pygame.display.set_caption("Warehouse Game")
    lastAction = ["menu"]
    lastGraph = ["list"]
    pageNum = [0]

    warehouse = [5, 5, 5]  # Testing, size is always 5, 5, 5

    boxList = []
    backOrder = []
    objectList = []

    createMenu.createBG(settings, objectList)
    createMenu.createMainMenu(settings, objectList)
    createMenu.getList(objectList, boxList, pageNum)
    img = pygame.image.load("warehouseLogo.png")

    repeat = True
    while repeat:
        screen.fill((0, 0, 0))

        # sss += 1
        # if sss == 20:
        #     objectList.append(testHolder)
        #     testHolder.printList()
        # if sss%500 == 0 and sss > 0:
        #     bname.msg += str(sss%499)
        # print("-----------")
        # boxInfo = [0, 0, [2, 2, 2]]
        # pos = [0, 0, 0]
        # for h in range(pos[2], boxInfo[2][2] + pos[2]):
        #     for l in range(pos[1], boxInfo[2][1] + pos[1]):
        #         for w in range(pos[0], boxInfo[2][0] + pos[0]):
        #             print(w, l, h)
        # print("-----------")
        i = 0
        for item in objectList:
            i = item.layer if item.layer > i else i
            item.draw(screen)
        if i == 2:
            screen.blit(img, (460, 250))

        gf.checkEvents(objectList, boxList, backOrder, warehouse, lastAction, lastGraph, pageNum)

        pygame.display.flip()


runWarehouse()
