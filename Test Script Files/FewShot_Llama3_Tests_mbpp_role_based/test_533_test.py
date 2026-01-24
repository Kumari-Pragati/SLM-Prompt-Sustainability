import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):
    def test_typical_use_case(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 'a', 2.5, 'b', 3])

    def test_edge_case_empty_tuple(self):
        test_tuple = ()
        data_type = str
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [])

    def test_edge_case_single_element_tuple(self):
        test_tuple = (1,)
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [])

    def test_edge_case_single_element_tuple_non_datatype(self):
        test_tuple = ('a',)
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, ['a'])

    def test_edge_case_single_element_tuple_datatype(self):
        test_tuple = (1,)
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1])

    def test_edge_case_tuple_with_datatype_elements(self):
        test_tuple = (1, 2, 3)
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2, 3])

    def test_edge_case_tuple_with_non_datatype_elements(self):
        test_tuple = ('a', 'b', 'c')
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [])
