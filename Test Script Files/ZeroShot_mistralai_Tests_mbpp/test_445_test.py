import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):

    def test_empty_lists(self):
        self.assertIsInstance(index_multiplication([], []), tuple)
        self.assertListEqual(index_multiplication([], []), [])

    def test_single_element_lists(self):
        self.assertIsInstance(index_multiplication([1], [2]), tuple)
        self.assertListEqual(index_multiplication([1], [2]), [2])
        self.assertIsInstance(index_multiplication([2], [1]), tuple)
        self.assertListEqual(index_multiplication([2], [1]), [2])

    def test_lists_with_different_lengths(self):
        self.assertRaises(ValueError, index_multiplication, [1, 2], [3])
        self.assertRaises(ValueError, index_multiplication, [1, 2, 3], [3, 4])

    def test_simple_lists(self):
        self.assertIsInstance(index_multiplication([1, 2], [3, 4]), tuple)
        self.assertListEqual(index_multiplication([1, 2], [3, 4]), [3, 4, 2, 8])
        self.assertIsInstance(index_multiplication([3, 4], [1, 2]), tuple)
        self.assertListEqual(index_multiplication([3, 4], [1, 2]), [3, 4, 6, 8])

    def test_lists_with_negative_numbers(self):
        self.assertIsInstance(index_multiplication([-1, 2], [3, -4]), tuple)
        self.assertListEqual(index_multiplication([-1, 2], [3, -4]), [-3, 6, -8])
        self.assertIsInstance(index_multiplication([3, -4], [-1, 2]), tuple)
        self.assertListEqual(index_multiplication([3, -4], [-1, 2]), [-3, -4, 6, 8])
