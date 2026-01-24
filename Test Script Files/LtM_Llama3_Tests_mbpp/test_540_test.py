import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(find_Diff([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(find_Diff([1], 1), 0)

    def test_two_elements_array(self):
        self.assertEqual(find_Diff([1, 2], 2), 0)

    def test_repeated_elements_array(self):
        self.assertEqual(find_Diff([1, 1, 2, 2], 4), 0)

    def test_max_min_diff(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5], 5), 4)

    def test_max_min_diff_with_repeated_elements(self):
        self.assertEqual(find_Diff([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 10), 4)

    def test_max_min_diff_with_repeated_elements_and_zero(self):
        self.assertEqual(find_Diff([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 12), 4)

    def test_max_min_diff_with_repeated_elements_and_zero_at_end(self):
        self.assertEqual(find_Diff([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 0], 12), 4)

    def test_max_min_diff_with_repeated_elements_and_zero_at_start(self):
        self.assertEqual(find_Diff([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 0], 12), 4)

    def test_max_min_diff_with_repeated_elements_and_zero_at_start_and_end(self):
        self.assertEqual(find_Diff([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 0, 0], 13), 4)
