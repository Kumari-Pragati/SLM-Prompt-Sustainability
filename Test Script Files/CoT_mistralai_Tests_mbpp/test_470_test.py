import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(add_pairwise([]))

    def test_single_element(self):
        self.assertIsInstance(add_pairwise([1]), tuple)
        self.assertEqual(add_pairwise([1]), (None,))

    def test_normal_case(self):
        self.assertIsInstance(add_pairwise([1, 2, 3, 4]), tuple)
        self.assertEqual(add_pairwise([1, 2, 3, 4]), (3, 5, 6))

    def test_negative_numbers(self):
        self.assertIsInstance(add_pairwise([-1, -2, 3, 4]), tuple)
        self.assertEqual(add_pairwise([-1, -2, 3, 4]), (2, -1, 7))

    def test_mixed_types(self):
        self.assertRaises(TypeError, add_pairwise, [1, 'a', 3])

    def test_invalid_input_length(self):
        self.assertRaises(IndexError, add_pairwise, [1, 2, 3])
