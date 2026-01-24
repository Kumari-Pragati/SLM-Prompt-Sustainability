import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):

    def test_simple_tuple(self):
        self.assertEqual(extract_rear(([1, 2, 3], [4, 5, 6])), ['3', '6'])

    def test_empty_tuple(self):
        self.assertEqual(extract_rear(()), [])

    def test_single_element_tuple(self):
        self.assertEqual(extract_rear(([1],)), ['1'])

    def test_mixed_types_tuple(self):
        self.assertEqual(extract_rear(([1, 'a'], [2, 'b'])), ['1', '2'])

    def test_tuple_with_empty_lists(self):
        self.assertEqual(extract_rear(([], []), []))

    def test_tuple_with_one_empty_list(self):
        self.assertEqual(extract_rear(([], [1, 2, 3]), ['3']))
