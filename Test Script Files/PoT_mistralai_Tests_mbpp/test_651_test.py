import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):
    def test_typical(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2)))
        self.assertTrue(check_subset((1, 2, 3), (1, 2, 3)))
        self.assertTrue(check_subset(set((1, 2, 3)), set((1, 2, 3))))

    def test_edge_and_boundary(self):
        self.assertFalse(check_subset((1, 2, 3), (1, 2, 4)))
        self.assertFalse(check_subset((1, 2, 3), set()))
        self.assertFalse(check_subset(set(), (1, 2, 3)))
        self.assertFalse(check_subset(set(), set()))
        self.assertTrue(check_subset(set(), set((1,))))
