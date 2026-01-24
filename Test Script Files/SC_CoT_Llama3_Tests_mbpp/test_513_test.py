import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(add_str([(1,2), (3,4)], 5), [(1,2), (3,4), 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(add_str([], 6), [6])

    def test_edge_case_single_element_list(self):
        self.assertEqual(add_str([(1,2)], 3), [(1,2), 3])

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(add_str([(1,2)], 3), [(1,2), 3])

    def test_edge_case_single_element_str(self):
        self.assertEqual(add_str(["hello"], 3), ["hello", 3])

    def test_edge_case_single_element_int(self):
        self.assertEqual(add_str([1], 3), [1, 3])

    def test_edge_case_single_element_float(self):
        self.assertEqual(add_str([3.14], 3), [3.14, 3])

    def test_edge_case_single_element_none(self):
        self.assertEqual(add_str([None], 3), [None, 3])

    def test_edge_case_single_element_bool(self):
        self.assertEqual(add_str([True], 3), [True, 3])

    def test_edge_case_single_element_list_of_tuples(self):
        self.assertEqual(add_str([(1,2), (3,4)], 5), [(1,2), (3,4), 5])

    def test_edge_case_single_element_list_of_strings(self):
        self.assertEqual(add_str(["hello", "world"], 3), ["hello", "world", 3])

    def test_edge_case_single_element_list_of_ints(self):
        self.assertEqual(add_str([1, 2, 3], 4), [1, 2, 3, 4])

    def test_edge_case_single_element_list_of_floats(self):
        self.assertEqual(add_str([1.0, 2.0, 3.0], 4), [1.0, 2.0, 3.0, 4])

    def test_edge_case_single_element_list_of_none(self):
        self.assertEqual(add_str([None, None, None], 4), [None, None, None, 4])

    def test_edge_case_single_element_list_of_bool(self):
        self.assertEqual(add_str([True, True, True], 4), [True, True, True, 4])
