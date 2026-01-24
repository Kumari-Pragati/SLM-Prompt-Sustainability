import unittest
from mbpp_502_code import find

class TestFind(unittest.TestCase):

    def test_find_positive_numbers(self):
        self.assertEqual(find(10, 3), 1)
        self.assertEqual(find(15, 5), 0)
        self.assertEqual(find(20, 7), 6)

    def test_find_negative_numbers(self):
        self.assertEqual(find(-10, 3), -1)
        self.assertEqual(find(-15, 5), 0)
        self.assertEqual(find(-20, 7), -6)

    def test_find_zero(self):
        self.assertEqual(find(0, 3), 0)
        self.assertEqual(find(0, 0), None)

    def test_find_large_numbers(self):
        self.assertEqual(find(1000000, 1000), 0)
        self.assertEqual(find(999999, 1000), 999)
