import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(repeat_tuples((), 3), ((), (), ()))

    def test_single_element_tuple(self):
        self.assertEqual(repeat_tuples((1,), 3), ((1,), (1,), (1,)))

    def test_multiple_elements_tuple(self):
        self.assertEqual(repeat_tuples((1, 2, 3), 2), ((1, 2, 3), (1, 2, 3)))

    def test_negative_N(self):
        with self.assertRaises(ValueError):
            repeat_tuples((1, 2, 3), -1)

    def test_zero_N(self):
        self.assertEqual(repeat_tuples((1, 2, 3), 0), ())
