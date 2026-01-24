import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(add_pairwise([]))

    def test_single_element(self):
        self.assertIsNone(add_pairwise([1]))

    def test_simple_list(self):
        self.assertEqual(add_pairwise([1, 2, 3, 4]), (3, 5, 6))

    def test_negative_numbers(self):
        self.assertEqual(add_pairwise([-1, -2, 3, 4]), (2, -1, 7))

    def test_mixed_numbers(self):
        self.assertEqual(add_pairwise([1, -2, 3, 4]), (3, -1, 7))
