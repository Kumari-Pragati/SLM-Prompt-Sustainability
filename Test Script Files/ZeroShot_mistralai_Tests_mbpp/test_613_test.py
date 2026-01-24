import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(maximum_value([]), [])

    def test_single_element_list(self):
        self.assertEqual(maximum_value([(1, [1])]), [(1, 1)])

    def test_multiple_elements_list(self):
        self.assertEqual(maximum_value([(1, [1, 2, 3]), (2, [4, 5, 6]), (3, [7, 8, 9])]),
                         [(1, 3), (2, 6), (3, 9)])

    def test_negative_numbers(self):
        self.assertEqual(maximum_value([(1, [-1, -2, -3]), (2, [-4, -5, -6]), (3, [-7, -8, -9])]),
                         [(1, -1), (2, -4), (3, -7)])

    def test_mixed_numbers(self):
        self.assertEqual(maximum_value([(1, [1, -2, 3]), (2, [4, -5, 6]), (3, [7, -8, 9])]),
                         [(1, 3), (2, 6), (3, 9)])
