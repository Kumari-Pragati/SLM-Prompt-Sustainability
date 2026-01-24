import unittest
from mbpp_281_code import all_unique

class TestAllUnique(unittest.TestCase):

    def test_simple_list(self):
        self.assertTrue(all_unique([1, 2, 3]))
        self.assertTrue(all_unique([4, 5, 6]))

    def test_edge_cases(self):
        self.assertFalse(all_unique([1, 1, 2, 3]))
        self.assertFalse(all_unique([1, 1, 1, 2, 3]))
        self.assertFalse(all_unique([1, 1, 1, 1, 2, 3]))
        self.assertTrue(all_unique([]))
        self.assertTrue(all_unique([1]))

    def test_boundary_cases(self):
        self.assertTrue(all_unique([-100, -99, -98]))
        self.assertTrue(all_unique([99, 100, 101]))
        self.assertFalse(all_unique([-100, -99, -99]))
        self.assertFalse(all_unique([100, 100, 101]))

    def test_complex_cases(self):
        self.assertTrue(all_unique([0.1, 0.2, 0.3]))
        self.assertFalse(all_unique([0.1, 0.1, 0.2]))
        self.assertTrue(all_unique([1j, 2j, 3j]))
        self.assertFalse(all_unique([1j, 1j, 2j]))
        self.assertFalse(all_unique([None, None, 1]))
