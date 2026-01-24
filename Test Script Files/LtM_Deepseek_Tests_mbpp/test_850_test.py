import unittest
from mbpp_850_code import is_triangleexists

class TestIsTriangleExists(unittest.TestCase):

    # Test for typical inputs
    def test_typical_inputs(self):
        self.assertTrue(is_triangleexists(60, 60, 60))
        self.assertTrue(is_triangleexists(1, 1, 178))

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertFalse(is_triangleexists(0, 0, 0))
        self.assertFalse(is_triangleexists(1, 1, 181))
        self.assertFalse(is_triangleexists(1, 181, 1))
        self.assertFalse(is_triangleexists(181, 1, 1))

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertFalse(is_triangleexists(90, 90, 0))
        self.assertFalse(is_triangleexists(90, 0, 90))
        self.assertFalse(is_triangleexists(0, 90, 90))
        self.assertFalse(is_triangleexists(1, 2, 3))
        self.assertFalse(is_triangleexists(100, 70, 10))
