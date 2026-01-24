import unittest
from mbpp_138_code import is_Sum_Of_Powers_Of_Two

class TestIsSumOfPowersOfTwo(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(0))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(2))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(4))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(6))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(8))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(10))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(14))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(18))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(20))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(26))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(30))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(34))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(38))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(42))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(46))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(50))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(54))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(58))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(62))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(66))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(70))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(74))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(78))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(82))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(86))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(90))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(94))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(98))

    def test_edge_and_boundary_cases(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(1))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(-1))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(2 ** 32))
