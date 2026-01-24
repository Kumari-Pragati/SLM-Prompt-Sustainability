import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 2), 2)

    def test_edge_case_max_in_array(self):
        self.assertEqual(min_Ops([5, 5, 5, 5, 5], 5, 2), 2)

    def test_edge_case_min_in_array(self):
        self.assertEqual(min_Ops([1, 1, 1, 1, 1], 5, 2), 2)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            min_Ops([1, 2, 3, 4, 5], '5', 2)

    def test_invalid_input_non_positive_integer(self):
        with self.assertRaises(TypeError):
            min_Ops([1, 2, 3, 4, 5], 0, 2)

    def test_invalid_input_non_integer_array(self):
        with self.assertRaises(TypeError):
            min_Ops(['a', 'b', 'c', 'd', 'e'], 5, 2)

    def test_invalid_input_non_array(self):
        with self.assertRaises(TypeError):
            min_Ops(1, 5, 2)

    def test_invalid_input_non_integer_k(self):
        with self.assertRaises(TypeError):
            min_Ops([1, 2, 3, 4, 5], 5, '2')

    def test_invalid_input_non_positive_integer_k(self):
        with self.assertRaises(TypeError):
            min_Ops([1, 2, 3, 4, 5], 5, 0)
