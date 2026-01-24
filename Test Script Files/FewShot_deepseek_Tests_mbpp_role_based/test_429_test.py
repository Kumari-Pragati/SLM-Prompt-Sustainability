import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(and_tuples((1, 2, 3), (1, 2, 4)), ((1, 2),))

    def test_edge_condition(self):
        self.assertEqual(and_sets((1,), (1, 2, 3)), ((1,),))

    def test_boundary_condition(self):
        self.assertEqual(and_sets((1, 2, 3), (1, 2, 3)), ((1, 2, 3),))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            and_tuples((1, 2, 3), "1, 2, 3")
