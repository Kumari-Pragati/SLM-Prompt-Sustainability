import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(min_val([3, 1, 2]), 1)

    def test_edge_condition(self):
        self.assertEqual(min_val([1]), 1)

    def test_boundary_condition(self):
        self.assertEqual(min_val([1, 2, 3, 4, 5]), 1)

    def test_with_non_integer_values(self):
        self.assertEqual(min_val([3, 1.5, 2]), 1.5)

    def test_with_negative_numbers(self):
        self.assertEqual(min_val([3, -1, 2]), -1)

    def test_with_mixed_types(self):
        self.assertEqual(min_val([3, 'a', 2]), 2)

    def test_with_empty_list(self):
        with self.assertRaises(ValueError):
            min_val([])

    def test_with_none_in_list(self):
        with self.assertRaises(TypeError):
            min_val([3, None, 2])
