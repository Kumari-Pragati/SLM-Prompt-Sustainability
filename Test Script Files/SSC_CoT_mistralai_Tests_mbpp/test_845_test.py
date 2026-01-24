import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertEqual(find_Digits(1), 1)
        self.assertEqual(find_Digits(10), 1)
        self.assertEqual(find_Digits(100), 2)
        self.assertEqual(find_Digits(1000), 3)
        self.assertEqual(find_Digits(10_000), 4)
        self.assertEqual(find_Digits(100_000), 5)
        self.assertEqual(find_Digits(1_000_000), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Digits(0), 0)
        self.assertEqual(find_Digits(1.0), 1)
        self.assertEqual(find_Digits(math.e), 1)
        self.assertEqual(find_Digits(math.pi), 1)
        self.assertEqual(find_Digits(math.e ** 10), 10)
        self.assertEqual(find_Digits(math.pi ** 10), 10)
        self.assertEqual(find_Digits(math.e ** 100), 100)
        self.assertEqual(find_Digits(math.pi ** 100), 100)
