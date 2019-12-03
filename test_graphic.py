"""Test the creation of Basic, Tex, Polygon items"""
import unittest
import pygame  # Needed to test if box appears on screen
import graphic
import settings  # Needed to init basic item


class TestGraphic(unittest.TestCase):
    """Testing all 3 display items (Basic, Text, Polygon) with some functions"""
    def setUp(self):
        """Done at the beginning of every test"""
        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode((100, 100))
        print("Set Up")

    def tearDown(self):
        """Done at the end of every test"""
        print("Tear Down")

    def test_createItem(self):
        """Creates Basic display item and tests functions"""
        self.testBasic = graphic.Basic(self.settings, 1)
        self.assertEqual(self.testBasic.__class__, graphic.Basic)

        self.testBasic.color = (20, 20, 20)
        self.testBasic.setPos(100, 200)  # sets item location to (100, 200)
        self.testBasic.setSize(350, 100)  # sets item size to (350 Length, 100 Height)
        self.testBasic.nudge(-50, -50, -50, -50)  # moves -50 in both axis and reduces size -50 in both len/heig

        self.testBasic.draw(self.screen)
        self.assertEqual(self.testBasic.rect.right, 350)  # checks right of box ends where it should

    def test_createText(self):
        """Creates Text display item and tests functions"""
        pygame.init()
        self.testText = graphic.Text(self.settings, 1, "asdzxc123789")
        self.assertEqual(self.testText.__class__, graphic.Text)

        self.assertIsNotNone(self.testText)
        self.assertEqual(self.testText.msg, "asdzxc123789")

        self.testText.msg = "New Text: 12zx!"
        self.testText.prep()
        self.assertEqual(self.testText.msg, "New Text: 12zx!")

        self.testText.draw(self.screen)

    def test_createPoly(self):
        """Creates Polygon display item and tests functions"""
        self.testPoly = graphic.Polygon(self.settings, 20)
        self.testPoly.polyCords = [(50, 150), (70, 170), (50, 190), (50, 170)]
        self.assertEqual(self.testPoly.__class__, graphic.Polygon)

        self.testPoly.draw(self.screen)


if __name__ == '__main__':
    unittest.main()
