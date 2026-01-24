import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiply_list([1, 2, 3]), 6)
        self.assertEqual(multiply_list([0, 0, 0]), 0)
        self.assertEqual(multiply_list([-1, -2, -3]), 6)

    def test_edge_case_empty_list(self):
        self.assertEqual(multiply_list([]), 1)

    def test_edge_case_single_item(self):
        self.assertEqual(multiply_list([4]), 4)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(multiply_list([-1, 2, -3, 4]), -24)

    def test_corner_case_floats(self):
        self.assertAlmostEqual(multiply_list([1.1, 2.2, 3.3]), 7.058000000000001)
