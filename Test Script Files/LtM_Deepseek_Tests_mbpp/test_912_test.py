import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(lobb_num(3, 2), 10.0)
        self.assertEqual(lobb_num(4, 3), 45.0)

    # Test for edge and boundary conditions
    def test_boundary_conditions(self):
        self.assertEqual(lobb_num(0, 0), 1.0)
        self.assertEqual(lobb_num(1, 0), 2.0)
        self.assertEqual(lobb_num(0, 1), 1.0)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(lobb_num(5, 2), 110.0)
        self.assertEqual(lobb_num(6, 3), 455.0)
