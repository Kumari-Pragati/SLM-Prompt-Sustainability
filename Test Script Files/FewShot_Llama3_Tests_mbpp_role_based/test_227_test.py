import unittest
from mbpp_227_code import min_of_three

class TestMinOfThree(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)

    def test_edge_case_equal(self):
        self.assertEqual(min_of_three(1, 1, 1), 1)

    def test_edge_case_negative(self):
        self.assertEqual(min_of_three(-1, -2, -3), -3)

    def test_edge_case_positive(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)

    def test_edge_case_zero(self):
        self.assertEqual(min_of_three(0, 0, 0), 0)

    def test_edge_case_negative_and_positive(self):
        self.assertEqual(min_of_three(-1, 2, 3), -1)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            min_of_three('a', 'b', 'c')
