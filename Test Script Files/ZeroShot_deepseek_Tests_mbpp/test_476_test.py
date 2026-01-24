import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):

    def test_big_sum(self):
        self.assertEqual(big_sum([1, 2, 3, 4, 5]), 6)
        self.assertEqual(big_sum([10, 20, 30, 40, 50]), 60)
        self.assertEqual(big_sum([-1, -2, -3, -4, -5]), -4)
        self.assertEqual(big_sum([0, 0, 0, 0, 0]), 0)
        self.assertEqual(big_sum([1000000, 2000000, 3000000, 4000000, 5000000]), 10000000)
