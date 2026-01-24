import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertLessEqual(tuple_size(()), 56)
        self.assertLessEqual(tuple_size((1,)), 80)
        self.assertLessEqual(tuple_size((1, 2, 3)), 88)

    def test_edge_conditions(self):
        self.assertLessEqual(tuple_size(()), 56)

    def test_boundary_conditions(self):
        self.assertLessEqual(tuple_size(tuple(range(1000))), 8000)
        self.assertLessEqual(tuple_size(tuple(range(10000))), 80000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            tuple_size(1)
        with self.assertRaises(TypeError):
            tuple_size('string')
        with self.assertRaises(TypeError):
            tuple_size(None)
