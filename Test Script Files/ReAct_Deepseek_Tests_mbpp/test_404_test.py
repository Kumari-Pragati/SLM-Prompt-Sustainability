import unittest
from mbpp_404_code import minimum

class TestMinimumFunction(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(minimum(1, 2), 1)
        self.assertEqual(minimum(3, 2), 2)
        self.assertEqual(minimum(-1, -2), -2)
        self.assertEqual(minimum(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(minimum(float('inf'), float('inf')), float('inf'))
        self.assertEqual(minimum(float('-inf'), float('-inf')), float('-inf'))
        self.assertEqual(minimum(float('inf'), float('-inf')), float('-inf'))

    def test_explicitly_handled_error_cases(self):
        # Since the function does not handle any error cases, this test is redundant.
        pass
