import unittest
from mbpp_68_code import is_Monotonic

class TestIsMonotonic(unittest.TestCase):
    
    def test_typical_cases(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))
        self.assertTrue(is_Monotonic([1, 1, 1, 1, 1]))
        self.assertTrue(is_Monotonic([1, 2, 2, 3, 4]))

    def test_edge_cases(self):
        self.assertTrue(is_Monotonic([1]))
        self.assertTrue(is_Monotonic([]))

    def test_boundary_conditions(self):
        self.assertTrue(is_Monotonic([1, 2]))
        self.assertTrue(is_Monotonic([2, 1]))
        self.assertFalse(is_Monotonic([1, 2, 1]))
        self.assertFalse(is_Monotonic([2, 1, 2]))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_Monotonic(123)
        with self.assertRaises(TypeError):
            is_Monotonic('123')
        with self.assertRaises(TypeError):
            is_Monotonic([1, '2'])
        with self.assertRaises(TypeError):
            is_Monotonic([1, None])
