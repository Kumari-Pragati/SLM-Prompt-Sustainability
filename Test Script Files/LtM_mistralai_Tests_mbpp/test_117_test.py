import unittest
from mbpp_117_code import list_to_float

class TestListToFloat(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(list_to_float([(1.0, 2.0), ('a', 3.0)]), '[(a, 3.0)]')

    def test_empty_list(self):
        self.assertEqual(list_to_float([]), '[]')

    def test_single_element_list(self):
        self.assertEqual(list_to_float([('a',)]), '[]')
        self.assertEqual(list_to_float([(1.0)]), '[]')

    def test_all_strings(self):
        self.assertEqual(list_to_float([('a', 'b', 'c')]), '[(a,), (b,), (c,)]')

    def test_all_floats(self):
        self.assertEqual(list_to_float([(1.0, 2.0, 3.0)]), '[(1.0, 2.0, 3.0)]')

    def test_mixed_strings_and_floats(self):
        self.assertEqual(list_to_float([('a', 1.0, 'b')]), '[(a, 1.0, b)]')

    def test_invalid_input(self):
        self.assertRaises(TypeError, list_to_float, [1, 2, 3])
