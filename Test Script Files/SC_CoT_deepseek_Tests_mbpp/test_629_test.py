import unittest
from mbpp_629_code import Split

class TestSplit(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(Split([1, 2, 3, 4, 5]), [2, 4])

    def test_empty_list(self):
        self.assertEqual(Split([]), [])

    def test_all_odd_numbers(self):
        self.assertEqual(Split([1, 3, 5, 7]), [])

    def test_all_even_numbers(self):
        self.assertEqual(Split([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_mixed_numbers(self):
        self.assertEqual(Split([1, 2, 3, 4]), [2, 4])

    def test_large_numbers(self):
        self.assertEqual(Split([1000000002, 1000000004]), [1000000002, 1000000004])

    def test_negative_numbers(self):
        self.assertEqual(Split([-1, -2, -3, -4]), [-2, -4])

    def test_zero(self):
        self.assertEqual(Split([0]), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Split("not a list")
