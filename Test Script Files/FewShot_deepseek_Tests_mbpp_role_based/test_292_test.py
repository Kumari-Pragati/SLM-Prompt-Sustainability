import unittest
from mbpp_292_code import find

class TestFind(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find(10, 2), 5)

    def test_boundary_condition(self):
        self.assertEqual(find(0, 1), 0)

    def test_edge_case(self):
        self.assertEqual(find(1, 1), 1)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find(10, 0)
