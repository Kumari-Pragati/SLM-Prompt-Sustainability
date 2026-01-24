import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2)))
        self.assertFalse(check_subset((1, 2, 3), (4, 5)))

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertTrue(check_subset((), ()))
        self.assertFalse(check_subset((1,), ()))
        self.assertTrue(check_subset((1, 2, 3), (1, 2, 3)))

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertTrue(check_subset((1, 2, 2, 3), (2, 2)))
        self.assertFalse(check_subset((1, 2, 3), (1, 2, 3, 4)))
