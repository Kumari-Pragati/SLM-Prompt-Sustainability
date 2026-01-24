import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(position_min([1, 2, 3, 2, 1]), [0, 3])

    def test_single_min_value(self):
        self.assertEqual(position_min([5, 6, 7, 8, 9]), [0])

    def test_empty_list(self):
        self.assertEqual(position_min([]), [])

    def test_negative_numbers(self):
        self.assertEqual(position_min([-1, -2, -3, -2, -1]), [0, 2])

    def test_duplicate_min_values(self):
        self.assertEqual(position_min([1, 2, 1, 2, 3]), [0, 2])

    def test_large_numbers(self):
        self.assertEqual(position_min([1000000, 2000000, 3000000]), [0])

    def test_float_numbers(self):
        self.assertEqual(position_min([1.1, 2.2, 3.3, 2.2, 1.1]), [0, 3])

    def test_string_list(self):
        with self.assertRaises(TypeError):
            position_min(['a', 'b', 'c', 'b', 'a'])

    def test_mixed_list(self):
        with self.assertRaises(TypeError):
            position_min([1, 'a', 2, 'b', 3])
