import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):
    def test_single_element_array(self):
        self.assertEqual(find_Diff([1], 1), 0)

    def test_empty_array(self):
        self.assertEqual(find_Diff([]), 0)

    def test_array_with_one_pair(self):
        self.assertEqual(find_Diff([1, 1]), 0)

    def test_array_with_multiple_pairs(self):
        self.assertEqual(find_Diff([1, 1, 2, 2, 3, 3]), 2)

    def test_array_with_single_odd_element(self):
        self.assertEqual(find_Diff([1, 1, 2, 2, 3]), 1)

    def test_array_with_single_even_element(self):
        self.assertEqual(find_Diff([2, 2, 2, 3]), 0)

    def test_array_with_only_even_elements(self):
        self.assertEqual(find_Diff([2, 2, 4, 6]), 0)

    def test_array_with_only_odd_elements(self):
        self.assertEqual(find_Diff([1, 3, 5, 7]), 0)

    def test_array_with_mixed_even_and_odd_elements(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5]), 1)

    def test_array_with_duplicates_at_beginning(self):
        self.assertEqual(find_Diff([1, 1, 2, 2, 3], 3), 1)

    def test_array_with_duplicates_at_end(self):
        self.assertEqual(find_Diff([1, 2, 2, 3, 3], 4), 1)

    def test_array_with_duplicates_in_middle(self):
        self.assertEqual(find_Diff([1, 2, 2, 2, 3], 4), 1)
