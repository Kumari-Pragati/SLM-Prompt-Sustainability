import unittest
from mbpp_138_code import is_Sum_Of_Powers_Of_Two

class TestIsSumOfPowersOfTwo(unittest.TestCase):

    def test_zero(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(0))

    def test_one(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(1))

    def test_powers_of_two(self):
        for i in range(1, 10):
            self.assertTrue(is_Sum_Of_Powers_Of_Two(2 ** i))

    def test_sum_of_powers(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(3))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(4))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(5))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(6))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(7))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(8))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(9))

    def test_large_numbers(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(16))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(32))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(64))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(65))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(129))
