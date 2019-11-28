import unittest
import graphic
import pygame  # Needed to test if box appears on screen
import settings  # Needed to init basic item

class TestGraphic(unittest.TestCase):

    def setUp(self):
        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode((100, 100))

        print("Set Up")

    def tearDown(self):
        print("Tear Down")

    def test_createItem(self):
        self.testItem = graphic.item(self.settings, 1)
        self.testItem.color = (20, 20, 20)
        self.testItem.setPos(100, 200)  # sets item location to (100, 200)
        self.testItem.setSize(350, 100)  # sets item size to (350 Length, 100 Height)
        self.testItem.nudge(-50, -50, -50, -50) # moves -50 in both axis and reduces size -50 in both len/heig

        self.testItem.draw(self.screen)
        self.assertIsNotNone(self.testItem)
        self.assertEqual(self.testItem.rect.right, 350)  # checks right of box ends where it should


    def test_createText(self):
        pygame.init()
        self.testText = graphic.item(self.settings, 1, "asdzxc123789")

        self.assertIsNotNone(self.testText)
        self.assertEqual(self.testText.msg, "")

        self.testText.msg = "New Text: asdzxc123789"
        self.testText.prep()
        self.assertEqual(self.testText.msg, "New Text: asdzxc123789")


    def test_createPoly(self):
        self.testItem = graphic.item(self.settings, 1)
        self.assertIsNotNone(self.testItem)
        self.assertEqual(self.testItem.__class__, graphic.item)

if __name__ == '__main__':
    unittest.main()
