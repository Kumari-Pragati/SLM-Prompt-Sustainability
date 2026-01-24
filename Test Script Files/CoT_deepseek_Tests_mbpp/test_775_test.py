import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(odd_position([1, 3, 5]))

    def test_typical_case_2(self):
        self.assertTrue(odd_position([2, 4, 6]))

    def test_typical_case_3(self):
        self.assertFalse(odd_position([1, 2, 3]))

    def test_typical_case_4(self):
        self.assertFalse(odd_position([2, 3, 4]))

    def test_edge_case_empty_list(self):
        self.assertTrue(odd_position([]))

    def test_edge_case_single_element(self):
        self.assertTrue(odd_position([1]))

    def test_edge_case_single_even_element(self):
        self.assertTrue(odd_position([2]))

    def test_boundary_case_all_even(self):
        self.assertFalse(odd_position([2, 4, 6, 8]))

    def test_boundary_case_all_odd(self):
        self.assertTrue(odd_position([1, 3, 5, 7]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            odd_position(123)

        with self.assertRaises(TypeError):
            odd_position('123')

        with self.assertRaises(TypeError):
            odd_position(None)

        with self.assertRaises(TypeError):
            odd_position([1, '2', 3])

        with self.assertRaises(TypeError):
            odd_position([1, None, 3])
