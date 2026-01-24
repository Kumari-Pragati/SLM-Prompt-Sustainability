import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):
    def test_simple_cases(self):
        self.assertTrue(does_Contain_B(1, 2, 1))
        self.assertFalse(does_Contain_B(1, 2, 2))

    def test_edge_conditions(self):
        self.assertTrue(does_Contain_B(0, 0, 1))
        self.assertFalse(does_Contain_B(0, 0, 0))
        self.assertTrue(does_Contain_B(-1, 1, 2))
        self.assertFalse(does_Contain_B(-1, 1, 1))

    def test_complex_cases(self):
        self.assertTrue(does_Contain_B(1, 10, 3))
        self.assertFalse(does_Contain_B(1, 10, 4))
        self.assertTrue(does_Contain_B(-10, 10, 2))
        self.assertFalse(does_Contain_B(-10, 10, 1))
