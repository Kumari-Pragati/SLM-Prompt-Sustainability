import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_no_of_ways(3, 2), 3)

    def test_edge_case_n_1(self):
        self.assertEqual(count_no_of_ways(1, 2), 2)

    def test_edge_case_n_2(self):
        self.assertEqual(count_no_of_ways(2, 2), 4)

    def test_edge_case_k_1(self):
        self.assertEqual(count_no_of_ways(3, 1), 1)

    def test_edge_case_k_0(self):
        with self.assertRaises(ZeroDivisionError):
            count_no_of_ways(3, 0)

    def test_invalid_input_type_n(self):
        with self.assertRaises(TypeError):
            count_no_of_ways("3", 2)

    def test_invalid_input_type_k(self):
        with self.assertRaises(TypeError):
            count_no_of_ways(3, "2")
