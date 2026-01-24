import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(substract_elements((5, 3, 2), (1, 2, 1)), (4, 1, 1))

    def test_edge_case_with_zero(self):
        self.assertEqual(substract_elements((0, 0, 0), (1, 2, 3)), (-1, -2, -3))

    def test_edge_case_with_negative_numbers(self):
        self.assertEqual(substract_elements((-5, -3, -2), (-1, -2, -1)), (-4, -1, -1))

    def test_edge_case_with_large_numbers(self):
        self.assertEqual(substract_elements((1000000, 2000000, 3000000), (100000, 200000, 300000)), (990000, 1800000, 2700000))

    def test_error_case_with_different_length_tuples(self):
        with self.assertRaises(ValueError):
            substract_elements((1, 2, 3), (1, 2))
