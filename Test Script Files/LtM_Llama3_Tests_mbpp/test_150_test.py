import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertTrue(does_Contain_B(1, 1, 1))
        self.assertTrue(does_Contain_B(2, 2, 2))
        self.assertFalse(does_Contain_B(1, 2, 1))

    def test_edge_cases(self):
        self.assertTrue(does_Contain_B(0, 0, 1))
        self.assertTrue(does_Contain_B(1, 1, 0))
        self.assertFalse(does_Contain_B(0, 1, 0))

    def test_complex_cases(self):
        self.assertTrue(does_Contain_B(1, 2, 3))
        self.assertTrue(does_Contain_B(2, 3, 4))
        self.assertFalse(does_Contain_B(1, 3, 2))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            does_Contain_B('a', 'b', 'c')
        with self.assertRaises(TypeError):
            does_Contain_B(1, 'b', 'c')
        with self.assertRaises(TypeError):
            does_Contain_B(1, 2, 'c')
