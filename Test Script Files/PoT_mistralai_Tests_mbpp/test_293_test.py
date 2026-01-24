import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(otherside_rightangle(3, 4), 5)

    def test_edge_case_zero(self):
        self.assertEqual(otherside_rightangle(0, 4), 0)
        self.assertEqual(otherside_rightangle(3, 0), 0)

    def test_edge_case_one(self):
        self.assertEqual(otherside_rightangle(1, 1), 2)

    def test_boundary_case_negative(self):
        self.assertEqual(otherside_rightangle(-3, 4), 5)
        self.assertEqual(otherside_rightangle(3, -4), 5)

    def test_boundary_case_large(self):
        self.assertEqual(otherside_rightangle(1e6, 1e6), 1.4142135623730951)
