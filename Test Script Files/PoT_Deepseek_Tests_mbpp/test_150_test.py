import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(does_Contain_B(1, 2, 1))
        self.assertTrue(does_Contain_B(10, 20, 10))
        self.assertFalse(does_Contain_B(10, 20, 15))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(does_Contain_B(0, 0, 1))
        self.assertFalse(does_Contain_B(0, 0, 0))
        self.assertTrue(does_Contain_B(1, 2, 1))
        self.assertFalse(does_Contain_B(1, 2, 0))

    def test_corner_cases(self):
        self.assertTrue(does_Contain_B(1, 2, 1))
        self.assertFalse(does_Contain_B(1, 2, 2))
        self.assertFalse(does_Contain_B(1, 1, 1))
