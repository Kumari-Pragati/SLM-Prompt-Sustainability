import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(check_greater((1, 2, 3), (2, 3, 4)))
        self.assertTrue(check_greater((5, 4, 3), (5, 6, 7)))

    def test_edge_cases(self):
        self.assertTrue(check_greater((0, 0, 0), (1, 1, 1)))
        self.assertTrue(check_greater((-1, -1, -1), (0, 0, 0)))
        self.assertTrue(check_greater((1, 1, 1), (0, 0, 0)))
        self.assertTrue(check_greater((1, 2, 3), (1, 2, 3)))
        self.assertTrue(check_greater((1, 2, 3), (1, 2, 4)))
        self.assertTrue(check_greater((1, 2, 3), (1, 3, 4)))
        self.assertTrue(check_greater((1, 2, 3), (2, 3, 4)))
        self.assertTrue(check_greater((1, 2, 3), (2, 3, 5)))
        self.assertTrue(check_greater((1, 2, 3), (3, 4, 5)))

    def test_empty_inputs(self):
        self.assertFalse(check_greater((), (1, 2, 3)))
        self.assertFalse(check_greater((1, 2), (1, 2, 3)))
        self.assertFalse(check_greater((1, 2, 3), ()))
        self.assertFalse(check_greater((1, 2, 3), (1, 2)))
