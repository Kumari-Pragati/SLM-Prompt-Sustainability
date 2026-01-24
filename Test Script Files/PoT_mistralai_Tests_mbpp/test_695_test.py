import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):
    def test_typical_case(self):
        self.assertFalse(check_greater((1, 2, 3), (2, 3, 4)))
        self.assertFalse(check_greater((3, 2, 1), (2, 3, 4)))
        self.assertFalse(check_greater((2, 3, 4), (1, 2, 3)))

    def test_edge_case(self):
        self.assertTrue(check_greater((0, 0, 0), (1, 1, 1)))
        self.assertTrue(check_greater((-1, -1, -1), (0, 0, 0)))
        self.assertTrue(check_greater((0, 0, 0), (-1, -1, -1)))

    def test_boundary_case(self):
        self.assertFalse(check_greater((1, 1, 1), (2, 2, 2)))
        self.assertFalse(check_greater((-1, -1, -1), (-2, -2, -2)))
        self.assertTrue(check_greater((-1, -1), (0, 0)))
        self.assertTrue(check_greater((0, 0), (1, 1)))
