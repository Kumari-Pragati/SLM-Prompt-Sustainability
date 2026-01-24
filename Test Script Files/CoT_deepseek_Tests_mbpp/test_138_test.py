import unittest
from mbpp_138_code import is_Sum_Of_Powers_Of_Two

class TestIsSumOfPowersOfTwo(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(0))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(2))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(4))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(8))
        self.assertTrue(is_Sum_Of_Powers_Of_Two(16))

    def test_edge_cases(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(1))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(3))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(5))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(7))
        self.assertFalse(is_Sum_Of_Powers_Of_Two(9))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_Sum_Of_Powers_Of_Two('a')
        with self.assertRaises(TypeError):
            is_Sum_Of_Powers_Of_Two(None)
        with self.assertRaises(TypeError):
            is_Sum_Of_Powers_Of_Two([])
