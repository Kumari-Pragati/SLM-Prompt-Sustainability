import unittest
from mbpp_839_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_tuple(((2, 'b'), (1, 'a'))), ((1, 'a'), (2, 'b')))

    def test_empty_tuple(self):
        self.assertEqual(sort_tuple(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(sort_tuple(((1, 'a'))), ((1, 'a')))

    def test_same_first_elements_tuples(self):
        self.assertEqual(sort_tuple(((1, 'b'), (1, 'a'))), ((1, 'a'), (1, 'b')))

    def test_negative_first_elements(self):
        self.assertEqual(sort_tuple(((-2, 'b'), (-1, 'a'))), ((-1, 'a'), (-2, 'b')))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_tuple(123)

        with self.assertRaises(TypeError):
            sort_tuple('abc')

        with self.assertRaises(TypeError):
            sort_tuple([(1, 'a'), (2, 'b')])
