import unittest
from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiply_elements((1, 2, 3)), (2, 3, 6))

    def test_edge_case_empty(self):
        self.assertEqual(multiply_elements(()), ())

    def test_edge_case_single_element(self):
        self.assertEqual(multiply_elements((1,)), ())

    def test_edge_case_two_elements(self):
        self.assertEqual(multiply_elements((1, 2)), ())

    def test_edge_case_three_elements(self):
        self.assertEqual(multiply_elements((1, 2, 3)), (2, 3, 6))

    def test_edge_case_four_elements(self):
        self.assertEqual(multiply_elements((1, 2, 3, 4)), (2, 6, 12, 24))

    def test_edge_case_five_elements(self):
        self.assertEqual(multiply_elements((1, 2, 3, 4, 5)), (2, 6, 12, 24, 60))

    def test_edge_case_six_elements(self):
        self.assertEqual(multiply_elements((1, 2, 3, 4, 5, 6)), (2, 6, 12, 24, 60, 120))

    def test_edge_case_seven_elements(self):
        self.assertEqual(multiply_elements((1, 2, 3, 4, 5, 6, 7)), (2, 6, 12, 24, 60, 120, 210))

    def test_edge_case_eight_elements(self):
        self.assertEqual(multiply_elements((1, 2, 3, 4, 5, 6, 7, 8)), (2, 6, 12, 24, 60, 120, 210, 336))

    def test_edge_case_nine_elements(self):
        self.assertEqual(multiply_elements((1, 2, 3, 4, 5, 6, 7, 8, 9)), (2, 6, 12, 24, 60, 120, 210, 336, 504))

    def test_edge_case_ten_elements(self):
        self.assertEqual(multiply_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)), (2, 6, 12, 24, 60, 120, 210, 336, 504, 720))
