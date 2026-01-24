import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(find_Index(1), 3)

    def test_large_positive_integer(self):
        self.assertEqual(find_Index(5), 21)

    def test_negative_integer(self):
        with self.assertRaises(OverflowError):
            find_Index(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            find_Index('a')

    def test_edge_case_zero(self):
        with self.assertRaises(OverflowError):
            find_Index(0)
