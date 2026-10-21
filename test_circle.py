import unittest
import math
from circle import *

class TestCircle(unittest.TestCase):
    def test_Area_positive(self):
        res = Area(3)

        self.assertEqual(res, math.pi * 3 * 3)

    def test_Area_1zero(self):
        res = Area(0)

        self.assertEqual(res, 0)


    def test_Area_negative(self):

        with self.assertRaises(ValueError):
            Area(-1)

    def test_Perimetr_positive(self):
        res = Perimetr(3)

        self.assertEqual(res, math.pi * 3)
    
    def test_Perimetr_1zero(self):
        res = Perimetr(0)

        self.assertEqual(res, 0)

    def test_Perimetr_negative(self):

        with self.assertRaises(ValueError):
            Perimetr(-1)

if __name__ == '__main__': 
    unittest.main()