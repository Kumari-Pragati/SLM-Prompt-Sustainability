import unittest
from mbpp_739_code import sqrt, pow
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):
    def test_find_Index(self):
        self.assertEqual(find_Index(1), 3)
        self.assertEqual(find_Index(2), 10)
        self.assertEqual(find_Index(3), 32)
        self.assertEqual(find_Index(4), 100)
        self.assertEqual(find_Index(5), 317)
        self.assertEqual(find_Index(6), 1000)
        self.assertEqual(find_Index(7), 3163)
        self.assertEqual(find_Index(8), 10000)
        self.assertEqual(find_Index(9), 31623)
        self.assertEqual(find_Index(10), 100000)
