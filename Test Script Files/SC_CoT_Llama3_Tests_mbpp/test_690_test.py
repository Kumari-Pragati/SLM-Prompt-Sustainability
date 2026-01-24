import unittest
from mbpp_690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4]), [2, 6])

    def test_edge_case_empty_list(self):
        self.assertEqual(mul_consecutive_nums([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(mul_consecutive_nums([1]), [])

    def test_edge_case_two_element_list(self):
        self.assertEqual(mul_consecutive_nums([1, 2]), [])

    def test_edge_case_list_with_one_element(self):
        self.assertEqual(mul_consecutive_nums([1]), [])

    def test_edge_case_list_with_two_elements(self):
        self.assertEqual(mul_consecutive_nums([1, 2]), [])

    def test_edge_case_list_with_three_elements(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3]), [2, 6])

    def test_edge_case_list_with_four_elements(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4]), [2, 6])

    def test_edge_case_list_with_five_elements(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4, 5]), [2, 6, 12])

    def test_edge_case_list_with_six_elements(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4, 5, 6]), [2, 6, 12, 24])

    def test_edge_case_list_with_seven_elements(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4, 5, 6, 7]), [2, 6, 12, 24, 42])

    def test_edge_case_list_with_eight_elements(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8]), [2, 6, 12, 24, 42, 56])

    def test_edge_case_list_with_nine_elements(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9]), [2, 6, 12, 24, 42, 56, 72])

    def test_edge_case_list_with_ten_elements(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [2, 6, 12, 24, 42, 56, 72, 90])
