import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):

    def test_remove_datatype_with_integers(self):
        self.assertEqual(remove_datatype((1, 2, 3, 4, 5), int), [1, 2, 3, 4, 5])

    def test_remove_datatype_with_floats(self):
        self.assertEqual(remove_datatype((1.1, 2.2, 3.3, 4.4, 5.5), float), [1.1, 2.2, 3.3, 4.4, 5.5])

    def test_remove_datatype_with_strings(self):
        self.assertEqual(remove_datatype(('a', 'b', 'c', 'd', 'e'), str), ['a', 'b', 'c', 'd', 'e'])

    def test_remove_datatype_with_mixed_datatypes(self):
        self.assertEqual(remove_datatype((1, 'a', 2.2, 'b', 3), str), [1, 2.2, 3])

    def test_remove_datatype_with_empty_tuple(self):
        self.assertEqual(remove_datatype((), int), [])

    def test_remove_datatype_with_invalid_data_type(self):
        with self.assertRaises(TypeError):
            remove_datatype((1, 2, 3), 'int')

    def test_remove_datatype_with_none_data_type(self):
        with self.assertRaises(TypeError):
            remove_datatype((1, 2, 3), None)
