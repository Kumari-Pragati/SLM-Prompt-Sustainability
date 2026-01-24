import unittest
from mbpp_633_code import pow
from six.moves import range

class TestPairORSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(pair_OR_Sum([], 0), 0)

    def test_single_element(self):
        for num in range(10):
            self.assertEqual(pair_OR_Sum([num], 1), num)

    def test_pair_case(self):
        test_cases = [
            ([1, 2, 3, 4], 4),
            ([5, 6, 7, 8], 28),
            ([9, 10, 11, 12], 144),
            ([13, 14, 15, 16], 360),
            ([17, 18, 19, 20], 720),
        ]
        for arr, expected in test_cases:
            self.assertEqual(pair_OR_Sum(arr, len(arr)), expected)

    def test_odd_length(self):
        for num in range(10):
            self.assertEqual(pair_OR_Sum([1, 2, 3, 4, num], 5), sum([1, 2, 3, 4, num]))

    def test_invalid_input_empty_array(self):
        with self.assertRaises(IndexError):
            pair_OR_Sum([], -1)

    def test_invalid_input_negative_array(self):
        with self.assertRaises(ValueError):
            pair_OR_Sum([-1, -2, -3], 3)

    def test_invalid_input_non_integer_array(self):
        with self.assertRaises(TypeError):
            pair_OR_Sum([1.1, 2.2, 3.3], 3)

    def test_invalid_input_non_integer_n(self):
        with self.assertRaises(TypeError):
            pair_OR_Sum([1, 2, 3], 'a')
