import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):

    def test_positive_cases(self):
        self.assertTrue(is_num_keith(14))
        self.assertTrue(is_num_keith(49))
        self.assertTrue(is_num_keith(89))
        self.assertTrue(is_num_keith(197))
        self.assertTrue(is_num_keith(4474))

    def test_negative_cases(self):
        self.assertFalse(is_num_keith(15))
        self.assertFalse(is_num_keith(50))
        self.assertFalse(is_num_keith(90))
        self.assertFalse(is_num_keith(198))
        self.assertFalse(is_num_keith(4475))

    def test_edge_cases(self):
        self.assertFalse(is_num_keith(0))
        self.assertFalse(is_num_keith(1))
        self.assertTrue(is_num_keith(10))
        self.assertTrue(is_num_keith(181))
        self.assertFalse(is_num_keith(1000))
