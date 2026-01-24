import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(find_fixed_point([], 10), -1)

    def test_single_element_array(self):
        self.assertEqual(find_fixed_point([0], 1), -1)
        self.assertEqual(find_fixed_point([1], 1), 1)

    def test_fixed_point_in_middle(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 2], 5), 2)

    def test_fixed_point_at_beginning(self):
        self.assertEqual(find_fixed_point([1, 2, 3, 1], 4), 1)

    def test_fixed_point_at_end(self):
        self.assertEqual(find_fixed_point([1, 2, 3, 1], 5), -1)

    def test_negative_index(self):
        self.assertEqual(find_fixed_point([1, 2, 3], -1), -1)

    def test_negative_n(self):
        self.assertEqual(find_fixed_point([1, 2, 3], 0), -1)

    def test_array_with_no_fixed_point(self):
        self.assertEqual(find_fixed_point([1, 2, 3, 4], 10), -1)
