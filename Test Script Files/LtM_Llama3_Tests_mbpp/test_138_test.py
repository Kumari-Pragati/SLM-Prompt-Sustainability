import unittest
from mbpp_138_code import is_Sum_Of_Powers_Of_Two

class TestIsSumOfPowersOfTwo(unittest.TestCase):
    def test_simple_true(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(4))

    def test_simple_false(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(3))

    def test_edge_zero(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(0))

    def test_edge_one(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(1))

    def test_edge_negative(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-1))

    def test_edge_negative_zero(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(0))

    def test_edge_max(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(2**31-1))

    def test_edge_max_negative(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-2**31))
