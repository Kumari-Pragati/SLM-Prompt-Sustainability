import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(count_no(2, 3, 1, 5), 4)
        self.assertEqual(count_no(3, 2, 1, 5), 5)
        self.assertEqual(count_no(5, 1, 1, 5), 5)
        self.assertEqual(count_no(7, 3, 1, 10), 10)

    def test_edge_and_boundary(self):
        self.assertEqual(count_no(2, 3, 0, 5), 0)
        self.assertEqual(count_no(2, 3, 6, 10), 6)
        self.assertEqual(count_no(2, 3, 1, 0), 0)
        self.assertEqual(count_no(2, 3, 1, 1), 1)
        self.assertEqual(count_no(2, 3, 1, 2), 2)
        self.assertEqual(count_no(2, 3, 1, 3), 3)
        self.assertEqual(count_no(2, 3, 1, 4), 4)
