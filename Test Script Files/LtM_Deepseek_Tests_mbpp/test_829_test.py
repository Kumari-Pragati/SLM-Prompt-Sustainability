import unittest
from mbpp_829_code import second_frequent

class TestSecondFrequent(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(second_frequent([1, 2, 2, 3, 3, 3]), 2)

    def test_edge_case_single_element(self):
        self.assertIsNone(second_frequent([1]))

    def test_edge_case_empty_list(self):
        self.assertIsNone(second_frequent([]))

    def test_boundary_case_all_same_elements(self):
        self.assertIsNone(second_frequent([1, 1, 1, 1, 1]))

    def test_complex_case_multiple_second_frequent_elements(self):
        self.assertEqual(second_frequent([1, 2, 2, 3, 3, 3, 4, 4]), 3)

    def test_complex_case_second_frequent_elements_with_one_element(self):
        self.assertEqual(second_frequent([1, 2, 2, 3, 3]), 2)
