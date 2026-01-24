import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(position_min([1]), [0])

    def test_multiple_elements_same_min(self):
        self.assertEqual(position_min([1, 1, 2]), [0, 1])

    def test_multiple_elements_different_min(self):
        self.assertEqual(position_min([1, 2, 3]), [0, 2])

    def test_empty_list(self):
        self.assertEqual(position_min([]), [])

    def test_list_with_no_min(self):
        self.assertEqual(position_min([2, 3, 4]), [])

    def test_list_with_negative_numbers(self):
        self.assertEqual(position_min([-1, -2, -3]), [0, 1, 2])
