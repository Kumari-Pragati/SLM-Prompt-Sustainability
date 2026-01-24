import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):
    def test_add_tuple_typical(self):
        self.assertEqual(add_tuple([1, 2, 3], (4, 5, 6)), [1, 2, 3, 4, 5, 6])

    def test_add_tuple_empty_list(self):
        self.assertEqual(add_tuple([], (1, 2, 3)), [1, 2, 3])

    def test_add_tuple_empty_tuple(self):
        self.assertEqual(add_tuple([1, 2, 3], ()), [1, 2, 3])

    def test_add_tuple_non_tuple_input(self):
        with self.assertRaises(TypeError):
            add_tuple([1, 2, 3], 'test')

    def test_add_tuple_non_list_input(self):
        with self.assertRaises(TypeError):
            add_tuple('test', (1, 2, 3))
