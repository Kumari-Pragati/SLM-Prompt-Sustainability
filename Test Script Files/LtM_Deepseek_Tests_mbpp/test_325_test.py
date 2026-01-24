import unittest
from mbpp_325_code import get_Min_Squares

class TestGetMinSquares(unittest.TestCase):

    # Test for simple / typical inputs
    def test_simple_inputs(self):
        self.assertEqual(get_Min_Squares(4), 1)
        self.assertEqual(get_Min_Squares(16), 1)
        self.assertEqual(get_Min_Squares(17), 2)
        self.assertEqual(get_Min_Squares(27), 3)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(get_Min_Squares(0), 0)
        self.assertEqual(get_Min_Squares(1), 1)
        self.assertEqual(get_Min_Squares(2), 2)
        self.assertEqual(get_Min_Squares(3), 3)

    # Test for more complex or corner cases
    def test_corner_cases(self):
        self.assertEqual(get_Min_Squares(100), 1)
        self.assertEqual(get_Min_Squares(12), 3)
        self.assertEqual(get_Min_Squares(14), 2)
        self.assertEqual(get_Min_Squares(1000), 1)
