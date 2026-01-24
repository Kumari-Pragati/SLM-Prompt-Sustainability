import unittest
from mbpp_172_code import count_occurance

class TestCountOccurance(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_occurance('start'), 1)
        self.assertEqual(count_occurance('study'), 1)
        self.assertEqual(count_occurance('studies'), 1)
        self.assertEqual(count_occurance('studied'), 0)

    def test_edge_case(self):
        self.assertEqual(count_occurance(''), 0)
        self.assertEqual(count_occurance('s'), 0)
        self.assertEqual(count_occurance('std'), 0)
        self.assertEqual(count_occurance('st'), 0)
        self.assertEqual(count_occurance('stt'), 0)
        self.assertEqual(count_occurance('stdd'), 1)
        self.assertEqual(count_occurance('stddd'), 1)
        self.assertEqual(count_occurance('stdddd'), 1)
