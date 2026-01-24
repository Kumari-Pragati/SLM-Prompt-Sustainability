import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):
    def test_sum_within_range(self):
        self.assertEqual(sum_nums(5, 3, 10, 20), 20)
        self.assertEqual(sum_nums(4, 2, 3, 6), None)

    def test_sum_outside_range(self):
        self.assertEqual(sum_nums(5, 3, 1, 2), 8)
        self.assertEqual(sum_nums(4, 2, 5, 6), None)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, sum_nums, 'a', 3, 4, 5)
        self.assertRaises(TypeError, sum_nums, 1, 'b', 4, 5)
        self.assertRaises(TypeError, sum_nums, 1, 3, 'a', 5)
        self.assertRaises(TypeError, sum_nums, 1, 3, 4, 'a')
