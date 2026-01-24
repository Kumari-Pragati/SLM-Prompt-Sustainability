import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(does_Contain_B(1, 1, 1))
        self.assertFalse(does_Contain_B(2, 3, 4))
        self.assertTrue(does_Contain_B(5, 5, 5))

    def test_edge_and_boundary_cases(self):
        self.assertTrue(does_Contain_B(0, 0, 1))
        self.assertFalse(does_Contain_B(1, 2, 0))
        self.assertTrue(does_Contain_B(3, 3, 3))

    def test_corner_cases(self):
        self.assertTrue(does_Contain_B(1, 1, 0))
        self.assertFalse(does_Contain_B(2, 3, 0))
