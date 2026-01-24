import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):

    def test_sum_of_alternates(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5)), ((9), (6)))
        self.assertEqual(sum_of_alternates((10, 20, 30, 40, 50)), ((90), (60)))
        self.assertEqual(sum_of_alternates((100, 200, 300, 400, 500)), ((900), (600)))
        self.assertEqual(sum_of_alternates(()), ((), ()))
        self.assertEqual(sum_of_alternates((1,)), ((1), ()))
        self.assertEqual(sum_of_alternates((1, 2)), ((2), (1)))
