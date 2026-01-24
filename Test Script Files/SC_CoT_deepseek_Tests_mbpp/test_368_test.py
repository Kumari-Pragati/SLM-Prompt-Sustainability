import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):

    def test_typical_case(self):
        test_tup = (1, 2, 3)
        N = 3
        expected_output = ((1, 2, 3),) * N
        self.assertEqual(repeat_tuples(test_tup, N), expected_output)

    def test_edge_case(self):
        test_tup = ()
        N = 5
        expected_output = ((),) * N
        self.assertEqual(repeat_tuples(test_tup, N), expected_output)

    def test_boundary_case(self):
        test_tup = (1, 2, 3)
        N = 0
        expected_output = ()
        self.assertEqual(repeat_tuples(test_tup, N), expected_output)

    def test_invalid_input(self):
        test_tup = (1, 2, 3)
        N = -1
        with self.assertRaises(ValueError):
            repeat_tuples(test_tup, N)
