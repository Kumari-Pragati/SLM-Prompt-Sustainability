import unittest
from mbpp_349_code import check

class TestCheckFunction(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertEqual(check("0"), "Yes")
        self.assertEqual(check("1"), "Yes")
        self.assertEqual(check("01"), "Yes")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(check(""), "No")
        self.assertEqual(check("0"), "Yes")
        self.assertEqual(check("1"), "Yes")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check(123)

    def test_invalid_inputs_type(self):
        with self.assertRaises(TypeError):
            check("abc")
