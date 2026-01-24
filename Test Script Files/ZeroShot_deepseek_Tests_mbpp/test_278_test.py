import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(count_first_elements(('a',)), 1)

    def test_multiple_elements(self):
        self.assertEqual(count_first_elements(('a', 'b', 'c')), 1)

    def test_mixed_elements(self):
        self.assertEqual(count_first_elements(('a', 1, 2.0)), 1)

    def test_nested_tuples(self):
        self.assertEqual(count_first_elements(('a', ('b', 'c'))), 1)

    def test_empty_tuple(self):
        self.assertEqual(count_first_elements(()), 0)

    def test_all_tuples(self):
        self.assertEqual(count_first_elements((('a',), ('b',), ('c',))), 1)

    def test_mixed_types(self):
        self.assertEqual(count_first_elements((1, 'a', 2.0)), 1)
