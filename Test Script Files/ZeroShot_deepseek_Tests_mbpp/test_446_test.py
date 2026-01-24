import unittest
from mbpp_446_code import Counter
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):

    def test_count_Occurrence(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['a', 'b', 'c']), 3)
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['a', 'b']), 2)
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['d', 'e']), 0)
        self.assertEqual(count_Occurrence((), ['a', 'b', 'c']), 0)
        self.assertEqual(count_Occurrence(('a', 'a', 'a'), ['a']), 3)
