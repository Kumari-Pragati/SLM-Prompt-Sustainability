import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):

    def test_sum_num(self):
        self.assertEqual(sum_num([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(sum_num([1, 2, 3, 4, 5, 6]), 3.5)
        self.assertAlmostEqual(sum_num([1, 1, 1, 1, 1]), 1.0)
        self.assertAlmostEqual(sum_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5.5)
        self.assertAlmostEqual(sum_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 5.833333333333333)

    def test_sum_num_empty_list(self):
        self.assertRaises(ZeroDivisionError, sum_num, [])

    def test_sum_num_single_element(self):
        self.assertAlmostEqual(sum_num([1]), 1.0)

    def test_sum_num_zero(self):
        self.assertAlmostEqual(sum_num([0]), 0.0)
