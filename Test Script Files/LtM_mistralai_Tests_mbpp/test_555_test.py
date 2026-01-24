import unittest
from mbpp_555_code import difference

class TestDifference(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(difference(1), 0)
        self.assertEqual(difference(2), 2)
        self.assertEqual(difference(3), 6)
        self.assertEqual(difference(4), 12)
        self.assertEqual(difference(5), 20)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(difference(0), 0)
        self.assertEqual(difference(1000), 500500)
        self.assertEqual(difference(-1), -1)

    def test_complex_cases(self):
        self.assertEqual(difference(10), 55)
        self.assertEqual(difference(20), 190)
        self.assertEqual(difference(30), 495)
        self.assertEqual(difference(40), 980)
        self.assertEqual(difference(50), 1725)
