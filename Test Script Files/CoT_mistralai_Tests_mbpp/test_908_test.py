import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_fixed_point([], 0), -1)

    def test_single_element(self):
        self.assertEqual(find_fixed_point([0], 1), 0)

    def test_single_element_wrong(self):
        self.assertEqual(find_fixed_point([1], 1), -1)

    def test_multiple_elements(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10), 9)

    def test_multiple_elements_wrong(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), -1)

    def test_negative_list(self):
        self.assertEqual(find_fixed_point([-1, -2, -3], 3), -1)

    def test_negative_list_wrong(self):
        self.assertEqual(find_fixed_point([-1, -2, -3, -4], 3), -1)

    def test_negative_number(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], -1), -1)

    def test_negative_number_wrong(self):
        self.assertEqual(find_fixed_point([-1, -2, -3, -4], -1), -1)

    def test_non_integer_input(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10.5), -1)
