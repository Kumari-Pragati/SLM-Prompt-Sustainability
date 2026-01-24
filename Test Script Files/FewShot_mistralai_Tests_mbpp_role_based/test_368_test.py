import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):
    def test_positive_integer_input(self):
        self.assertEqual(repeat_tuples((1, 2), 3), ((1, 2), (1, 2), (1, 2)))

    def test_zero_input(self):
        self.assertEqual(repeat_tuples((1, 2), 0), ())

    def test_negative_integer_input(self):
        self.assertEqual(repeat_tuples((1, 2), -1), ())

    def test_empty_tuple_input(self):
        self.assertEqual(repeat_tuples((), 3), ((), (), ()))

    def test_string_input(self):
        with self.assertRaises(TypeError):
            repeat_tuples('abc', 3)
