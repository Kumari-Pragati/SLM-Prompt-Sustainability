import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_Index(1), 1)
        self.assertEqual(find_Index(2), 2)
        self.assertEqual(find_Index(3), 3)
        self.assertEqual(find_Index(10), 4)
        self.assertEqual(find_Index(20), 5)

    def test_zero(self):
        self.assertEqual(find_Index(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_Index(-1), 0)
        self.assertEqual(find_Index(-2), -1)

    def test_large_numbers(self):
        self.assertEqual(find_Index(1000), 10)
        self.assertEqual(find_Index(2000), 11)

    def test_floating_point_numbers(self):
        self.assertEqual(find_Index(1.5), 2)
        self.assertEqual(find_Index(2.5), 3)
        self.assertEqual(find_Index(3.5), 4)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, find_Index, -2.5)
        self.assertRaises(ValueError, find_Index, "not_a_number")
