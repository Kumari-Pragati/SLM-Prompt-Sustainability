import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_type((1, 1, 1)))
        self.assertTrue(check_type(("a", "a", "a")))

    def test_edge_case(self):
        self.assertFalse(check_type((1, "a", 1)))
        self.assertFalse(check_type(("a", 1, "a")))

    def test_boundary_case(self):
        self.assertTrue(check_type((1, 1)))
        self.assertTrue(check_type(("a", "a")))

    def test_corner_case(self):
        self.assertFalse(check_type((1, 1, "a")))
        self.assertFalse(check_type(("a", 1, 1)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_type([1, 2, 3])
