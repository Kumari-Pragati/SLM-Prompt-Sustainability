import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(two_unique_nums([1, 2, 3, 2, 1]), [3])
        self.assertEqual(two_unique_nums([5, 5, 5, 5, 5]), [])
        self.assertEqual(two_unique_nums([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_conditions(self):
        self.assertEqual(two_unique_nums([]), [])
        self.assertEqual(two_unique_nums([1]), [1])
        self.assertEqual(two_unique_nums([1, 1]), [])

    def test_complex_cases(self):
        self.assertEqual(two_unique_nums([1, 2, 2, 3, 3]), [1])
        self.assertEqual(two_unique_nums([1, 1, 2, 2, 3]), [3])
        self.assertEqual(two_unique_nums([1, 2, 3, 4, 4]), [1, 2, 3])
