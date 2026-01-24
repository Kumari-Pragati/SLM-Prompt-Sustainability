import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_Occurrence([1, 2, 3], [1, 2, 3, 4]), 3)
        self.assertEqual(count_Occurrence([1, 'a', 3], [1, 'a', 3, 'a']), 3)

    def test_edge_and_boundary(self):
        self.assertEqual(count_Occurrence([], []), 0)
        self.assertEqual(count_Occurrence([1], [1, 2]), 1)
        self.assertEqual(count_Occurrence([1, 2], [1, 2, 3]), 2)
        self.assertEqual(count_Occurrence([1, 2], [1, 3]), 0)
        self.assertEqual(count_Occurrence([1, 2], []), 0)

    def test_complex(self):
        self.assertEqual(count_Occurrence([1, 2, 1, 3, 2, 1], [1, 2, 3]), 3)
        self.assertEqual(count_Occurrence([1, 2, 1, 'a', 3, 2, 1], [1, 2, 3, 'a']), 3)
