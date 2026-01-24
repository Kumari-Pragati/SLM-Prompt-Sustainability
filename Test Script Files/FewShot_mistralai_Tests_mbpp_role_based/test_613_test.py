import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(maximum_value([(1, [1, 2, 3]), (2, [4, 5, 6]), (3, [7, 8, 9])]), [(3, 9)])

    def test_empty_list(self):
        self.assertEqual(maximum_value([(1, [])]), [(1, None)])

    def test_single_element_list(self):
        self.assertEqual(maximum_value([(1, [1])]), [(1, 1)])

    def test_negative_numbers(self):
        self.assertEqual(maximum_value([(1, [-1, -2, -3]), (2, [-4, -5, -6]), (3, [-7, -8, -9])]), [(3, -7)])

    def test_mixed_numbers(self):
        self.assertEqual(maximum_value([(1, [1, -2, 3]), (2, [-4, 5, 6]), (3, [-7, 8, 9])]), [(3, 9)])
