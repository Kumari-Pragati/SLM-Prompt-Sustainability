import unittest
from mbpp_77_code import is_Diff

class TestIsDiff(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_Diff(11))

    def test_boundary_conditions(self):
        self.assertTrue(is_Diff(0))
        self.assertFalse(is_Diff(1))

    def test_edge_conditions(self):
        self.assertTrue(is_Diff(22))
        self.assertFalse(is_Diff(33))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_Diff('11')
