import unittest
from mbpp_138_code import is_Sum_Of_Powers_Of_Two

class TestIsSumOfPowersOfTwo(unittest.TestCase):

    def test_simple_even_numbers(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(2))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(4))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(6))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(8))

    def test_edge_cases(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(0))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(1))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(2 ** 31 - 1))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(2 ** 63 - 1))

    def test_complex_cases(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(2 ** 30 + 2 ** 29))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(2 ** 62 + 2 ** 61))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(3))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(5))
