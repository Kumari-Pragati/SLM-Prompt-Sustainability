import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):
    def test_typical_use_cases(self):
        self.assertTrue(is_num_keith(14))
        self.assertTrue(is_num_keith(44))
        self.assertTrue(is_num_keith(197))
        self.assertTrue(is_num_keith(407))
        self.assertTrue(is_num_keith(13117))

    def test_edge_conditions(self):
        self.assertFalse(is_num_keith(0))
        self.assertFalse(is_num_keith(1))
        self.assertFalse(is_num_keith(2))
        self.assertFalse(is_num_keith(3))
        self.assertFalse(is_num_keith(4))

    def test_boundary_conditions(self):
        self.assertFalse(is_num_keith(10))
        self.assertFalse(is_num_keith(18))
        self.assertFalse(is_num_keith(20))
        self.assertFalse(is_num_keith(28))
        self.assertFalse(is_num_keith(30))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_num_keith('14')
        with self.assertRaises(TypeError):
            is_num_keith(-14)
        with self.assertRaises(TypeError):
            is_num_keith(14.5)
