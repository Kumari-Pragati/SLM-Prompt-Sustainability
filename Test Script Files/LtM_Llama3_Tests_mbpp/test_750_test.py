import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(add_tuple([], (1, 2)), [1, 2])

    def test_non_empty_list(self):
        self.assertEqual(add_tuple([1, 2, 3], (4, 5)), [1, 2, 3, 4, 5])

    def test_empty_tuple(self):
        self.assertEqual(add_tuple([1, 2], ()), [1, 2])

    def test_non_empty_tuple(self):
        self.assertEqual(add_tuple([1, 2], (3, 4)), [1, 2, 3, 4])

    def test_list_and_tuple_mixed(self):
        self.assertEqual(add_tuple([1, 2], (3, 4, 5)), [1, 2, 3, 4, 5])

    def test_list_and_tuple_mixed_reverse(self):
        self.assertEqual(add_tuple([1, 2, 3, 4, 5], ()), [1, 2, 3, 4, 5])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add_tuple('not a list', (1, 2))
