import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):

    def test_simple_integer(self):
        self.assertEqual(remove_datatype((1, 2.5, 'a'), int), [2.5, 'a'])

    def test_simple_float(self):
        self.assertEqual(remove_datatype((1, 2.5, 'a'), float), [1, 'a'])

    def test_simple_string(self):
        self.assertEqual(remove_datatype(('a', 2.5, 1), str), [2.5, 1])

    def test_empty_list(self):
        self.assertEqual(remove_datatype([], int), [])

    def test_single_element(self):
        self.assertEqual(remove_datatype((1,), int), [])

    def test_min_integer(self):
        self.assertEqual(remove_datatype((-9223372036854775807, 2.5, 'a'), int), [2.5, 'a'])

    def test_max_integer(self):
        self.assertEqual(remove_datatype((9223372036854775807, 2.5, 'a'), int), [2.5, 'a'])

    def test_min_float(self):
        self.assertEqual(remove_datatype((-9223372036854775807.0, 2.5, 'a'), float), [1, 'a'])

    def test_max_float(self):
        self.assertEqual(remove_datatype((9223372036854775807.0, 2.5, 'a'), float), [1, 'a'])

    def test_mixed_types(self):
        self.assertEqual(remove_datatype(('a', 1, 2.5, True, [1, 2, 3]), str), [1, 2.5, True, [1, 2, 3]])
