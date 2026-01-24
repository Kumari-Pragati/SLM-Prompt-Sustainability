import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):

    def test_find_index_with_positive_integer(self):
        self.assertAlmostEqual(find_Index(1), 1.4142135623730951)
        self.assertAlmostEqual(find_Index(2), 2.8284271247461903)
        self.assertAlmostEqual(find_Index(3), 4.242640687119285)
        self.assertAlmostEqual(find_Index(4), 5.656854249492382)
        self.assertAlmostEqual(find_Index(5), 7.071067811865255)

    def test_find_index_with_zero(self):
        self.assertEqual(find_Index(0), 0.0)

    def test_find_index_with_negative_integer(self):
        self.assertRaises(ValueError, find_Index, -1)
