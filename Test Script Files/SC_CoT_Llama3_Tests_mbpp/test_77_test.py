import unittest
from mbpp_77_code import is_Diff

class TestIsDiff(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertTrue(is_Diff(0))
        self.assertTrue(is_Diff(11))
        self.assertTrue(is_Diff(22))
        self.assertTrue(is_Diff(33))

    def test_edge_cases(self):
        self.assertFalse(is_Diff(1))
        self.assertFalse(is_Diff(2))
        self.assertFalse(is_Diff(3))
        self.assertFalse(is_Diff(4))

    def test_boundary_cases(self):
        self.assertTrue(is_Diff(10))
        self.assertTrue(is_Diff(20))
        self.assertTrue(is_Diff(30))
        self.assertTrue(is_Diff(40))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_Diff('a')
        with self.assertRaises(TypeError):
            is_Diff(None)
        with self.assertRaises(TypeError):
            is_Diff([1, 2, 3])
