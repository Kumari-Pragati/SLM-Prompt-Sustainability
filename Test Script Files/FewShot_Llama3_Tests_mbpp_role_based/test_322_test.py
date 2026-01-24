import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(position_min([5]), [0])

    def test_multiple_elements_list(self):
        self.assertEqual(position_min([5, 2, 8, 12]), [0, 1])

    def test_list_with_duplicates(self):
        self.assertEqual(position_min([5, 2, 8, 2, 12]), [0, 1, 2, 3])

    def test_list_with_negative_numbers(self):
        self.assertEqual(position_min([-5, -2, -8, -12]), [0, 1, 2, 3])

    def test_list_with_zero(self):
        self.assertEqual(position_min([0, 2, 8, 12]), [0])

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            position_min([])
