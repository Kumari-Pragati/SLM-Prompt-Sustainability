import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(position_min([1, 2, 3, 2, 4]), [0, 3])

    def test_single_min_value(self):
        self.assertEqual(position_min([5, 5, 5, 5]), [0, 1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(position_min([]), [])

    def test_negative_numbers(self):
        self.assertEqual(position_min([-1, -2, -3, -2, -4]), [0, 2])

    def test_all_same_values(self):
        self.assertEqual(position_min([1, 1, 1, 1]), [0, 1, 2, 3])

    def test_large_list(self):
        self.assertEqual(position_min(list(range(1, 10001))), list(range(0, 10000, 9999)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            position_min("not a list")
