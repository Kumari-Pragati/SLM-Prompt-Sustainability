import unittest
from mbpp_555_code import difference

class TestDifference(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(difference(1), 1)
        self.assertEqual(difference(2), 21)
        self.assertEqual(difference(3), 111)

    def test_edge_conditions(self):
        self.assertEqual(difference(0), 0)

    def test_complex_cases(self):
        self.assertEqual(difference(10), 4950)
        self.assertEqual(difference(20), 199500)
