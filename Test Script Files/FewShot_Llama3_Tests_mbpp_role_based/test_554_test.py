import unittest
from mbpp_554_code import Split

class TestSplit(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Split([]), [])

    def test_all_even_numbers(self):
        self.assertEqual(Split([2, 4, 6, 8]), [])

    def test_all_odd_numbers(self):
        self.assertEqual(Split([1, 3, 5, 7]), [1, 3, 5, 7])

    def test_mixed_numbers(self):
        self.assertEqual(Split([2, 1, 4, 3, 6, 5]), [1, 3, 5])

    def test_single_even_number(self):
        self.assertEqual(Split([4]), [])

    def test_single_odd_number(self):
        self.assertEqual(Split([1]), [1])
