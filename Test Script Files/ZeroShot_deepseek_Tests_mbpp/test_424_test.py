import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):

    def test_single_tuple(self):
        self.assertEqual(extract_rear((('a', 'b', 'c'))), ['c'])

    def test_multiple_tuples(self):
        self.assertEqual(extract_rear((('a', 'b', 'c'), ('d', 'e', 'f'))), ['c', 'f'])

    def test_empty_tuple(self):
        self.assertEqual(extract_rear(()), [])

    def test_tuple_with_single_element(self):
        self.assertEqual(extract_rear((('a',))), ['a'])

    def test_tuple_with_duplicate_elements(self):
        self.assertEqual(extract_rear((('a', 'b', 'a'))), ['a'])
