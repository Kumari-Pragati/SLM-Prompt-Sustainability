import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(same_Length(123, 456))

    def test_boundary_condition(self):
        self.assertTrue(same_Length(0, 0))

    def test_edge_condition(self):
        self.assertFalse(same_Length(1, 10))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            same_Length("123", 456)
