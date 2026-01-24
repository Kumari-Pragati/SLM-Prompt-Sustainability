import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(and_tuples((1, 2, 3), (1, 2, 4)), (1, 2))

    def test_empty_tuples(self):
        self.assertEqual(and_tuples((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(and_tuples((1,), (1,)), (1,))

    def test_different_length_tuples(self):
        self.assertEqual(and_tuples((1, 2, 3), (1, 2)), (1, 2))

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            and_tuples((1, 'a'), (1, 2))

    def test_non_tuple_arguments(self):
        with self.assertRaises(TypeError):
            and_tuples([1, 2, 3], (1, 2, 4))
