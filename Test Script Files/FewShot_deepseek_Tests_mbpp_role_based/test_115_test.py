import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(empty_dit([]))

    def test_edge_condition(self):
        self.assertTrue(empty_dit([None]))

    def test_boundary_condition(self):
        self.assertFalse(empty_dit([{}]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            empty_dit(123)
