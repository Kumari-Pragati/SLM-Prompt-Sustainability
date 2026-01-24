import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_tuplex(('a', 'b', 'c'), ('b',)))

    def test_edge_condition(self):
        self.assertTrue(check_tuplex((), ()))

    def test_boundary_condition(self):
        self.assertFalse(check_tuplex(('a', 'b', 'c'), ('d',)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_tuplex(123, 'b')
