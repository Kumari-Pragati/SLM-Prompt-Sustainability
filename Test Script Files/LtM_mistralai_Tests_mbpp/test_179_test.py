import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(is_num_keith(12345))
        self.assertTrue(is_num_keith(54321))
        self.assertTrue(is_num_keith(11111))
        self.assertTrue(is_num_keith(98765))

    def test_edge_cases(self):
        self.assertFalse(is_num_keith(0))
        self.assertFalse(is_num_keith(10**6))
        self.assertFalse(is_num_keith(10**7))
        self.assertFalse(is_num_keith(-12345))

    def test_complex_cases(self):
        self.assertTrue(is_num_keith(123000))
        self.assertTrue(is_num_keith(543001))
        self.assertFalse(is_num_keith(12300))
        self.assertFalse(is_num_keith(54300))
