import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4]), [1, 1])

    def test_edge_boundary_conditions(self):
        self.assertEqual(diff_consecutivenums([1]), [])
        self.assertEqual(diff_consecutivenums([]), [])
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4, 5]), [1, 1, 1])

    def test_more_complex_cases(self):
        self.assertEqual(diff_consecutivenums([10, 20, 30, 40, 50]), [10, 10, 10])
        self.assertEqual(diff_consecutivenums([1, 3, 5, 7, 9]), [2, 2, 2])
