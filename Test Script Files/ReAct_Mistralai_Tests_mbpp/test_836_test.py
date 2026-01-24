import unittest
from mbpp_836_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_single_element_array(self):
        for num in range(-100, 101):
            self.assertEqual(max_sub_array_sum([num], 1), 1)

    def test_positive_numbers(self):
        for i in range(10):
            arr = [random.randint(1, 100) for _ in range(random.randint(1, 10))]
            self.assertGreaterEqual(max_sub_array_sum(arr, len(arr)), sum(arr))

    def test_negative_numbers(self):
        for i in range(10):
            arr = [random.randint(-100, -1) for _ in range(random.randint(1, 10))]
            self.assertGreaterEqual(max_sub_array_sum(arr, len(arr)), 0)

    def test_mixed_numbers(self):
        for i in range(10):
            arr = [random.randint(-100, 100) for _ in range(random.randint(1, 20))]
            self.assertGreaterEqual(max_sub_array_sum(arr, len(arr)), sum(arr) if sum(arr) >= 0 else 0)

    def test_zero_sum_array(self):
        self.assertEqual(max_sub_array_sum([0] * 10, 10), 0)
        self.assertEqual(max_sub_array_sum([0, 0, 1, 0, -1, 0, 0, 1, 0, -1], 10), 3)

    def test_negative_sum_array(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 0)
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 5), 1)

    def test_large_array(self):
        arr = [random.randint(-100, 100) for _ in range(10000)]
        self.assertGreaterEqual(max_sub_array_sum(arr, len(arr)), sum(arr) if sum(arr) >= 0 else 0)
