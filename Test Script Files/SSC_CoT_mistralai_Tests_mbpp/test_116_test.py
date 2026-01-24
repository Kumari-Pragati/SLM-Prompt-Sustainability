import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)
        self.assertEqual(tuple_to_int((0, 0, 0)), 0)
        self.assertEqual(tuple_to_int((9, 9, 9)), 729)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(tuple_to_int(()), 0)
        self.assertEqual(tuple_to_int((1,)), 1)
        self.assertEqual(tuple_to_int((1, 2, 3, 4)), 12034)
        self.assertEqual(tuple_to_int((10, 20, 30, 40)), 102340)
        self.assertEqual(tuple_to_int((-1, -2, -3)), 123)

    def test_special_cases(self):
        self.assertEqual(tuple_to_int((0, 0, 1)), 1)
        self.assertEqual(tuple_to_int((1, 0, 0)), 1)
        self.assertEqual(tuple_to_int((0, 1, 0)), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, tuple_to_int, ('1', '2', '3'))
        self.assertRaises(TypeError, tuple_to_int, (1.1, 2.2, 3.3))
        self.assertRaises(TypeError, tuple_to_int, (True, False, True))
