import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(multiple_to_single([1, 2, 3, 4]), 1234)
        self.assertEqual(multiple_to_single([5, 6, 7, 8]), 5678)

    def test_edge_case_single_element(self):
        self.assertEqual(multiple_to_single([1]), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(multiple_to_single([]), 0)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(multiple_to_single([-1, -2, -3]), 123)

    def test_corner_case_zero(self):
        self.assertEqual(multiple_to_single([0]), 0)
        self.assertEqual(multiple_to_single([0, 0]), 0)
        self.assertEqual(multiple_to_single([0, 0, 0]), 0)
