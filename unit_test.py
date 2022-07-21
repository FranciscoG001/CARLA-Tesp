from dre2 import data1input, data2input
import unittest

class TestDic(unittest.TestCase):
    """Test"""

    def testdic1(self):
        """Test"""
        if len(data1input) == 0:
            resultdic = False
        else:
            resultdic = True
        self.assertEqual(resultdic, True)

    def testdic2(self):
        """Test"""
        if len(data2input) == 0:
            resultdic = False
        else:
            resultdic = True
        self.assertEqual(resultdic, True)
