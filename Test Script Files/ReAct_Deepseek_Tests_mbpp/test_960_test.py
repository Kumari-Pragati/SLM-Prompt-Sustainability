import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfways(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_noOfways(0), 0)
        self.assertEqual(get_noOfways(1), 1)
        self.assertEqual(get_noOfways(2), 2)
        self.assertEqual(get_noOfways(3), 3)
        self.assertEqual(get_noOfways(4), 5)
        self.assertEqual(get_noOfways(5), 8)

    def test_edge_cases(self):
        self.assertEqual(get_noOfways(-1), 0)
        self.assertEqual(get_noOfways(10), 89)

    def test_explicitly_handled_error_cases(self):
        # The function does not handle any error cases, so this test is redundant.
        self.assertEqual(get_noOfways(100), 6765)
