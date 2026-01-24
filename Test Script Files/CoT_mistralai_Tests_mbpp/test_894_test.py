import unittest
from mbpp_894_code import float_to_tuple

class TestFloatToTuple(unittest.TestCase):

    def test_valid_input(self):
        self.assertTupleEqual(float_to_tuple('1, 2.5, 3.0'), (1.0, 2.5, 3.0))
        self.assertTupleEqual(float_to_tuple('-1, -2.5, -3.0'), (-1.0, -2.5, -3.0))
        self.assertTupleEqual(float_to_tuple('0, 0.0, 0.0'), (0.0, 0.0, 0.0))

    def test_empty_input(self):
        self.assertIsInstance(float_to_tuple(''), tuple)
        self.assertIsInstance(float_to_tuple(' '), tuple)
        self.assertIsInstance(float_to_tuple('\t'), tuple)
        self.assertIsInstance(float_to_tuple('\n'), tuple)

    def test_single_input(self):
        self.assertIsInstance(float_to_tuple('1'), (float,))
        self.assertIsInstance(float_to_tuple('-1'), (float,))
        self.assertIsInstance(float_to_tuple('0'), (float,))

    def test_invalid_input(self):
        self.assertRaises(ValueError, float_to_tuple, '1, 2, 3')
        self.assertRaises(ValueError, float_to_tuple, '1, 2, 3, 4')
        self.assertRaises(ValueError, float_to_tuple, '1, 2, 3, 4, 5')
        self.assertRaises(ValueError, float_to_tuple, '1, 2, 3, 4, 5, 6, 7, 8, 9, 0.1')
