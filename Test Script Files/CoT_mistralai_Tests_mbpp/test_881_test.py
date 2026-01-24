import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):
    def test_empty_list(self):
        self.assertIs(sum_even_odd([]), -1)

    def test_single_element(self):
        self.assertIs(sum_even_odd([1]), 1)
        self.assertIs(sum_even_odd([2]), 2)

    def test_mixed_list(self):
        self.assertIs(sum_even_odd([1, 2, 3, 4, 5]), 1 + 3)
        self.assertIs(sum_even_odd([2, 1, 0, 5, 4]), 2 + 0)

    def test_all_even(self):
        self.assertIs(sum_even_odd([2, 4, 6]), 2 + 6)

    def test_all_odd(self):
        self.assertIs(sum_even_odd([1, 3, 5]), 1 + 3)

    def test_first_even_last_odd(self):
        self.assertIs(sum_even_odd([2, 1, 3]), 2 + 3)

    def test_first_odd_last_even(self):
        self.assertIs(sum_even_odd([1, 2, 0]), 1 + 0)

    def test_first_and_last_even(self):
        self.assertIs(sum_even_odd([2, 2]), 2 + 2)

    def test_first_and_last_odd(self):
        self.assertIs(sum_even_odd([1, 1]), 1 + 1)
