import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(position_min([5, 2, 7, 2, 4]), [1, 3])

    def test_single_min_value(self):
        self.assertEqual(position_min([5, 2, 7, 8, 4]), [1])

    def test_empty_list(self):
        self.assertEqual(position_min([]), [])

    def test_list_with_same_min_values(self):
        self.assertEqual(position_min([2, 2, 7, 8, 4]), [0, 1])

    def test_negative_numbers(self):
        self.assertEqual(position_min([-5, -2, -7, -2, -4]), [1, 3])

    def test_large_numbers(self):
        self.assertEqual(position_min([1000000, 2, 7, 8, 4]), [1])

    def test_float_numbers(self):
        self.assertEqual(position_min([1.5, 2.5, 7.5, 8.5, 4.5]), [0, 1])

    def test_string_list(self):
        with self.assertRaises(TypeError):
            position_min(['a', 'b', 'c', 'd'])
