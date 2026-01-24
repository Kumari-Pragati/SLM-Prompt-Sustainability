import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):
    def test_positive_integer(self):
        self.assertAlmostEqual(find_Index(1), math.sqrt(20))
        self.assertAlmostEqual(find_Index(2), math.sqrt(80))
        self.assertAlmostEqual(find_Index(3), math.sqrt(160))

    def test_zero(self):
        self.assertEqual(find_Index(0), 0)

    def test_negative_integer(self):
        self.assertRaises(ValueError, find_Index, -1)

    def test_floating_point(self):
        self.assertRaises(ValueError, find_Index, 0.5)
