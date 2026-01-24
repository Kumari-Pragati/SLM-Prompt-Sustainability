import unittest
from mbpp_275_code import get_Position

class TestGetPosition(unittest.TestCase):

    def test_get_position_empty_list(self):
        with self.assertRaises(ValueError):
            get_Position([], 1, 2)

    def test_get_position_single_element(self):
        self.assertEqual(get_Position([1], 1, 2), 1)

    def test_get_position_multiple_elements(self):
        self.assertEqual(get_Position([1, 2, 3, 4, 5], 5, 2), 5)

    def test_get_position_negative_numbers(self):
        self.assertEqual(get_Position([-1, -2, -3, -4, -5], 5, 2), 1)

    def test_get_position_zero(self):
        self.assertEqual(get_Position([0], 1, 2), 1)

    def test_get_position_maximum_value(self):
        self.assertEqual(get_Position([2147483647], 1, 2), 1)

    def test_get_position_maximum_value_with_zero(self):
        self.assertEqual(get_Position([2147483647, 0], 1, 2), 2)
