import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(func([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), [1, 2, 3])

    def test_typical_input(self):
        self.assertEqual(func([[1, 2, 2], [3, 3, 3], [4, 4, 4]], 2), [2, 3])

    def test_edge_condition_k_equals_zero(self):
        self.assertEqual(func([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0), [])

    def test_edge_condition_k_greater_than_total_elements(self):
        self.assertEqual(func([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_boundary_condition_k_equals_one(self):
        self.assertEqual(func([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), [1])

    def test_complex_input(self):
        self.assertEqual(func([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 2), [1, 2])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            func("not a list", 3)
