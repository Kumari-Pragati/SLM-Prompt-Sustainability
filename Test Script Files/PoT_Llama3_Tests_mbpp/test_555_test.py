import unittest
from mbpp_555_code import difference

class TestDifference(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(difference(3), 6)

    def test_edge(self):
        self.assertEqual(difference(1), 0)
        self.assertEqual(difference(2), 2)

    def test_edge2(self):
        self.assertRaises(TypeError, difference, 'a')

    def test_edge3(self):
        self.assertEqual(difference(-1), 0)
        self.assertEqual(difference(0), 0)

    def test_edge4(self):
        self.assertEqual(difference(1), 0)
        self.assertEqual(difference(2), 2)

    def test_edge5(self):
        self.assertEqual(difference(3), 6)
