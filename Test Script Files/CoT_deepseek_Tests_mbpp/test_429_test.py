import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(and_tuples((1, 2, 3), (1, 2, 4)), ((1, 2),))

    def test_empty_tuples(self):
        self.assertEqual(and_tuples((), ()), ())

    def test_different_length_tuples(self):
        self.assertEqual(and_tuples((1, 2, 3), (1, 2)), ((1, 2),))

    def test_non_tuple_inputs(self):
        with self.assertRaises(TypeError):
            and_tuples([1, 2, 3], [1, 2, 4])

    def test_tuple_with_non_set_elements(self):
        with self.assertRaises(TypeError):
            and_tuples((1, 2, [3, 4]), (1, 2, [3, 4]))

    def test_tuple_with_non_hashable_elements(self):
        with self.assertRaises(TypeError):
            and_tuples((1, 2, {3, 4}), (1, 2, {3, 4}))
