import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):

    def test_typical_case(self):
        tuplex = (1, 2, 3)
        tuple1 = (1,)
        self.assertTrue(check_tuplex(tuplex, tuple1))

    def test_typical_case_2(self):
        tuplex = ('a', 'b', 'c')
        tuple1 = ('a',)
        self.assertTrue(check_tuplex(tuplex, tuple1))

    def test_edge_case_empty_tuples(self):
        tuplex = ()
        tuple1 = ()
        self.assertFalse(check_tuplex(tuplex, tuple1))

    def test_edge_case_single_element_tuples(self):
        tuplex = (1,)
        tuple1 = (1,)
        self.assertTrue(check_tuplex(tuplex, tuple1))

    def test_edge_case_tuple1_not_in_tuplex(self):
        tuplex = (1, 2, 3)
        tuple1 = (4,)
        self.assertFalse(check_tuplex(tuplex, tuple1))

    def test_edge_case_tuple1_larger_than_tuplex(self):
        tuplex = (1, 2)
        tuple1 = (1, 2, 3)
        self.assertFalse(check_tuplex(tuplex, tuple1))
