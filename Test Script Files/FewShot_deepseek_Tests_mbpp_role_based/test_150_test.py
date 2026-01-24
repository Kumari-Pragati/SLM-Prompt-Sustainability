import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(does_Contain_B(1, 2, 1))

    def test_edge_case(self):
        self.assertTrue(does_Contain_B(0, 0, 1))

    def test_boundary_case(self):
        self.assertFalse(does_Contain_B(1, 2, 0))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            does_Contain_B('a', 2, 1)
