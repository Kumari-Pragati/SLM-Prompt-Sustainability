import unittest
from mbpp_504_code import sum_Of_Series

class TestSum_Of_Series(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Of_Series(3), 36)

    def test_edge_case(self):
        self.assertEqual(sum_Of_Series(1), 1)

    def test_edge_case(self):
        self.assertEqual(sum_Of_Series(2), 8)

    def test_edge_case(self):
        self.assertEqual(sum_Of_Series(0), 0)

    def test_edge_case(self):
        self.assertEqual(sum_Of_Series(-1), 0)

    def test_edge_case(self):
        self.assertEqual(sum_Of_Series(5), 225)

    def test_edge_case(self):
        self.assertEqual(sum_Of_Series(10), 3025)
