import unittest
from mbpp_460_code import Extract

class TestExtract(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(Extract([(1,), (2, 3), (4, 5, 6)]), [1, 2, 4])

    def test_edge_cases(self):
        self.assertEqual(Extract([]), [])
        self.assertEqual(Extract([(1,)]), [1])
        self.assertEqual(Extract([(1, 2)]), [1])

    def test_complex(self):
        self.assertEqual(Extract([(1,), (2, 3), (4, 5, 6), (7, 8, 9, 10)]), [1, 2, 4, 7])
        self.assertEqual(Extract([(1,), (2, 3, 4), (5, 6, 7)]), [1, 2, 5])
