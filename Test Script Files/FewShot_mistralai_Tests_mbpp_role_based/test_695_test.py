import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertFalse(check_greater((1, 2), (2, 3)))
        self.assertFalse(check_greater((3, 2), (2, 1)))
        self.assertTrue(check_greater((1, 2), (1, 3)))
        self.assertTrue(check_greater((3, 2), (3, 1)))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(check_greater((0, 0), (1, 1)))
        self.assertFalse(check_greater((1, 0), (1, 1)))
        self.assertFalse(check_greater((0, 1), (1, 1)))
        self.assertFalse(check_greater((1, 0), (0, 1)))
        self.assertFalse(check_greater((0, 0), (0, 0)))
