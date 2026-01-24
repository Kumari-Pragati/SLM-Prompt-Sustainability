import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(min_Swaps('0101', '1010'), 1)
        self.assertEqual(min_Swaps('1110', '0001'), 2)

    # Test for edge and boundary conditions
    def test_edge_and_boundary_conditions(self):
        self.assertEqual(min_Swaps('0000', '1111'), 0)
        self.assertEqual(min_Swaps('0000', '0000'), 0)
        self.assertEqual(min_Swaps('1111', '1111'), -1)

    # Test for more complex or corner cases
    def test_more_complex_cases(self):
        self.assertEqual(min_Swaps('010101', '101010'), 1)
        self.assertEqual(min_Swaps('110011', '001100'), 2)
        self.assertEqual(min_Swaps('001100', '110011'), 2)
        self.assertEqual(min_Swaps('000000', '111111'), -1)
