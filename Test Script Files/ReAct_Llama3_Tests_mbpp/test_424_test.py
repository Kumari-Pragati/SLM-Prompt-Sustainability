import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):
    def test_single_sub(self):
        self.assertEqual(extract_rear((['a', 'b', 'c'])), ['c'])

    def test_multiple_sub(self):
        self.assertEqual(extract_rear([('a', 'b', 'c'), ('d', 'e', 'f')]), ['c', 'f'])

    def test_empty_sub(self):
        self.assertEqual(extract_rear([]), [])

    def test_single_sub_empty(self):
        self.assertEqual(extract_rear([('a', 'b', 'c'), ()]), ['c'])

    def test_single_sub_single_element(self):
        self.assertEqual(extract_rear([('a', 'b', 'c'), ('d')]), ['c'])

    def test_single_sub_multiple_elements(self):
        self.assertEqual(extract_rear([('a', 'b', 'c'), ('d', 'e', 'f', 'g')]), ['c', 'g'])
