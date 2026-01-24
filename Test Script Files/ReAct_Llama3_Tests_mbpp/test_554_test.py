import unittest
from mbpp_554_code import Split

class TestSplit(unittest.TestCase):
    def test_even_list(self):
        self.assertEqual(Split([2, 4, 6, 8]), [])

    def test_odd_list(self):
        self.assertEqual(Split([1, 3, 5, 7]), [1, 3, 5, 7])

    def test_mixed_list(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6, 7, 8]), [1, 3, 5, 7])

    def test_empty_list(self):
        self.assertEqual(Split([]), [])

    def test_single_element_list(self):
        self.assertEqual(Split([5]), [5])

    def test_list_with_duplicates(self):
        self.assertEqual(Split([1, 2, 3, 2, 4, 5, 3, 6]), [1, 3, 5])
