import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):
    def test_typical_use_case(self):
        test_tuple = (1, 'a', 2.5, 'b')
        data_type = str
        expected_output = (1, 2.5)
        self.assertEqual(remove_datatype(test_tuple, data_type), expected_output)

    def test_edge_condition(self):
        test_tuple = ()
        data_type = int
        expected_output = ()
        self.assertEqual(remove_datatype(test_tuple, data_type), expected_output)

    def test_boundary_condition(self):
        test_tuple = (1, 'a', 2.5, 'b')
        data_type = int
        expected_output = ('a', 'b')
        self.assertEqual(remove_datatype(test_tuple, data_type), expected_output)

    def test_invalid_input(self):
        test_tuple = (1, 'a', 2.5, 'b')
        data_type = 10
        with self.assertRaises(TypeError):
            remove_datatype(test_tuple, data_type)
