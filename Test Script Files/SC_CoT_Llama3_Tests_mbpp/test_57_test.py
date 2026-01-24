import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(find_Max_Num([123, 45, 78], 3), 123)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Max_Num([123], 1), 123)

    def test_edge_case_empty_array(self):
        with self.assertRaises(IndexError):
            find_Max_Num([], 1)

    def test_edge_case_single_element_zero(self):
        self.assertEqual(find_Max_Num([0], 1), 0)

    def test_edge_case_single_element_negative(self):
        self.assertEqual(find_Max_Num([-123], 1), -123)

    def test_edge_case_max_num_zero(self):
        self.assertEqual(find_Max_Num([0, 0, 0], 3), 0)

    def test_edge_case_max_num_negative(self):
        self.assertEqual(find_Max_Num([-123, -45, -78], 3), -123)

    def test_edge_case_max_num_mixed(self):
        self.assertEqual(find_Max_Num([123, -45, 78], 3), 123)

    def test_edge_case_max_num_all_negative(self):
        self.assertEqual(find_Max_Num([-123, -45, -78], 3), -123)

    def test_edge_case_max_num_all_zero(self):
        self.assertEqual(find_Max_Num([0, 0, 0], 3), 0)

    def test_edge_case_max_num_all_positive(self):
        self.assertEqual(find_Max_Num([123, 45, 78], 3), 123)

    def test_edge_case_max_num_mixed_negative(self):
        self.assertEqual(find_Max_Num([-123, 45, -78], 3), -123)

    def test_edge_case_max_num_mixed_positive(self):
        self.assertEqual(find_Max_Num([123, -45, 78], 3), 123)

    def test_edge_case_max_num_mixed_zero(self):
        self.assertEqual(find_Max_Num([0, 123, 0], 3), 123)

    def test_edge_case_max_num_mixed_negative_zero(self):
        self.assertEqual(find_Max_Num([-123, 0, -78], 3), -123)
