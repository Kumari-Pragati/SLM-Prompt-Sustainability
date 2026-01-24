import unittest
from mbpp_138_code import is_Sum_Of_Powers_Of_Two

class TestIsSumOfPowersOfTwo(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(2))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(4))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(6))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(8))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(0))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(1))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(2 ** 31 - 1))  # 2^31 - 1 is the maximum positive integer that can be represented in a 32-bit two's complement integer
        self.assertTrue(is_Sum_Of_Powers_Of_Two(2 ** 64))  # 2^64 is the maximum positive integer that can be represented in a 64-bit two's complement integer

    def test_special_cases(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(2 ** 1000))  # large power of 2
        self.assertTrue(is_Sum_Of_Powers_Of_Two(2 ** 1000 - 1))  # one less than a large power of 2
