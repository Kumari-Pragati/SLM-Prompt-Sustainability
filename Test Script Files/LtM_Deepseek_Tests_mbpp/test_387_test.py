import unittest
from mbpp_387_code import even_or_odd

class TestEvenOrOdd(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(even_or_odd('1'), 'Odd')
        self.assertEqual(even_or_odd('2'), 'Even')
        self.assertEqual(even_or_odd('3'), 'Odd')
        self.assertEqual(even_or_odd('4'), 'Even')
        self.assertEqual(even_or_odd('5'), 'Odd')
        self.assertEqual(even_or_odd('6'), 'Even')
        self.assertEqual(even_or_odd('7'), 'Odd')
        self.assertEqual(even_or_odd('8'), 'Even')
        self.assertEqual(even_or_odd('9'), 'Odd')
        self.assertEqual(even_or_odd('0'), 'Even')

    def test_edge_conditions(self):
        self.assertEqual(even_or_odd('A'), 'Even')
        self.assertEqual(even_or_odd('C'), 'Even')
        self.assertEqual(even_or_odd('E'), 'Even')
        self.assertEqual(even_or_odd('0'), 'Even')
        self.assertEqual(even_or_odd('2'), 'Even')
        self.assertEqual(even_or_odd('4'), 'Even')
        self.assertEqual(even_or_odd('6'), 'Even')
        self.assertEqual(even_or_odd('8'), 'Even')

    def test_complex_cases(self):
        self.assertEqual(even_or_odd('1A'), 'Odd')
        self.assertEqual(even_or_odd('2C'), 'Even')
        self.assertEqual(even_or_odd('3E'), 'Odd')
        self.assertEqual(even_or_odd('40'), 'Even')
        self.assertEqual(even_or_odd('52'), 'Odd')
        self.assertEqual(even_or_odd('64'), 'Even')
        self.assertEqual(even_or_odd('76'), 'Odd')
        self.assertEqual(even_or_odd('88'), 'Even')
        self.assertEqual(even_or_odd('9A'), 'Odd')
