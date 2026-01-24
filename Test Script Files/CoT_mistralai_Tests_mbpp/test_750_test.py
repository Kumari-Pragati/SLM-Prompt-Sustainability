import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):
    def test_add_tuple_with_lists_and_tuples(self):
        self.assertListEqual(add_tuple([1, 2, 3], (4, 5, 6)), [1, 2, 3, 4, 5, 6])
        self.assertListEqual(add_tuple([], (1, 2, 3)), [1, 2, 3])
        self.assertListEqual(add_tuple((1, 2, 3), [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertListEqual(add_tuple([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_add_tuple_with_empty_inputs(self):
        self.assertListEqual(add_tuple([], []), [])
        self.assertListEqual(add_tuple([], (1, 2, 3)), [1, 2, 3])
        self.assertListEqual(add_tuple((1, 2, 3), []), [1, 2, 3])

    def test_add_tuple_with_mixed_types(self):
        with self.assertRaises(TypeError):
            add_tuple([1, 2, 3], 'not a tuple')
        with self.assertRaises(TypeError):
            add_tuple((1, 2, 3), 4)
