import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(zigzag(3, 2), 3)
        self.assertEqual(zigzag(4, 3), 6)
        self.assertEqual(zigzag(2, 1), 2)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(zigzag(0, 0), 1)
        self.assertEqual(zigzag(0, 1), 0)
        self.assertEqual(zigzag(1, 0), 1)
        self.assertEqual(zigzag(1, 1), 1)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(zigzag(5, 3), 10)
        self.assertEqual(zigzag(6, 4), 15)
        self.assertEqual(zigzag(7, 5), 21)
