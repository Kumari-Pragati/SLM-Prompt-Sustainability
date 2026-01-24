import unittest
from mbpp_588_code import big_diff

class TestBigDiff(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(big_diff([1, 2, 3]), 2)
        self.assertEqual(big_diff([10, 3, 100]), 97)
        self.assertEqual(big_diff([5, 5, 5]), 0)

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            big_diff([])

    def test_single_element_input(self):
        with self.assertRaises(TypeError):
            big_diff([1])

    def test_negative_numbers(self):
        self.assertEqual(big_diff([-1, 0, 1]), 1)

    def test_positive_numbers(self):
        self.assertEqual(big_diff([1, 2, 3]), 2)

    def test_mixed_numbers(self):
        self.assertEqual(big_diff([-1, 0, 1]), 1)

    def test_large_numbers(self):
        self.assertEqual(big_diff([100, 200, 300]), 200)
