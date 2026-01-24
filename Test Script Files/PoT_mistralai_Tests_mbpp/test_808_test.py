import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):
    def test_typical(self):
        self.assertTrue(check_K([1, 2, 3, 4, 5], 5))
        self.assertTrue(check_K(["a", "b", "c", "d", "e"], "e"))
        self.assertTrue(check_K([True, False, True, False, True], True))

    def test_edge_and_boundary(self):
        self.assertFalse(check_K([], 1))
        self.assertFalse(check_K([1], 2))
        self.assertFalse(check_K([1, 2], 3))
        self.assertFalse(check_K([1, 2, 3], 4))
        self.assertFalse(check_K([1, 2, 3], 0))
        self.assertFalse(check_K([], 0))
        self.assertFalse(check_K([1], 0))
        self.assertFalse(check_K([1, 2], "a"))
        self.assertFalse(check_K([True, False], True))
        self.assertFalse(check_K([True, False], False))
