from dre2 import color
import unittest

class TestTextColor(unittest.TestCase):
    """Test"""

    def testtextcolor(self):
        """Test"""
        resultcolor = color
        self.assertEqual(resultcolor, (255, 0, 0))

if __name__ == "__main__":
    test = TestTextColor()
    test.testtextcolor()
