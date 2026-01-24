import unittest
from mbpp_46_code import test_distinct

class TestDistinct(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(test_distinct([1, 2, 3, 4, 5]))

    def test_edge_condition(self):
        self.assertTrue(test_distinct([]))

    def test_boundary_condition(self):
        self.assertTrue(test_distinct([1]))
        self.assertFalse(test_distinct([1, 1]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            test_distinct(None)
        with self.assertRaises(TypeError):
            test_distinct('123')
        with self.assertRaises(TypeError):
            test_distinct(123)
