import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):

    def test_remove_int(self):
        self.assertEqual(remove_datatype((1, 2.0, 'three', 4), int), (2.0, 'three'))
        self.assertEqual(remove_datatype((1, 2.0, 'three', 4), float), (1, 'three', 4))
        self.assertEqual(remove_datatype((1, 2.0, 'three', 4), str), (1, 2.0, 4))

    def test_remove_float(self):
        self.assertEqual(remove_datatype((1.0, 2.0, 'three', 4.0), int), (1, 'three', 4))
        self.assertEqual(remove_datatype((1.0, 2.0, 'three', 4.0), float), (1, 'three'))
        self.assertEqual(remove_datatype((1.0, 2.0, 'three', 4.0), str), (1, 4))

    def test_remove_str(self):
        self.assertEqual(remove_datatype(('one', 2.0, 'three', 4), int), (2.0, 'three', 4))
        self.assertEqual(remove_datatype(('one', 2.0, 'three', 4), float), (1, 'three', 4))
        self.assertEqual(remove_datatype(('one', 2.0, 'three', 4), str), (1, 2.0, 4))

    def test_empty_list(self):
        self.assertEqual(remove_datatype([], int), [])

    def test_single_element(self):
        self.assertEqual(remove_datatype([1], int), [1])
        self.assertEqual(remove_datatype([1.0], float), [1.0])
        self.assertEqual(remove_datatype([1], str), [1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_datatype('invalid', int)
