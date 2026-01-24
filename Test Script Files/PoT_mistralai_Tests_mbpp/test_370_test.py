import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(float_sort([('1.5',), ('2.0',), ('3.14',), ('0.0',)]), [('3.14',), ('2.0',), ('1.5',), ('0.0',)])

    def test_edge_case_zero(self):
        self.assertEqual(float_sort([('0.0',),]), [('0.0',)])

    def test_edge_case_negative(self):
        self.assertEqual(float_sort([('-1.5',), ('-2.0',), ('-3.14',), ('-0.0',)]), [('-0.0',), ('-3.14',), ('-2.0',), ('-1.5',)])

    def test_edge_case_empty(self):
        self.assertEqual(float_sort([]), [])

    def test_edge_case_single_item(self):
        self.assertEqual(float_sort([('1.0',)]), [('1.0',)])

    def test_edge_case_string(self):
        self.assertEqual(float_sort([('a',)]), [('a',)])

    def test_edge_case_invalid_float(self):
        self.assertEqual(float_sort([('x',)]), [('x',)])
