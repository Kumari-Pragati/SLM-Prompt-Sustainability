import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_of_alternates([]), (0, 0))

    def test_single_element(self):
        self.assertEqual(sum_of_alternates([1]), (1, 0))

    def test_even_length_list(self):
        self.assertEqual(sum_of_alternates([1, 2, 3, 4]), ((1 + 3), (2 + 4)))

    def test_odd_length_list(self):
        self.assertEqual(sum_of_alternates([1, 2, 3, 4, 5]), ((1 + 3 + 5), (2 + 4)))
