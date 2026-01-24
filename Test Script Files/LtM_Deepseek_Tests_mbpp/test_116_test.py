import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)
        self.assertEqual(tuple_to_int((9, 8, 7)), 987)

    def test_boundary_conditions(self):
        self.assertEqual(tuple_to_int((0,)), 0)
        self.assertEqual(tuple_to_int((9, 0)), 90)
        self.assertEqual(tuple_to_int((0, 9)), 9)
        self.assertEqual(tuple_to_int((9, 9)), 99)

    def test_edge_cases(self):
        self.assertEqual(tuple_to_int(()), 0)
        self.assertEqual(tuple_to_int((1, 2, 3, 4, 5, 6, 7, 8, 9, 0)), 1234567890)
        self.assertEqual(tuple_to_int((9, 8, 7, 6, 5, 4, 3, 2, 1, 0)), 9876543210)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            tuple_to_int("123")
        with self.assertRaises(TypeError):
            tuple_to_int(123)
        with self.assertRaises(TypeError):
            tuple_to_int([1, 2, 3])
