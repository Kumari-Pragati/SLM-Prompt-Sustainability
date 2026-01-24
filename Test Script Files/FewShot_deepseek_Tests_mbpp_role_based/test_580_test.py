import unittest
from mbpp_580_code import extract_even

class TestExtractEven(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(extract_even((1, 2, 3, 4, 5, 6)), (2, 4, 6))

    def test_typical_use_case_with_nested_tuples(self):
        self.assertEqual(extract_even(((1, 2), (3, 4), (5, 6))), ((2,), (4,), (6,)))

    def test_boundary_conditions(self):
        self.assertEqual(extract_even(()), ())
        self.assertEqual(extract_even((2,)), (2,))

    def test_edge_conditions(self):
        self.assertEqual(extract_even((1, 3, 5, 7)), ())

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            extract_even(123)
        with self.assertRaises(TypeError):
            extract_even('123')
        with self.assertRaises(TypeError):
            extract_even([1, 2, 3])
