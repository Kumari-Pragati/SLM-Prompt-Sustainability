import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):
    def test_normal_case(self):
        self.assertTrue(does_Contain_B(1, 2, 1))
        self.assertTrue(does_Contain_B(2, 2, 1))
        self.assertTrue(does_Contain_B(10, 15, 5))

    def test_edge_cases(self):
        self.assertFalse(does_Contain_B(0, 1, 1))
        self.assertFalse(does_Contain_B(1, 0, 1))
        self.assertFalse(does_Contain_B(-1, 1, 1))
        self.assertFalse(does_Contain_B(1, -1, 1))
        self.assertFalse(does_Contain_B(1, 1, 0))
        self.assertFalse(does_Contain_B(1, 1, -1))
        self.assertFalse(does_Contain_B(1, 1, 2))

    def test_boundary_cases(self):
        self.assertTrue(does_Contain_B(1, 2, 2))
        self.assertTrue(does_Contain_B(2, 3, 1))
        self.assertTrue(does_Contain_B(10, 15, 2))
        self.assertTrue(does_Contain_B(10, 15, 10))
        self.assertFalse(does_Contain_B(1, 2, 3))
        self.assertFalse(does_Contain_B(2, 3, 2))
        self.assertFalse(does_Contain_B(10, 15, 11))
        self.assertFalse(does_Contain_B(10, 15, 16))
