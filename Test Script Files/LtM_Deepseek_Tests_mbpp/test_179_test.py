import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertTrue(is_num_keith(14))
        self.assertTrue(is_num_keith(407))
        self.assertFalse(is_num_keith(198))
        self.assertFalse(is_num_keith(1))

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertFalse(is_num_keith(0))
        self.assertFalse(is_num_keith(8))
        self.assertFalse(is_num_keith(10))
        self.assertFalse(is_num_keith(18))
        self.assertFalse(is_num_keith(19))
        self.assertFalse(is_num_keith(20))
        self.assertFalse(is_num_keith(28))
        self.assertFalse(is_num_keith(30))
        self.assertFalse(is_num_keith(39))
        self.assertFalse(is_num_keith(40))

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertTrue(is_num_keith(171))
        self.assertTrue(is_num_keith(4104))
        self.assertFalse(is_num_keith(10000))
        self.assertFalse(is_num_keith(100000))
