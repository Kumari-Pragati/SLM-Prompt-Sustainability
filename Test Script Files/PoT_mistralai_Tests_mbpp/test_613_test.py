import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(maximum_value([(1, [2, 3]), (2, [4, 5]), (3, [6, 7])]), [(1, 3), (2, 5), (3, 7)])

    def test_empty_list(self):
        self.assertEqual(maximum_value([(1, [])]), [(1, None)])

    def test_single_element_list(self):
        self.assertEqual(maximum_value([(1, [1])]), [(1, 1)])

    def test_single_key_multiple_values(self):
        self.assertEqual(maximum_value([(1, [1, 2]), (2, [3, 4])]), [(1, 2), (2, 4)])

    def test_negative_numbers(self):
        self.assertEqual(maximum_value([(1, [-2, -1]), (2, [-3, -4])]), [(1, -1), (2, -3)])

    def test_no_maximum_value(self):
        self.assertEqual(maximum_value([(1, [0, -1]), (2, [0, -2])]), [(1, 0), (2, 0)])
