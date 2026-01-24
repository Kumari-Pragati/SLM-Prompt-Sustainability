import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(maximum_value([(1, [1, 2, 3]), (2, [4, 5, 6]), (3, [7, 8, 9])]), [(1, 3), (2, 6), (3, 9)])

    def test_empty_list(self):
        self.assertListEqual(maximum_value([(1, []), (2, [])]), [(1, None), (2, None)])

    def test_single_element_list(self):
        self.assertListEqual(maximum_value([(1, [1]), (2, [2]), (3, [3])]), [(1, 1), (2, 2), (3, 3)])

    def test_negative_numbers(self):
        self.assertListEqual(maximum_value([(1, [-1, -2, -3]), (2, [-4, -5, -6]), (3, [-7, -8, -9])]), [(1, -1), (2, -6), (3, -9)])

    def test_mixed_numbers(self):
        self.assertListEqual(maximum_value([(1, [1, -2, 3]), (2, [-4, 5, 6]), (3, [7, -8, 9])]), [(1, 1), (2, 6), (3, 9)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            maximum_value([(1, 'list'), (2, [1, 2, 3])])
