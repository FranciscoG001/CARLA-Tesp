import dre2
import unittest
import pygame

class TestTextColor(unittest.TestCase):
    """Test"""

    def testtextcolor(self):
        """Test"""
        resultcolor = dre2.color
        self.assertEqual(resultcolor, (255, 0, 0))