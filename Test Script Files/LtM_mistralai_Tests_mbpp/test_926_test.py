import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(rencontres_number(1, 0), 1)
        self.assertEqual(rencontres_number(2, 1), 2)
        self.assertEqual(rencontres_number(3, 2), 6)

    def test_edge_inputs(self):
        self.assertEqual(rencontres_number(0, 0), 1)
        self.assertEqual(rencontres_number(1, 1), 0)
        self.assertEqual(rencontres_number(2, 2), 3)

    def test_boundary_inputs(self):
        self.assertEqual(rencontres_number(1, 2), 0)
        self.assertEqual(rencontres_number(2, 3), 0)
        self.assertEqual(rencontres_number(3, 4), 0)

    def test_complex_inputs(self):
        self.assertEqual(rencontres_number(5, 3), 20)
        self.assertEqual(rencontres_number(6, 4), 45)
        self.assertEqual(rencontres_number(7, 5), 120)
