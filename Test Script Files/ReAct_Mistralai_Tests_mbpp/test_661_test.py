import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum_of_three_consecutive([], 0), 0)

    def test_single_element_list(self):
        for num in range(-10, 10):
            self.assertEqual(max_sum_of_three_consecutive([num], 1), num)

    def test_two_elements_list(self):
        for a in range(-10, 10):
            for b in range(-10, 10):
                self.assertEqual(max_sum_of_three_consecutive([a, b], 2), max(a, b) + min(a, b))

    def test_three_elements_list(self):
        for a in range(-10, 10):
            for b in range(-10, 10):
                for c in range(-10, 10):
                    self.assertEqual(max_sum_of_three_consecutive([a, b, c], 3), max(a + max(b, c), b + max(a, c), c + a))

    def test_negative_n(self):
        self.assertRaises(ValueError, max_sum_of_three_consecutive, [1, 2, 3], -1)

    def test_negative_numbers(self):
        for n in range(1, 10):
            self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3, 1, 2, 3], n), max(max(-1 + max(-2, -3), -2 + max(-1, -3), -3 + -1), 1 + -1 + max(-3, -2), 2 + 1 + -1, 3 + 1 + -1 + -3))
