import unittest
from mbpp_281_code import all_unique

class TestAllUnique(unittest.TestCase):
    def test_typical_input(self):
        self.assertTrue(all_unique([1, 2, 3, 4, 5]))
        self.assertTrue(all_unique(["a", "b", "c", "d", "e"]))
        self.assertTrue(all_unique([1.0, 2.0, 3.0, 4.0, 5.0]))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(all_unique([]))
        self.assertTrue(all_unique([1]))
        self.assertTrue(all_unique([1, 1]))
        self.assertFalse(all_unique([1, 1, 2, 1]))
        self.assertFalse(all_unique([1, 1, 1, 2, 3, 1, 1]))
        self.assertFalse(all_unique([1, 1, 1, 2, 3, 1, 1, 1]))
        self.assertFalse(all_unique([1, 1, 1, 2, 3, 1, 1, 1, 1]))

    def test_special_cases(self):
        self.assertFalse(all_unique([float('nan'), float('nan'), 3]))
        self.assertFalse(all_unique([True, True, False]))
        self.assertFalse(all_unique([None, None, None]))
        self.assertFalse(all_unique([set(), set()]))
