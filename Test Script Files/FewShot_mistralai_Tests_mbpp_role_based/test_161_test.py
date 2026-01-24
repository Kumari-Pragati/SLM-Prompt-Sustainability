import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):
    def test_empty_lists(self):
        self.assertListEqual(remove_elements([], []), [])
        self.assertListEqual(remove_elements([], [1]), [])
        self.assertListEqual(remove_elements([], [1, 2, 3]), [])

    def test_single_element_lists(self):
        self.assertListEqual(remove_elements([1], []), [1])
        self.assertListEqual(remove_elements([1], [1]), [])
        self.assertListEqual(remove_elements([1], [2, 3]), [1])

    def test_lists_with_duplicates(self):
        self.assertListEqual(remove_elements([1, 1, 2, 2, 3, 3], [1, 2]), [3])
        self.assertListEqual(remove_elements([1, 1, 2, 2, 3, 3], [2, 3]), [1])

    def test_lists_with_no_matches(self):
        self.assertListEqual(remove_elements([1, 2, 3], [4, 5]), [1, 2, 3])

    def test_lists_with_negative_numbers(self):
        self.assertListEqual(remove_elements([-1, 0, 1], [-1, 2]), [0, 1])
        self.assertListEqual(remove_elements([-1, 0, 1], [2, 3]), [-1, 0, 1])
