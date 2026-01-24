import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_rear(([1, 2, 3], [4, 5, 6])), ['3', '6'])

    def test_empty_tuple(self):
        self.assertEqual(extract_rear(()), [])

    def test_single_element_tuple(self):
        self.assertEqual(extract_rear(([1],)), ['1'])

    def test_large_tuple(self):
        self.assertEqual(extract_rear(([1, 2, 3] * 1000, [4, 5, 6] * 1000)), ['3'] * 1000)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            extract_rear(([1, 2, 3], 'abc'))

    def test_non_list_elements(self):
        with self.assertRaises(TypeError):
            extract_rear((1, 2, 3))
