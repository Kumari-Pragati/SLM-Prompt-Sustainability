import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(amicable_numbers_sum(281_230), 220 + 284)
        self.assertEqual(amicable_numbers_sum(123), 220 + 284)
        self.assertEqual(amicable_numbers_sum(1000), 9890 + 9188)

    def test_edge_cases(self):
        self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")
        self.assertEqual(amicable_numbers_sum(1), "Input must be bigger than 0!")
        self.assertEqual(amicable_numbers_sum(-1), "Input must be bigger than 0!")
        self.assertEqual(amicable_numbers_sum(1.5), "Input is not an integer!")
        self.assertEqual(amicable_numbers_sum(2), 0)

    def test_invalid_input(self):
        self.assertEqual(amicable_numbers_sum("not_an_integer"), "Input is not an integer!")
        self.assertEqual(amicable_numbers_sum([1, 2, 3]), "Input is not an integer!")
        self.assertEqual(amicable_numbers_sum(None), "Input is not an integer!")
