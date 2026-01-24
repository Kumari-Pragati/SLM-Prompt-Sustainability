import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_num_keith(14))
        self.assertTrue(is_num_keith(407))
        self.assertTrue(is_num_keith(197))

    def test_edge_cases(self):
        self.assertTrue(is_num_keith(1))
        self.assertTrue(is_num_keith(10))
        self.assertTrue(is_num_keith(11))
        self.assertTrue(is_num_keith(12))
        self.assertTrue(is_num_keith(13))
        self.assertTrue(is_num_keith(14))
        self.assertTrue(is_num_keith(15))
        self.assertTrue(is_num_keith(16))
        self.assertTrue(is_num_keith(17))
        self.assertTrue(is_num_keith(18))
        self.assertTrue(is_num_keith(19))
        self.assertTrue(is_num_keith(20))

    def test_corner_cases(self):
        self.assertFalse(is_num_keith(1000))
        self.assertFalse(is_num_keith(10000))
        self.assertFalse(is_num_keith(100000))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_num_keith('14')
        with self.assertRaises(ValueError):
            is_num_keith(-14)
        with self.assertRaises(TypeError):
            is_num_keith(None)
