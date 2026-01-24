import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(position_max([1, 2, 3, 4, 5]), [4])

    def test_single_max_value(self):
        self.assertEqual(position_max([5, 4, 3, 2, 1]), [0])

    def test_multiple_max_values(self):
        self.assertEqual(position_max([1, 2, 3, 3, 1]), [2, 4])

    def test_empty_list(self):
        self.assertEqual(position_max([]), [])

    def test_negative_numbers(self):
        self.assertEqual(position_max([-1, -2, -3, -4, -5]), [4])

    def test_mixed_numbers(self):
        self.assertEqual(position_max([-1, 2, -3, 4, -5]), [3])

    def test_max_at_start(self):
        self.assertEqual(position_max([5, 1, 2, 3, 4]), [0])

    def test_max_at_end(self):
        self.assertEqual(position_max([1, 2, 3, 4, 5]), [4])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            position_max("not a list")
