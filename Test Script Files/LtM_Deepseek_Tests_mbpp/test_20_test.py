import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertTrue(is_woodall(1))
        self.assertTrue(is_woodall(3))
        self.assertTrue(is_woodall(15))
        self.assertTrue(is_woodall(127))

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertFalse(is_woodall(0))
        self.assertFalse(is_woodall(-1))
        self.assertFalse(is_woodall(2))
        self.assertFalse(is_woodall(4))

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertFalse(is_woodall(8))
        self.assertFalse(is_woodall(10))
        self.assertFalse(is_woodall(16))
        self.assertFalse(is_woodall(1023))
        self.assertFalse(is_woodall(1024))
