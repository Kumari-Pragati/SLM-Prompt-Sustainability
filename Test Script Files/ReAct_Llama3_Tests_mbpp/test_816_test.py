import unittest
from mbpp_816_code import clear_tuple

class TestClearTuple(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(clear_tuple(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(clear_tuple((1,)), ())

    def test_multiple_elements_tuple(self):
        self.assertEqual(clear_tuple((1, 2, 3)), ())

    def test_tuple_with_duplicates(self):
        self.assertEqual(clear_tuple((1, 1, 2, 2, 3)), ())

    def test_tuple_with_empty_subtuple(self):
        self.assertEqual(clear_tuple(((1, 2),)), ())

    def test_tuple_with_empty_subtuple_and_duplicates(self):
        self.assertEqual(clear_tuple(((1, 1),)), ())

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            clear_tuple("test")

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            clear_tuple(123)
