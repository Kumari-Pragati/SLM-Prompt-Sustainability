import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_num_keith(14))
        self.assertTrue(is_num_keith(407))
        self.assertTrue(is_num_keith(197))
        self.assertTrue(is_num_keith(44040))

    def test_edge_cases(self):
        self.assertFalse(is_num_keith(0))
        self.assertFalse(is_num_keith(1))
        self.assertFalse(is_num_keith(10))
        self.assertFalse(is_num_keith(100))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_num_keith('14')
        with self.assertRaises(TypeError):
            is_num_keith(14.5)
        with self.assertRaises(TypeError):
            is_num_keith(None)
        with self.assertRaises(TypeError):
            is_num_keith([14])
