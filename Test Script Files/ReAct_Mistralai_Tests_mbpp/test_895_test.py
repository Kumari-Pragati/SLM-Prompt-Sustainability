import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum_subseq([]), 0)

    def test_single_element_list(self):
        for num in range(-10, 11):
            self.assertEqual(max_sum_subseq([num]), num)

    def test_positive_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(max_sum_subseq(numbers), sum(numbers))

    def test_negative_numbers(self):
        numbers = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
        self.assertEqual(max_sum_subseq(numbers), max(numbers))

    def test_mixed_numbers(self):
        numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9]
        self.assertEqual(max_sum_subseq(numbers), max(numbers, sum(numbers[::2])))

    def test_long_list(self):
        numbers = [random.randint(-100, 100) for _ in range(1000)]
        self.assertEqual(max_sum_subseq(numbers), max(numbers, key=numbers.index))
