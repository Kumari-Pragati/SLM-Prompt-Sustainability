import unittest
from mbpp_478_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_lowercase('HelloWorld'), 'HW')

    def test_edge_condition_empty_string(self):
        self.assertEqual(remove_lowercase(''), '')

    def test_edge_condition_all_lowercase(self):
        self.assertEqual(remove_lowercase('hello'), '')

    def test_edge_condition_all_uppercase(self):
        self.assertEqual(remove_lowercase('HELLO'), 'HELLO')

    def test_edge_condition_mixed_case(self):
        self.assertEqual(remove_lowercase('HeLLoWorLD'), 'HW')

    def test_complex_input(self):
        self.assertEqual(remove_lowercase('HelloWorld123'), 'HW123')
