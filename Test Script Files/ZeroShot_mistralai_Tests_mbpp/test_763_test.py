import unittest
from763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_Min_Diff([], 0), 0)

    def test_single_element(self):
        self.assertEqual(find_Min_Diff([1], 1), 0)

    def test_two_elements(self):
        self.assertEqual(find_Min_Diff([1, 2], 2), 0)

    def test_three_elements(self):
        self.assertEqual(find_Min_Diff([1, 2, 3], 3), 0)

    def test_four_elements(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4], 4), 0)

    def test_five_elements(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_Min_Diff([-1, -2, -3, -4], 4), 1)

    def test_large_numbers(self):
        self.assertEqual(find_Min_Diff([1000000001, 1000000002, 1000000003, 1000000004], 4), 1)

    def test_duplicates(self):
        self.assertEqual(find_Min_Diff([1, 1, 2, 2, 3], 5), 0)

    def test_large_duplicates(self):
        self.assertEqual(find_Min_Diff([1000000001, 1000000001, 1000000002, 1000000003, 1000000004], 5), 0)
