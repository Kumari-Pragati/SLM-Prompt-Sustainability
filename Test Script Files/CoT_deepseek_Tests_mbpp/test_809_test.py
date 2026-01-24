import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_smaller((1, 2, 3), (2, 3, 4)))

    def test_edge_case(self):
        self.assertFalse(check_smaller((3, 2, 1), (2, 3, 4)))

    def test_boundary_case(self):
        self.assertTrue(check_smaller((1, 2, 3), (1, 2, 3)))
        self.assertFalse(check_smaller((3, 2, 1), (1, 2, 3)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_smaller((1, 2, 3), "string")
        with self.assertRaises(TypeError):
            check_smaller("string", (1, 2, 3))
        with self.assertRaises(TypeError):
            check_smaller("string", "string")
