import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):

    def test_remove_datatype_with_int(self):
        test_tuple = (1, 2, 3, '4', 5)
        data_type = int
        self.assertEqual(remove_datatype(test_tuple, data_type), [1, 2, 3, 5])

    def test_remove_datatype_with_str(self):
        test_tuple = ('1', '2', '3', 4, '5')
        data_type = str
        self.assertEqual(remove_datatype(test_tuple, data_type), [4])

    def test_remove_datatype_with_float(self):
        test_tuple = (1.1, 2.2, 3.3, '4.4', 5.5)
        data_type = float
        self.assertEqual(remove_datatype(test_tuple, data_type), [1.1, 2.2, 3.3, 5.5])

    def test_remove_datatype_with_empty_tuple(self):
        test_tuple = ()
        data_type = int
        self.assertEqual(remove_datatype(test_tuple, data_type), [])

    def test_remove_datatype_with_all_same_type(self):
        test_tuple = (1, 2, 3)
        data_type = int
        self.assertEqual(remove_datatype(test_tuple, data_type), [])
