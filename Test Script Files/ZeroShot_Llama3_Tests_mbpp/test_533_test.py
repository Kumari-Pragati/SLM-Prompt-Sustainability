import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):

    def test_remove_datatype(self):
        test_tuple = (1, 2, 'a', 'b', 3.0, 'c', 'd')
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, ['a', 'b', 'c', 'd'])

    def test_remove_datatype_empty(self):
        test_tuple = ()
        data_type = str
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [])

    def test_remove_datatype_no_match(self):
        test_tuple = (1, 2, 3, 4, 5)
        data_type = str
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_remove_datatype_multiple_match(self):
        test_tuple = (1, 2, 'a', 'b', 3.0, 'c', 'd', 'e', 'f')
        data_type = str
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2, 3.0])

    def test_remove_datatype_single_match(self):
        test_tuple = (1, 2, 'a', 3.0, 'c', 'd')
        data_type = str
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2, 3.0])
