import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)
        self.assertEqual(tuple_to_int((4, 5, 6)), 456)
        self.assertEqual(tuple_to_int((7, 8, 9)), 789)

    def test_edge_cases(self):
        self.assertEqual(tuple_to_int(()), 0)
        self.assertEqual(tuple_to_int((0,)), 0)
        self.assertEqual(tuple_to_int((0, 0)), 0)
        self.assertEqual(tuple_to_int((0, 0, 0)), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            tuple_to_int([1, 2, 3])
        with self.assertRaises(TypeError):
            tuple_to_int("hello")
        with self.assertRaises(TypeError):
            tuple_to_int(None)

    def test_mixed_signs(self):
        self.assertEqual(tuple_to_int((-1, 2, 3)), -123)
        self.assertEqual(tuple_to_int((1, -2, 3)), 123)
        self.assertEqual(tuple_to_int((-1, -2, -3)), -123)
