import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Diff([1, 2, 2, 3, 4, 4, 4, 5, 6], 9), 2)

    def test_single_element(self):
        self.assertEqual(find_Diff([5], 1), 0)

    def test_empty_array(self):
        self.assertEqual(find_Diff([], 0), 0)

    def test_all_same_elements(self):
        self.assertEqual(find_Diff([1, 1, 1, 1, 1], 5), 0)

    def test_all_different_elements(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5], 5), 4)

    def test_negative_numbers(self):
        self.assertEqual(find_Diff([-1, 0, 1, 2, 2], 5), 1)

    def test_large_numbers(self):
        self.assertEqual(find_Diff([1000, 2000, 2000, 3000, 4000], 5), 1)

    def test_large_array(self):
        self.assertEqual(find_Diff(list(range(1, 10001)), 10000), 9999)
