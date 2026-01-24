import unittest
from mbpp_797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(sum_in_Range(1, 5), 14)
        self.assertEqual(sum_in_Range(7, 10), 19)

    # Test for edge and boundary conditions
    def test_boundary_conditions(self):
        self.assertEqual(sum_in_Range(1, 1), 1)
        self.assertEqual(sum_in_Range(1, 100), 1684)
        self.assertEqual(sum_in_Range(100, 100), 0)
        self.assertEqual(sum_in_Range(100, 200), 4950)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(sum_in_Range(1, 1000), 1501500)
        self.assertEqual(sum_in_Range(1000, 2000), 99001500)
