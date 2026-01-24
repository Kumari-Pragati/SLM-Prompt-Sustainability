import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_undulating([1, 2, 2, 1]))
        self.assertTrue(is_undulating([1, 2, 3, 2, 1]))
        self.assertTrue(is_undulating([1, 2, 2, 3, 2, 1]))

    def test_edge_cases(self):
        self.assertFalse(is_undulating([1, 1]))
        self.assertFalse(is_undulating([1, 2, 2]))
        self.assertFalse(is_undulating([2, 1]))
        self.assertFalse(is_undulating([1, 2]))
        self.assertFalse(is_undulating([2, 1, 2]))

    def test_boundary_cases(self):
        self.assertFalse(is_undulating([]))
        self.assertFalse(is_undulating([1]))
        self.assertFalse(is_undulating([1, 2, 2, 1, 2]))
        self.assertFalse(is_undulating([1, 2, 2, 1, 2, 3]))
