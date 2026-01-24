import unittest
from mbpp_970_code import min_of_two

class TestMinOfTwo(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(min_of_two(2, 4), 2)

    def test_edge_case_equal(self):
        self.assertEqual(min_of_two(2, 2), 2)

    def test_edge_case_negative(self):
        self.assertEqual(min_of_two(-2, -4), -4)

    def test_edge_case_zero(self):
        self.assertEqual(min_of_two(0, 0), 0)

    def test_edge_case_negative_zero(self):
        self.assertEqual(min_of_two(-2, 0), -2)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            min_of_two("a", 4)
