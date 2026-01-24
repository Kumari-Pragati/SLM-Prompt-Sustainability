import unittest
from mbpp_138_code import is_Sum_Of_Powers_Of_Two

class TestIsSumOfPowersOfTwo(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(4))

    def test_edge_case(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(1))

    def test_boundary_case(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(2))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_Sum_Of_Powers_Of_Two('a')
