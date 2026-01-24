import unittest
from mbpp_583_code import catalan_number

class TestCatalanNumber(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)

    def test_edge_conditions(self):
        self.assertEqual(catalan_number(-1), 1)  # Negative number should return 1
        self.assertEqual(catalan_number(20), 165580141)  # Max value should return correct result

    def test_complex_cases(self):
        self.assertEqual(catalan_number(5), 42)
        self.assertEqual(catalan_number(10), 16796)
