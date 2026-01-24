import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_num_keith(14))
        self.assertTrue(is_num_keith(19))
        self.assertTrue(is_num_keith(407))
        self.assertTrue(is_num_keith(171))
        self.assertTrue(is_num_keith(121))

    def test_edge_cases(self):
        self.assertFalse(is_num_keith(0))
        self.assertFalse(is_num_keith(1))
        self.assertFalse(is_num_keith(10))
        self.assertFalse(is_num_keith(11))
        self.assertFalse(is_num_keith(100))

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            is_num_keith("14")
        with self.assertRaises(TypeError):
            is_num_keith(14.5)
        with self.assertRaises(TypeError):
            is_num_keith([])
        with self.assertRaises(TypeError):
            is_num_keith({})
