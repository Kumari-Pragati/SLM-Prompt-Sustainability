import unittest
from mbpp_53_code import check_Equality

class TestCheckEquality(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(check_Equality("hello"), "Equal")
        self.assertEqual(check_Equality("world"), "Equal")
        self.assertEqual(check_Equality("abc"), "Equal")

    def test_edge_cases(self):
        self.assertEqual(check_Equality("a"), "Equal")
        self.assertEqual(check_Equality("b"), "Equal")
        self.assertEqual(check_Equality("c"), "Equal")

    def test_boundary_cases(self):
        self.assertEqual(check_Equality(""), "Not Equal")
        self.assertEqual(check_Equality("a"), "Equal")
        self.assertEqual(check_Equality("abc"), "Equal")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_Equality(123)
        with self.assertRaises(TypeError):
            check_Equality([1, 2, 3])
