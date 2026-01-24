import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(average_tuple([(1, 2, 3), (4, 5, 6)]), [2.5, 5.0])

    def test_edge_case_empty_list(self):
        self.assertRaises(ZeroDivisionError, average_tuple, [])

    def test_edge_case_single_list(self):
        self.assertEqual(average_tuple([(1, 2, 3)]), [1.0])

    def test_edge_case_single_element_list(self):
        self.assertEqual(average_tuple([(1)]), [1.0])

    def test_edge_case_single_element_list_with_zero(self):
        self.assertRaises(ZeroDivisionError, average_tuple, [[0]])

    def test_edge_case_multiple_single_element_lists(self):
        self.assertEqual(average_tuple([(1), (2), (3)]), [1.0, 2.0, 3.0])

    def test_edge_case_multiple_single_element_lists_with_zero(self):
        self.assertRaises(ZeroDivisionError, average_tuple, [[0], [1], [2]])
