import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(compute_Last_Digit(1, 1), 1)
        self.assertEqual(compute_Last_Digit(2, 2), 1)
        self.assertEqual(compute_Last_Digit(3, 3), 1)
        self.assertEqual(compute_Last_Digit(4, 4), 1)
        self.assertEqual(compute_Last_Digit(5, 5), 1)

    def test_edge_and_boundary(self):
        self.assertEqual(compute_Last_Digit(0, 1), 1)
        self.assertEqual(compute_Last_Digit(1, 0), 1)
        self.assertEqual(compute_Last_Digit(1, 2), 0)
        self.assertEqual(compute_Last_Digit(2, 1), 0)
        self.assertEqual(compute_Last_Digit(10, 11), 1)
        self.assertEqual(compute_Last_Digit(11, 10), 1)
        self.assertEqual(compute_Last_Digit(100, 101), 1)
        self.assertEqual(compute_Last_Digit(101, 100), 1)
        self.assertEqual(compute_Last_Digit(1000, 1001), 1)
        self.assertEqual(compute_Last_Digit(1001, 1000), 1)

    def test_complex(self):
        self.assertEqual(compute_Last_Digit(1, 10), 1)
        self.assertEqual(compute_Last_Digit(10, 1), 1)
        self.assertEqual(compute_Last_Digit(10, 20), 1)
        self.assertEqual(compute_Last_Digit(20, 10), 1)
        self.assertEqual(compute_Last_Digit(10, 30), 0)
        self.assertEqual(compute_Last_Digit(30, 10), 0)
        self.assertEqual(compute_Last_Digit(10, 40), 1)
        self.assertEqual(compute_Last_Digit(40, 10), 1)
        self.assertEqual(compute_Last_Digit(10, 50), 0)
        self.assertEqual(compute_Last_Digit(50, 10), 0)
        self.assertEqual(compute_Last_Digit(10, 60), 1)
        self.assertEqual(compute_Last_Digit(60, 10), 1)
        self.assertEqual(compute_Last_Digit(10, 70), 0)
        self.assertEqual(compute_Last_Digit(70, 10), 0)
        self.assertEqual(compute_Last_Digit(10, 80), 1)
        self.assertEqual(compute_Last_Digit(80, 10), 1)
        self.assertEqual(compute_Last_Digit(10, 90), 0)
        self.assertEqual(compute_Last_Digit(90, 10), 0)
