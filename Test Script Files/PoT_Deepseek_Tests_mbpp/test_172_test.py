import unittest
from mbpp_172_code import count_occurance

class TestCountOccurance(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_occurance('sdt'), 1)
        self.assertEqual(count_occurance('sstdt'), 1)
        self.assertEqual(count_occurance('sdtstdt'), 2)
        self.assertEqual(count_occurance('sdtstdtstdt'), 3)

    def test_edge_cases(self):
        self.assertEqual(count_occurance(''), 0)
        self.assertEqual(count_occurance('s'), 0)
        self.assertEqual(count_occurance('t'), 0)
        self.assertEqual(count_occurance('d'), 0)
        self.assertEqual(count_occurance('st'), 0)
        self.assertEqual(count_occurance('sd'), 0)
        self.assertEqual(count_occurance('td'), 0)
        self.assertEqual(count_occurance('sdtd'), 0)
        self.assertEqual(count_occurance('tsd'), 0)

    def test_corner_cases(self):
        self.assertEqual(count_occurance('sstdtstdtstdt'), 3)
        self.assertEqual(count_occurance('sdtstdtstdtstdt'), 4)
        self.assertEqual(count_occurance('sdtstdtstdtstdtstdt'), 5)
        self.assertEqual(count_occurance('sdtstdtstdtstdtstdtstdt'), 6)
