import unittest
from triangle import *

class TestRectangle(unittest.TestCase):
    def test_Area_positive(self):
        res = Area(3, 4)

        self.assertEqual(res, 6)

    def test_Area_1zero(self):
        res = Area(0, 18)

        self.assertEqual(res, 0)

    def test_Area_2zero(self):
        res = Area(0, 0)

        self.assertEqual(res, 0)

    def test_Area_negative(self):

        with self.assertRaises(ValueError):
            Area(-1, -1)

    def test_Perimetr_positive(self):
        res = Perimetr(3, 4, 5)

        self.assertEqual(res, 12)
    
    def test_Perimetr_1zero(self):

        with self.assertRaises(ValueError):
            Perimetr(0, 6, 7)

    def test_Perimetr_2zero(self):

        with self.assertRaises(ValueError):
            Perimetr(0, 0, 7)

    def test_Perimetr_negative(self):

        with self.assertRaises(ValueError):
            Perimetr(-1, -1, -1)

if __name__ == '__main__': 
    unittest.main()