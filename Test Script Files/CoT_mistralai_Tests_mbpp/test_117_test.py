import unittest
from mbpp_117_code import list_to_float

class TestListToFloat(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(list_to_float([]), '[]')

    def test_single_element_list(self):
        self.assertEqual(list_to_float([1]), '[(1.0)]')
        self.assertEqual(list_to_float(['a']), '[(a)]')
        self.assertEqual(list_to_float([1, 'a']), '[(1.0), (a)]')

    def test_multiple_elements_list(self):
        self.assertEqual(list_to_float([1, 2, 3]), '[(1.0), (2.0), (3.0)]')
        self.assertEqual(list_to_float(['a', 'b', 'c']), '[(a), (b), (c)]')
        self.assertEqual(list_to_float([1, 'a', 2, 'b', 3, 'c']), '[(1.0), (a), (2.0), (b), (3.0), (c)]')

    def test_mixed_list(self):
        self.assertEqual(list_to_float([1, 'a', 'b', 2, 'c', 3]), '[(1.0), (a), (b), (2.0), (c), (3.0)]')
        self.assertEqual(list_to_float(['a', 1, 'b', '2', 'c', 3]), '[(a), (1.0), (b), (2.0), (c), (3.0)]')

    def test_invalid_input(self):
        self.assertRaises(TypeError, list_to_float, [1, 'a', [1, 2, 3]])
        self.assertRaises(TypeError, list_to_float, [1, 'a', (1, 2, 3)])
        self.assertRaises(TypeError, list_to_float, [1, 'a', {'key': 'value'}])
        self.assertRaises(TypeError, list_to_float, [1, 'a', None])
