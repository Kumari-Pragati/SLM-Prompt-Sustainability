import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):

    def test_normal(self):
        self.assertTrue(is_undulating([1, 2, 2, 1]))
        self.assertTrue(is_undulating([3, 4, 4, 3]))
        self.assertTrue(is_undulating([0, 1, 0, 1]))

    def test_edge_cases(self):
        self.assertFalse(is_undulating([1, 2, 2]))
        self.assertFalse(is_undulating([2, 2, 1]))
        self.assertFalse(is_undulating([1, 1, 2]))
        self.assertFalse(is_undulating([1, 2, 2, 1, 2]))
        self.assertFalse(is_undulating([2, 2, 1, 2]))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_undulating, 1.5)
        self.assertRaises(TypeError, is_undulating, "string")
        self.assertRaises(TypeError, is_undulating, [1, 2, 2, 1, "invalid"])
