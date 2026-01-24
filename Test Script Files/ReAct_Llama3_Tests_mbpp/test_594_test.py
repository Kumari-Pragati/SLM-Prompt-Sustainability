import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(diff_even_odd([]), -1)

    def test_single_element_list(self):
        self.assertEqual(diff_even_odd([5]), -1)

    def test_even_and_odd_elements(self):
        self.assertEqual(diff_even_odd([2, 5]), 2 - 5)

    def test_all_even_elements(self):
        self.assertEqual(diff_even_odd([2, 4, 6]), 2 - 2)

    def test_all_odd_elements(self):
        self.assertEqual(diff_even_odd([1, 3, 5]), -1 - 1)

    def test_mixed_elements(self):
        self.assertEqual(diff_even_odd([2, 1, 4, 3, 6]), 4 - 3)

    def test_list_with_duplicates(self):
        self.assertEqual(diff_even_odd([2, 2, 4, 4, 6, 6]), 6 - 4)

    def test_list_with_duplicates_and_odd(self):
        self.assertEqual(diff_even_odd([2, 2, 4, 4, 6, 6, 1, 3]), 6 - 3)
