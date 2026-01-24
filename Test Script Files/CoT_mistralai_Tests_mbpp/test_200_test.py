import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(position_max([]), [])

    def test_single_element_list(self):
        self.assertEqual(position_max([1]), [0])

    def test_multiple_elements_list(self):
        self.assertEqual(position_max([1, 2, 3]), [2, 1])

    def test_max_at_beginning(self):
        self.assertEqual(position_max([3, 2, 1]), [0])

    def test_max_at_end(self):
        self.assertEqual(position_max([1, 2, 3]), [2])

    def test_max_in_middle(self):
        self.assertEqual(position_max([1, 3, 2]), [1])

    def test_duplicate_max_values(self):
        self.assertEqual(position_max([3, 3, 2]), [1, 2])

    def test_negative_numbers(self):
        self.assertEqual(position_max([-1, -2, -3]), [2])

    def test_mixed_positive_and_negative_numbers(self):
        self.assertEqual(position_max([1, -2, 3, -4]), [2, 3])

    def test_invalid_input_not_list(self):
        with self.assertRaises(TypeError):
            position_max("not a list")
