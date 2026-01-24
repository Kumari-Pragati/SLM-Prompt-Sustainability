import unittest
from mbpp_610_code import remove_kth_element

class TestRemoveKthElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 3), [1, 2, 3, 5])

    def test_edge_case_L1(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 1), [1, 2, 3, 4])

    def test_edge_case_Llast(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 5), [1, 2, 3, 4])

    def test_edge_case_L0(self):
        with self.assertRaises(IndexError):
            remove_kth_element([1, 2, 3, 4, 5], 0)

    def test_edge_case_Lgreater_than_length(self):
        with self.assertRaises(IndexError):
            remove_kth_element([1, 2, 3, 4, 5], 6)

    def test_empty_list(self):
        self.assertEqual(remove_kth_element([], 1), [])

    def test_single_element_list(self):
        self.assertEqual(remove_kth_element([1], 1), [])
