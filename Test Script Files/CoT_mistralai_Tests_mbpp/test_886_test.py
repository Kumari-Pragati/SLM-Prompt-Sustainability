import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):

    def test_empty_list(self):
        self.assertAlmostEqual(sum_num([]), 0)

    def test_single_element(self):
        self.assertAlmostEqual(sum_num([1]), 1)

    def test_multiple_elements(self):
        self.assertAlmostEqual(sum_num([1, 2, 3]), 2)

    def test_negative_numbers(self):
        self.assertAlmostEqual(sum_num([-1, -2, -3]), -0.5)

    def test_floats(self):
        self.assertAlmostEqual(sum_num([1.1, 2.2, 3.3]), 2.2)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            sum_num([1, 2, "three"])

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            sum_num([0])
