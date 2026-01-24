import unittest
from mbpp_138_code import is_Sum_Of_Powers_Of_Two

class TestIsSumOfPowersOfTwo(unittest.TestCase):

    def test_simple_cases(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(0))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(2))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(4))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(8))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(16))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(1))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(32))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(64))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(128))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(256))

    def test_more_complex_cases(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(512))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(513))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(1024))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(1025))
