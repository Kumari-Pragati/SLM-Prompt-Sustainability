import unittest
from mbpp_227_code import min_of_three

class TestMinOfThree(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)

    def test_edge_case_a_smallest(self):
        self.assertEqual(min_of_three(3, 2, 1), 1)

    def test_edge_case_b_smallest(self):
        self.assertEqual(min_of_three(1, 3, 2), 1)

    def test_edge_case_c_smallest(self):
        self.assertEqual(min_of_three(2, 1, 3), 1)

    def test_edge_case_all_equal(self):
        self.assertEqual(min_of_three(1, 1, 1), 1)

    def test_error_case_non_integer_input(self):
        with self.assertRaises(TypeError):
            min_of_three('a', 'b', 'c')
