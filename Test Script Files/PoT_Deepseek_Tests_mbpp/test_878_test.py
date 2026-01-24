import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_tuples((1, 2, 3), {1, 2, 3}))

    def test_edge_case(self):
        self.assertFalse(check_tuples((1, 2, 3), set()))

    def test_boundary_case(self):
        self.assertTrue(check_tuples((), set()))
        self.assertFalse(check_tuples((1,), set()))

    def test_corner_case(self):
        self.assertTrue(check_tuples((1, 2, 3), {1, 2, 3, 4, 5}))
        self.assertFalse(check_tuples((1, 2, 3), {4, 5, 6, 7, 8}))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_tuples("not a tuple", set())
        with self.assertRaises(TypeError):
            check_tuples((1, 2, 3), "not a set")
