import unittest
from mbpp_718_code import alternate_elements

class TestAlternateElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], alternate_elements([]))

    def test_single_element_list(self):
        self.assertListEqual([1], alternate_elements([1]))
        self.assertListEqual([2], alternate_elements([2]))

    def test_even_length_list(self):
        self.assertListEqual([1, 2, 3], alternate_elements([1, 2, 3, 4]))
        self.assertListEqual([5, 6, 7, 8], alternate_elements([5, 6, 7, 8, 9]))

    def test_odd_length_list(self):
        self.assertListEqual([1, 2, 3, 4], alternate_elements([1, 2, 3, 4, 5]))
        self.assertListEqual([5, 6, 7, 8, 9, 10], alternate_elements([5, 6, 7, 8, 9, 10, 11]))

    def test_list_with_duplicates(self):
        self.assertListEqual([1, 2, 2, 3], alternate_elements([1, 2, 2, 3, 4]))
        self.assertListEqual([5, 6, 6, 7, 8], alternate_elements([5, 6, 6, 7, 8, 9]))

    def test_list_with_only_even_indices(self):
        self.assertListEqual([1, 3, 5], alternate_elements([1, 2, 3, 4, 5]))
        self.assertListEqual([5, 7, 9, 11], alternate_elements([5, 6, 7, 8, 9, 10, 11]))

    def test_list_with_only_odd_indices(self):
        self.assertListEqual([2], alternate_elements([1, 2, 3]))
        self.assertListEqual([6, 8, 10], alternate_elements([5, 6, 7, 8, 9]))
