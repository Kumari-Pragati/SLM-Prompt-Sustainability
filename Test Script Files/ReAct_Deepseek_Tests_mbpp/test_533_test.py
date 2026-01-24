import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):

    def test_remove_datatype_typical_case(self):
        test_tuple = (1, 'a', 2.0, True)
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2.0, True])

    def test_remove_datatype_empty_tuple(self):
        test_tuple = ()
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [])

    def test_remove_datatype_all_elements_of_same_type(self):
        test_tuple = (1, 2, 3)
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [])

    def test_remove_datatype_all_elements_of_different_types(self):
        test_tuple = (1, 'a', 2.0, True)
        data_type = str
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2.0, True])

    def test_remove_datatype_none_elements_of_specified_type(self):
        test_tuple = ('a', 'b', 'c')
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [])
