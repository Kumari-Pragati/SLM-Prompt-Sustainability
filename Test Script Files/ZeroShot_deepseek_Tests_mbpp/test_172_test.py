import unittest
from mbpp_172_code import count_occurance

class TestCountOccurance(unittest.TestCase):

    def test_count_occurance(self):
        self.assertEqual(count_occurance('sstdd'), 1)
        self.assertEqual(count_occurance('ssttdd'), 1)
        self.assertEqual(count_occurance('sstddsstdd'), 2)
        self.assertEqual(count_occurance('sstddsstddsstdd'), 3)
        self.assertEqual(count_occurance(''), 0)
        self.assertEqual(count_occurance('stddsstddsstdd'), 2)
        self.assertEqual(count_occurance('sstddsstddsstddsstdd'), 3)
        self.assertEqual(count_occurance('sstddsstddsstddsstddsstddsstdd'), 4)
        self.assertEqual(count_occurance('sstddsstddsstddsstddsstddsstddsstddsstdd'), 5)
        self.assertEqual(count_occurance('sstddsstddsstddsstddsstddsstddsstddsstddsstddsstddsstdd'), 6)
