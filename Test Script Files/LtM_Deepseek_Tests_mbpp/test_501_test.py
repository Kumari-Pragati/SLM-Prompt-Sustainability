import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(num_comm_div(10, 20), 6)
        self.assertEqual(num_comm_div(30, 45), 9)

    # Test for edge and boundary conditions
    def test_edge_and_boundary_conditions(self):
        self.assertEqual(num_comm_div(0, 20), 2)
        self.assertEqual(num_comm_div(1, 1), 1)
        self.assertEqual(num_comm_div(1000000000, 1000000000), 1)

    # Test for more complex or corner cases
    def test_more_complex_cases(self):
        self.assertEqual(num_comm_div(21, 45), 6)
        self.assertEqual(num_comm_div(100, 200), 10)
        self.assertEqual(num_comm_div(1000000001, 1000000002), 2)
