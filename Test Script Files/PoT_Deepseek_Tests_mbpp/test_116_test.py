import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)
        self.assertEqual(tuple_to_int((9, 0, 8)), 908)
        self.assertEqual(tuple_to_int((0, 0, 0)), 0)

    def test_edge_cases(self):
        self.assertEqual(tuple_to_int((0,)), 0)
        self.assertEqual(tuple_to_int((9,)), 9)

    def test_boundary_cases(self):
        self.assertEqual(tuple_to_int((9, 9, 9, 9, 9)), 99999)
        self.assertEqual(tuple_to_int((0, 0, 0, 0, 0)), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            tuple_to_int((1, '2', 3))
        with self.assertRaises(TypeError):
            tuple_to_int((1, 2, '3'))
        with self.assertRaises(TypeError):
            tuple_to_int((1, '2', '3'))
