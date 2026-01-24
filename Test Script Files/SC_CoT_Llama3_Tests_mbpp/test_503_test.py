import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5]), [1, 1, 2, 3, 4])

    def test_edge_case_single_element(self):
        self.assertEqual(add_consecutive_nums([1]), [])

    def test_edge_case_empty_list(self):
        self.assertEqual(add_consecutive_nums([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(add_consecutive_nums([1, 1]), [])

    def test_edge_case_list_with_one_element(self):
        self.assertEqual(add_consecutive_nums([1]), [])

    def test_edge_case_list_with_two_elements(self):
        self.assertEqual(add_consecutive_nums([1, 2]), [])

    def test_edge_case_list_with_three_elements(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3]), [1, 1, 2])

    def test_edge_case_list_with_four_elements(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4]), [1, 1, 2, 3])

    def test_edge_case_list_with_five_elements(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5]), [1, 1, 2, 3, 4])

    def test_edge_case_list_with_six_elements(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5, 6]), [1, 1, 2, 3, 4, 5])

    def test_edge_case_list_with_seven_elements(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5, 6, 7]), [1, 1, 2, 3, 4, 5, 6])

    def test_edge_case_list_with_eight_elements(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8]), [1, 1, 2, 3, 4, 5, 6, 7])

    def test_edge_case_list_with_nine_elements(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_edge_case_list_with_ten_elements(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_list_with_eleven_elements(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_edge_case_list_with_twelve_elements(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_edge_case_list_with_thirteen_elements(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_edge_case_list_with_fourteen_elements(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_edge_case_list_with_fifteen