import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(average_tuple([[1, 2, 3], [4, 5, 6]]), [2.5, 5.5])

    def test_edge_case_empty_list(self):
        self.assertEqual(average_tuple([]), [])

    def test_edge_case_single_list(self):
        self.assertEqual(average_tuple([[1, 2, 3]]), [2.0])

    def test_edge_case_single_element_list(self):
        self.assertEqual(average_tuple([[1]]), [1.0])

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(average_tuple([(1,)]), [1.0])

    def test_edge_case_single_element_list_of_tuples(self):
        self.assertEqual(average_tuple([(1,)]), [1.0])

    def test_edge_case_multiple_single_element_lists(self):
        self.assertEqual(average_tuple([[1], [2], [3]]), [1.0, 2.0, 3.0])

    def test_edge_case_multiple_single_element_tuples(self):
        self.assertEqual(average_tuple([(1,), (2,), (3,)]), [1.0, 2.0, 3.0])

    def test_edge_case_multiple_single_element_lists_of_tuples(self):
        self.assertEqual(average_tuple([(1,), (2,), (3,)]), [1.0, 2.0, 3.0])

    def test_edge_case_invalid_input_type(self):
        with self.assertRaises(TypeError):
            average_tuple('abc')

    def test_edge_case_invalid_input_structure(self):
        with self.assertRaises(TypeError):
            average_tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
