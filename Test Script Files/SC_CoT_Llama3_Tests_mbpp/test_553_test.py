import unittest
from mbpp_553_code import tuple_to_float

class TestTupleToFloat(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(tuple_to_float((1, 2, 3)), 1.23)
        self.assertEqual(tuple_to_float((4, 5, 6)), 4.56)
        self.assertEqual(tuple_to_float((7, 8, 9)), 7.89)

    def test_edge_cases(self):
        self.assertEqual(tuple_to_float((0, 0, 0)), 0.0)
        self.assertEqual(tuple_to_float((1, 0, 0)), 1.0)
        self.assertEqual(tuple_to_float((0, 1, 0)), 0.1)
        self.assertEqual(tuple_to_float((0, 0, 1)), 0.1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            tuple_to_float(None)
        with self.assertRaises(TypeError):
            tuple_to_float("")
        with self.assertRaises(TypeError):
            tuple_to_float(123)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            tuple_to_float(())
