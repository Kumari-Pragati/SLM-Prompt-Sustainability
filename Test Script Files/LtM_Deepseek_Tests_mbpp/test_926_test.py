import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(rencontres_number(3, 2), 2)
        self.assertEqual(rencontres_number(4, 1), 6)

    # Test for edge and boundary conditions
    def test_boundary_conditions(self):
        self.assertEqual(rencontres_number(0, 0), 1)
        self.assertEqual(rencontres_number(1, 0), 0)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(rencontres_number(5, 3), 10)
        self.assertEqual(rencontres_number(6, 2), 15)
