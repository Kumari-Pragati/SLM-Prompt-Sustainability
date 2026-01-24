import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):
    def test_normal_input(self):
        self.assertIsInstance(new_tuple([1, 2, 3], 'abc'), tuple)
        self.assertEqual(new_tuple([1, 2, 3], 'abc'), (1, 2, 3, 'abc'))

    def test_empty_input(self):
        self.assertIsInstance(new_tuple([], ''), tuple)
        self.assertEqual(new_tuple([], ''), ([], ''))

    def test_single_input(self):
        self.assertIsInstance(new_tuple([1], 'abc'), tuple)
        self.assertEqual(new_tuple([1], 'abc'), (1, 'abc'))

    def test_list_with_str(self):
        self.assertIsInstance(new_tuple(['a', 'b'], 1), tuple)
        self.assertEqual(new_tuple(['a', 'b'], 1), ('a', 'b', 1))

    def test_str_with_list(self):
        self.assertIsInstance(new_tuple(['a', 'b'], 'c'), tuple)
        self.assertEqual(new_tuple(['a', 'b'], 'c'), ('a', 'b', 'c'))

    def test_list_with_empty_str(self):
        self.assertIsInstance(new_tuple([1], ''), tuple)
        self.assertEqual(new_tuple([1], ''), (1, ''))

    def test_empty_list_with_str(self):
        self.assertIsInstance(new_tuple([], 'abc'), tuple)
        self.assertEqual(new_tuple([], 'abc'), ('', 'abc'))

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            new_tuple(1, 2)

    def test_invalid_input_2(self):
        with self.assertRaises(TypeError):
            new_tuple([1], {})
