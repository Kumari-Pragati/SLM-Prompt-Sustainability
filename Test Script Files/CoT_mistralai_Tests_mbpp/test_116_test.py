import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)
        self.assertEqual(tuple_to_int((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)), 123456789)

    def test_negative_numbers(self):
        self.assertEqual(tuple_to_int((-1, -2, -3)), 123)
        self.assertEqual(tuple_to_int((-9, -8, -7, -6, -5, -4, -3, -2, -1)), 987654321)

    def test_mixed_numbers(self):
        self.assertEqual(tuple_to_int((1, -2, 3, -4, 5)), 135)
        self.assertEqual(tuple_to_int((-9, 8, -7, 6, -5, 4, 3, -2, 1)), 86431)

    def test_empty_tuple(self):
        self.assertEqual(tuple_to_int(()), 0)

    def test_single_number(self):
        self.assertEqual(tuple_to_int((1)), 1)

    def test_single_zero(self):
        self.assertEqual(tuple_to_int((0)), 0)

    def test_single_negative_number(self):
        self.assertEqual(tuple_to_int((-1)), -1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, tuple_to_int, [1, 2, 3])
        self.assertRaises(TypeError, tuple_to_int, (1, '2', 3))
        self.assertRaises(TypeError, tuple_to_int, (1, 2, '3'))
