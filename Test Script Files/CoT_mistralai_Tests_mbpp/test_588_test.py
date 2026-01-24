import unittest
from mbpp_588_code import big_diff

class TestBigDiff(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(big_diff([1, 2, 3, 4, 5]), 4)
        self.assertEqual(big_diff([10, 20, 30, 40, 50]), 40)

    def test_negative_numbers(self):
        self.assertEqual(big_diff([-1, -2, -3, -4, -5]), 5)
        self.assertEqual(big_diff([-10, -20, -30, -40, -50]), 50)

    def test_mixed_numbers(self):
        self.assertEqual(big_diff([1, -2, 3, -4, 5]), 5)
        self.assertEqual(big_diff([-1, 2, -3, 4, -5]), 5)

    def test_single_number(self):
        self.assertEqual(big_diff([1]), 0)
        self.assertEqual(big_diff([-1]), 0)

    def test_empty_list(self):
        self.assertEqual(big_diff([]), None)

    def test_invalid_input(self):
        self.assertRaises(TypeError, big_diff, "string")
        self.assertRaises(TypeError, big_diff, [1, 2, 3, "four"])
