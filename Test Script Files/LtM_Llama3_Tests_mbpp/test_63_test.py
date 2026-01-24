import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(max_difference([(1, 2), (3, 4)]), 1)

    def test_empty_list(self):
        self.assertEqual(max_difference([]), None)

    def test_single_element_list(self):
        self.assertEqual(max_difference([(1, 1)]), 0)

    def test_max_value(self):
        self.assertEqual(max_difference([(1, 10), (2, 20)]), 9)

    def test_min_value(self):
        self.assertEqual(max_difference([(1, 2), (3, 1)]), 1)

    def test_negative_values(self):
        self.assertEqual(max_difference([(-1, 1), (2, 3)]), 2)

    def test_large_values(self):
        self.assertEqual(max_difference([(1000, 2000), (3000, 4000)]), 1000)
