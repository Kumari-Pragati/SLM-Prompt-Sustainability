import unittest
from mbpp_296_code import get_Inv_Count

class TestGetInvCount(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_Inv_Count([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(get_Inv_Count([5, 4, 3, 2, 1], 5), 5)
        self.assertEqual(get_Inv_Count([1, 1, 1, 1, 1], 5), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(get_Inv_Count([1], 1), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(get_Inv_Count([], 0), 0)

    def test_boundary_case_first_element_larger(self):
        self.assertEqual(get_Inv_Count([5, 1, 2, 3, 4], 5), 4)

    def test_boundary_case_last_element_smaller(self):
        self.assertEqual(get_Inv_Count([1, 2, 3, 4, 1], 5), 4)

    def test_boundary_case_first_and_last_equal(self):
        self.assertEqual(get_Inv_Count([1, 1, 2, 3, 1], 5), 3)

    def test_invalid_input_negative_list_length(self):
        with self.assertRaises(ValueError):
            get_Inv_Count([1, 2, 3], -1)

    def test_invalid_input_negative_array_length(self):
        with self.assertRaises(ValueError):
            get_Inv_Count([], -1)
