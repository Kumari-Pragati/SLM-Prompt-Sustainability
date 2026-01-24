import unittest
from mbpp_68_code import is_Monotonic

class TestIsMonotonic(unittest.TestCase):
    def test_typical_increasing(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))

    def test_typical_decreasing(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))

    def test_typical_constant(self):
        self.assertTrue(is_Monotonic([1, 1, 1, 1, 1]))

    def test_edge_increasing(self):
        self.assertTrue(is_Monotonic([1, 1, 2, 3, 4]))

    def test_edge_decreasing(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1, 1]))

    def test_edge_constant(self):
        self.assertTrue(is_Monotonic([1, 1, 1, 1, 1, 1]))

    def test_edge_mixed(self):
        self.assertFalse(is_Monotonic([1, 2, 3, 2, 1]))

    def test_edge_mixed2(self):
        self.assertFalse(is_Monotonic([5, 4, 3, 2, 1, 5]))

    def test_edge_mixed3(self):
        self.assertFalse(is_Monotonic([1, 1, 2, 3, 4, 3]))

    def test_edge_mixed4(self):
        self.assertFalse(is_Monotonic([5, 5, 4, 3, 2, 1]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_Monotonic('abc')
