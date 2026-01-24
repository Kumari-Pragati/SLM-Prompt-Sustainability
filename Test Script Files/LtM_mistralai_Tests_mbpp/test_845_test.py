import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_Digits(1), 1)
        self.assertEqual(find_Digits(10), 2)
        self.assertEqual(find_Digits(100), 3)
        self.assertEqual(find_Digits(1000), 4)

    def test_edge_conditions(self):
        self.assertEqual(find_Digits(0), 0)
        self.assertEqual(find_Digits(1.0), 1)
        self.assertEqual(find_Digits(math.e), 1)
        self.assertEqual(find_Digits(math.pi), 2)

    def test_complex_inputs(self):
        self.assertEqual(find_Digits(math.e ** 10), 10)
        self.assertEqual(find_Digits(math.pi ** 10), 20)
        self.assertEqual(find_Digits(math.e ** 100), 101)
        self.assertEqual(find_Digits(math.pi ** 100), 201)
