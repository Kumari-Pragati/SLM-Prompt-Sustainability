import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(first_odd([2, 4, 6]), -1)
        self.assertEqual(first_odd([1]), 1)
        self.assertEqual(first_odd([2, 3, 4]), 3)

    def test_edge_conditions(self):
        self.assertEqual(first_odd([]), -1)
        self.assertEqual(first_odd([2, 4, 6, 8, 10]), -1)
        self.assertEqual(first_odd([2, 4, 6, 8, 10, 11]), 11)

    def test_complex_cases(self):
        self.assertEqual(first_odd([2, 4, 6, 8, 10, 11, 13]), 11)
        self.assertEqual(first_odd([2, 4, 6, 8, 10, 12, 14]), -1)
