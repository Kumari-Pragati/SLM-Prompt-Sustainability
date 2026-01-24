import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_smaller((1, 2, 3), (2, 3, 4)))

    def test_boundary_condition(self):
        self.assertFalse(check_smaller((1, 2, 3), (1, 2, 3)))

    def test_edge_case(self):
        self.assertTrue(check_smaller((1, 2, 3), (4, 5, 6)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_smaller((1, 2, 'a'), (1, 2, 3))
