import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_num_keith(9527))
        self.assertTrue(is_num_keith(527))
        self.assertTrue(is_num_keith(7))

    def test_edge_cases(self):
        self.assertFalse(is_num_keith(0))
        self.assertFalse(is_num_keith(10 ** 10))
        self.assertFalse(is_num_keith(-1))

    def test_boundary_cases(self):
        self.assertTrue(is_num_keith(9))
        self.assertTrue(is_num_keith(99))
        self.assertTrue(is_num_keith(999))
        self.assertTrue(is_num_keith(9999))
        self.assertTrue(is_num_keith(99999))
        self.assertTrue(is_num_keith(999999))
        self.assertTrue(is_num_keith(9999999))
