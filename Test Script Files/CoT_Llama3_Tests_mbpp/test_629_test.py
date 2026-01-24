import unittest
from mbpp_629_code import Split

class TestSplit(unittest.TestCase):
    def test_even_numbers(self):
        self.assertEqual(Split([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_odd_numbers(self):
        self.assertEqual(Split([1, 3, 5, 7]), [])

    def test_mixed_numbers(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_empty_list(self):
        self.assertEqual(Split([]), [])

    def test_single_element(self):
        self.assertEqual(Split([10]), [10])

    def test_negative_numbers(self):
        self.assertEqual(Split([-2, -4, -6, -8]), [-2, -4, -6, -8])

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            Split(['a', 'b', 'c'])
