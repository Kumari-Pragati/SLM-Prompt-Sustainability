import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(position_min([]), [])

    def test_single_element_list(self):
        self.assertListEqual(position_min([1]), [0])

    def test_multiple_elements_equal_min(self):
        self.assertListEqual(position_min([1, 1, 2]), [0, 1])

    def test_multiple_elements_different_min(self):
        self.assertListEqual(position_min([1, 2, 1]), [0, 2])

    def test_min_not_in_list(self):
        self.assertListEqual(position_min([2, 3, 4]), [])

    def test_min_at_first_position(self):
        self.assertListEqual(position_min([1, 2, 1]), [0])

    def test_min_at_last_position(self):
        self.assertListEqual(position_min([1, 2, 1]), [2])

    def test_min_in_middle_position(self):
        self.assertListEqual(position_min([1, 2, 1]), [1])

    def test_negative_numbers(self):
        self.assertListEqual(position_min([-1, -2, -3]), [0, 1])

    def test_floats(self):
        self.assertListEqual(position_min([1.1, 2.2, 1.1]), [0, 2])

    def test_strings(self):
        self.assertListEqual(position_min(["a", "b", "a"]), [0, 2])
