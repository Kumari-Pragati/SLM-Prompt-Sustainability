import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(position_max([]), [])

    def test_single_element_list(self):
        self.assertListEqual(position_max([1]), [0])

    def test_multiple_elements_same_value(self):
        self.assertListEqual(position_max([1, 1, 2]), [0, 1])

    def test_multiple_elements_different_values(self):
        self.assertListEqual(position_max([1, 2, 3]), [1, 2])

    def test_max_at_beginning(self):
        self.assertListEqual(position_max([5, 1, 2, 3]), [0])

    def test_max_at_end(self):
        self.assertListEqual(position_max([1, 5, 2, 3]), [2])

    def test_max_in_middle(self):
        self.assertListEqual(position_max([1, 2, 5, 3]), [1])

    def test_negative_numbers(self):
        self.assertListEqual(position_max([-1, -2, -3]), [0, 1])

    def test_floats(self):
        self.assertListEqual(position_max([1.1, 2.2, 3.3]), [0, 1])

    def test_mixed_types(self):
        self.assertListEqual(position_max([1, 'a', 2]), [0, 2])

    def test_list_with_none(self):
        self.assertListEqual(position_max([None, 1, 2]), [1])
