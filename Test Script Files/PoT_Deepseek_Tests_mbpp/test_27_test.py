import unittest
from mbpp_27_code import remove

class TestRemove(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(remove(['abc123', 'def456']), ['abc', 'def'])
        self.assertEqual(remove(['123', '456']), ['', ''])

    def test_edge_cases(self):
        self.assertEqual(remove(['']), [''])
        self.assertEqual(remove([]), [])

    def test_corner_cases(self):
        self.assertEqual(remove(['1', '2', '3']), ['', '', ''])
        self.assertEqual(remove(['1234567890']), [''])
