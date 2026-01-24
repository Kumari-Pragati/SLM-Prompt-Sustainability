import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_smaller((1, 2, 3), (2, 3, 4)))

    def test_edge_case(self):
        self.assertFalse(check_smaller((3, 2, 1), (2, 3, 4)))

    def test_boundary_case(self):
        self.assertTrue(check_smaller((1, 1, 1), (2, 2, 2)))
        self.assertFalse(check_smaller((2, 2, 2), (1, 1, 1)))

    def test_special_case(self):
        self.assertTrue(check_smaller((1, 2, 3), (1, 2, 3)))
        self.assertFalse(check_smaller((1, 2, 3), (0, 1, 2)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_smaller((1, 2, 3), "abc")

        with self.assertRaises(TypeError):
            check_smaller("abc", (1, 2, 3))

        with self.assertRaises(TypeError):
            check_smaller("abc", "def")
