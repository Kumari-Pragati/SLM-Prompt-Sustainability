import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(extract_rear((1, 2, 3)), [3])
        self.assertListEqual(extract_rear((4,)), [4])
        self.assertListEqual(extract_rear(('a', 'b', 'c')), ['c'])

    def test_edge_cases(self):
        self.assertListEqual(extract_rear((1,)), [])
        self.assertListEqual(extract_rear(()), [])
        self.assertListEqual(extract_rear((1, 2)), [2])
        self.assertListEqual(extract_rear(('a',)), ['a'])

    def test_complex_input(self):
        self.assertListEqual(extract_rear((1, 2, 3, 4)), [4])
        self.assertListEqual(extract_rear((1, 2, 3, 4, 5)), [5])
        self.assertListEqual(extract_rear(('a', 'b', 'c', 'd')), ['d'])
        self.assertListEqual(extract_rear(('a', 'b', 'c', 'd', 'e')), ['e'])
