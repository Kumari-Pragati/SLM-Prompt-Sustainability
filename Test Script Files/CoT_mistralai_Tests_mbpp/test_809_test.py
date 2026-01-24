import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_smaller((1, 2, 3), (2, 3, 4)))
        self.assertTrue(check_smaller((5, 4, 3), (4, 3, 2)))
        self.assertTrue(check_smaller((10, 9, 8), (9, 8, 7)))

    def test_edge_case_equal_elements(self):
        self.assertTrue(check_smaller((1, 1, 2), (1, 1, 2)))
        self.assertTrue(check_smaller((1, 2, 1), (1, 2, 1)))
        self.assertTrue(check_smaller((1, 1, 1), (1, 1, 1)))

    def test_edge_case_reversed_order(self):
        self.assertTrue(check_smaller((2, 1), (1, 2)))
        self.assertTrue(check_smaller((3, 2, 1), (1, 2, 3)))
        self.assertTrue(check_smaller((4, 3, 2, 1), (1, 2, 3, 4)))

    def test_edge_case_empty_tuples(self):
        self.assertTrue(check_smaller((), ()))
        self.assertTrue(check_smaller((1), ()))
        self.assertTrue(check_smaller((), (1)))

    def test_invalid_input_types(self):
        self.assertRaises(TypeError, check_smaller, (1, 2, 3), 'abc')
        self.assertRaises(TypeError, check_smaller, 'abc', (1, 2, 3))
        self.assertRaises(TypeError, check_smaller, [1, 2, 3], (1, 2, 3))
