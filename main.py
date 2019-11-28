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

    sss = 0
    # testBase = graphic.Basic(settings, 20)
    # testBase.nudge(50, 10)
    # testText = graphic.Text(settings, 20, "Test String", True)
    # testText.textPadding(8, 6)
    # testText.nudge(50, 100)
    # testPoly = graphic.Polygon(settings, 20)
    # testPoly.polyCords = [(50, 150), (70, 170), (50, 190), (50, 170)]
    # testHolder = graphic.Holder(settings, 20)
    # testHolder.addItems([testBase, testText, testPoly])

    # b = graphic.Basic(settings, 20)
    # b.nudge(50, 75, 240, 100)
    # bname = graphic.Text(settings, 20, "Name", True)
    # # bname.nudge(50, 75)
    # gr.setLeft(b, bname)
    # bpos = graphic.Text(settings, 20, "Pos")
    # bpos.alignment = "right"
    # gr.setRight(b, bpos)
    # bcomment = graphic.Text(settings, 20, "Comment")
    # bcomment.alignemnt = "center"
    # bcomment.changeTextSize(10)
    # gr.setDown(b, bcomment)
    # testHolder = graphic.Holder(settings, 20)
    # testHolder.addItems([b, bname, bpos, bcomment])




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

        i = 0
        for item in objectList:
            i = item.layer if item.layer > i else i
            item.draw(screen)
        if i == 2:
            screen.blit(img, (460, 250))

        gf.checkEvents(objectList, boxList, backOrder, warehouse, lastAction, lastGraph, pageNum)

        pygame.display.flip()


runWarehouse()
