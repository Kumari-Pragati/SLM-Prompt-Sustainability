import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertTrue(check_smaller((1, 2, 3), (2, 3, 4)))
        self.assertFalse(check_smaller((3, 2, 1), (2, 3, 1)))

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertTrue(check_smaller((1, 1, 1), (2, 2, 2)))
        self.assertFalse(check_smaller((2, 2, 2), (1, 1, 1)))
        self.assertTrue(check_smaller((1, 2, 3), (1, 2, 3)))

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertFalse(check_smaller((1, 2, 3), (1, 2, 2)))
        self.assertTrue(check_smaller((1, 2, 3), (2, 2, 3)))
        self.assertFalse(check_smaller((1, 2, 3), (1, 2, 4)))
