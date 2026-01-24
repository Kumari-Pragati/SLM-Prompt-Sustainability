import unittest
from mbpp_610_code import remove_kth_element

class TestRemoveKthElement(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 3), [1, 2, 3, 5])
    def test_edge_case_1(self):
        self.assertEqual(remove_kth_element([1, 2, 3], 1), [1, 2])
    def test_edge_case_2(self):
        self.assertEqual(remove_kth_element([1, 2, 3], 3), [1, 2])
    def test_edge_case_3(self):
        self.assertEqual(remove_kth_element([1, 2, 3], 4), [1, 2, 3])
    def test_edge_case_4(self):
        self.assertEqual(remove_kth_element([1, 2, 3], 5), [1, 2, 3])
    def test_edge_case_5(self):
        self.assertEqual(remove_kth_element([], 1), [])
