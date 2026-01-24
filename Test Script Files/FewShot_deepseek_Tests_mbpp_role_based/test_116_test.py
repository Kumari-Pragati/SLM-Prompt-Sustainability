import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)

    def test_edge_condition(self):
        self.assertEqual(tuple_to_int((0,)), 0)

    def test_boundary_condition(self):
        self.assertEqual(tuple_to_int((9, 9)), 99)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            tuple_to_int("123")

        with self.assertRaises(TypeError):
            tuple_to_int(123)

        with self.assertRaises(TypeError):
            tuple_to_int((1, "2", 3))

        with self.assertRaises(TypeError):
            tuple_to_int((1, 2, None))
