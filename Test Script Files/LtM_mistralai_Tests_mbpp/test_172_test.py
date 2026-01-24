import unittest
from mbpp_172_code import count_occurance

class TestCountOccurance(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(count_occurance('std'), 1)
        self.assertEqual(count_occurance('stdd'), 1)
        self.assertEqual(count_occurance('sstd'), 0)

    def test_edge_case(self):
        self.assertEqual(count_occurance(''), 0)
        self.assertEqual(count_occurance('s'), 0)
        self.assertEqual(count_occurance('st'), 0)
        self.assertEqual(count_occurance('stdt'), 1)
        self.assertEqual(count_occurance('stdst'), 1)
        self.assertEqual(count_occurance('stdstd'), 2)

    def test_complex_case(self):
        self.assertEqual(count_occurance('ststdst'), 2)
        self.assertEqual(count_occurance('stdstdstd'), 3)
        self.assertEqual(count_occurance('stdstdstdstd'), 3)
        self.assertEqual(count_occurance('stdstdstdstdst'), 3)
