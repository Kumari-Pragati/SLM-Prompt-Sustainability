import unittest
from mbpp_227_code import min_of_three

class TestMinOfThree(unittest.TestCase):

    # Simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)
        self.assertEqual(min_of_three(3, 2, 1), 1)
        self.assertEqual(min_of_three(2, 1, 3), 1)

    # Edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(min_of_three(0, 0, 0), 0)
        self.assertEqual(min_of_three(-1, -1, -1), -1)
        self.assertEqual(min_of_three(1000000, 1000000, 1000000), 1000000)

    # More complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(min_of_three(2.5, 2.5, 3.5), 2.5)
        self.assertEqual(min_of_three(-1000000, 1000000, 0), -1000000)
        self.assertEqual(min_of_three(1, 2, 1), 1)
        self.assertEqual(min_of_three(1, 1, 2), 1)
