import unittest
from mbpp_816_code import clear_tuple

class TestClearTuple(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(clear_tuple(()), ())

    def test_non_empty_tuple(self):
        self.assertEqual(clear_tuple((1, 2, 3)), ())

    def test_tuple_with_duplicates(self):
        self.assertEqual(clear_tuple((1, 1, 2, 2, 3)), ())

    def test_tuple_with_mixed_types(self):
        self.assertEqual(clear_tuple((1, 'a', 2.5)), ())

    def test_tuple_with_nested_tuples(self):
        self.assertEqual(clear_tuple(((1, 2), (3, 4))), ())

    def test_tuple_with_empty_list(self):
        self.assertEqual(clear_tuple(([], 1, 2)), ())

    def test_tuple_with_empty_tuple(self):
        self.assertEqual(clear_tuple(((1, 2), ())), ())

    def test_tuple_with_invalid_input(self):
        with self.assertRaises(TypeError):
            clear_tuple("invalid input")
