import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(max_difference([1, 2, 3, 4, 5]), 4)
        self.assertEqual(max_difference([10, 20, 30, 40, 50]), 40)

    def test_negative_numbers(self):
        self.assertEqual(max_difference([-1, -2, -3, -4, -5]), 4)
        self.assertEqual(max_difference([-10, -20, -30, -40, -50]), 40)

    def test_mixed_numbers(self):
        self.assertEqual(max_difference([1, -2, 3, -4, 5]), 5)
        self.assertEqual(max_difference([-1, 2, -3, 4, -5]), 5)

    def test_empty_list(self):
        self.assertEqual(max_difference([]), 0)

    def test_single_element_list(self):
        self.assertEqual(max_difference([1]), 0)
        self.assertEqual(max_difference([-1]), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, max_difference, [1, 'a', 3])
        self.assertRaises(TypeError, max_difference, ['1', 2, 3])
