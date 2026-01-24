import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):
    def test_typical_input(self):
        test_tuple = (1, 2, 3, 4, 5)
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [])

    def test_edge_case(self):
        test_tuple = (1, 2, 3, 4, 5)
        data_type = str
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_edge_case2(self):
        test_tuple = (1, 2, 3, 4, 5)
        data_type = float
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [])

    def test_edge_case3(self):
        test_tuple = (1, 2, 3, 4, 5)
        data_type = bool
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [])

    def test_edge_case4(self):
        test_tuple = (1, 2, 3, 4, 5)
        data_type = object
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [])

    def test_invalid_input(self):
        test_tuple = (1, 2, 3, 4, 5)
        data_type ='string'
        with self.assertRaises(TypeError):
            remove_datatype(test_tuple, data_type)

    def test_empty_input(self):
        test_tuple = ()
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [])

    def test_single_element_input(self):
        test_tuple = (1,)
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [])

    def test_single_element_input2(self):
        test_tuple = (1,)
        data_type = str
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1])

    def test_multiple_datatypes(self):
        test_tuple = (1, 2, 3, 4, 5)
        data_type = (int, str, float)
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_multiple_datatypes2(self):
        test_tuple = (1, 2, 3, 4, 5)
        data_type = (int, float)
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2, 3, 4, 5])
