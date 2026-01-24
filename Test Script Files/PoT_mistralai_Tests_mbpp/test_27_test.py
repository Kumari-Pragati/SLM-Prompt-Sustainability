import unittest
from mbpp_27_code import remove

class TestRemoveFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(remove(['abc123', 'def456', 'ghi789']), ['abc', 'def', 'ghi'])

    def test_edge_case_empty_list(self):
        self.assertListEqual(remove([]), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(remove(['abc']), [''])

    def test_edge_case_only_numbers(self):
        self.assertListEqual(remove([123, 456, 789]), [])

    def test_corner_case_mixed_case(self):
        self.assertListEqual(remove(['AbC123', 'dEf456', 'gHi789']), ['AbC', 'dEf', 'gHi'])
