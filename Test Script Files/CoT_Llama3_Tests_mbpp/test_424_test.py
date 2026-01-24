import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(extract_rear((('a', 'b'), ('c', 'd'), ('e', 'f'))), ['f', 'd', 'b'])

    def test_empty_input(self):
        self.assertEqual(extract_rear(()), [])

    def test_single_input(self):
        self.assertEqual(extract_rear([('a', 'b')]), ['b'])

    def test_multiple_sublists(self):
        self.assertEqual(extract_rear([('a', 'b'), ('c', 'd'), ('e', 'f'), ('g', 'h')]), ['h', 'd', 'b'])

    def test_single_element_sublist(self):
        self.assertEqual(extract_rear([('a')]), ['a'])

    def test_sublist_with_single_element(self):
        self.assertEqual(extract_rear([('a', 'b', 'c')]), ['c'])

    def test_sublist_with_multiple_elements(self):
        self.assertEqual(extract_rear([('a', 'b', 'c', 'd')]), ['d'])
