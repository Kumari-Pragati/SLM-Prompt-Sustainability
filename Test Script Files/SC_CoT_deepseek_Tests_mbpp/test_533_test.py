import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):
    
    def test_typical_case(self):
        test_tuple = (1, 'a', 2.0, 'b')
        data_type = str
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2.0])

    def test_empty_tuple(self):
        test_tuple = ()
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [])

    def test_all_same_type(self):
        test_tuple = ('a', 'b', 'c')
        data_type = str
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [])

    def test_mixed_types(self):
        test_tuple = (1, 'a', 2.0, 'b')
        data_type = object
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, test_tuple)

    def test_invalid_input(self):
        test_tuple = (1, 'a', 2.0, 'b')
        data_type = 10
        with self.assertRaises(TypeError):
            remove_datatype(test_tuple, data_type)
