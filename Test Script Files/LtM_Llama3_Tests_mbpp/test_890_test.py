import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_Extra([1, 2, 3], [1, 2, 4], 3), 2)

    def test_edge1(self):
        self.assertEqual(find_Extra([1, 2, 3], [1, 2, 3], 3), 3)

    def test_edge2(self):
        self.assertEqual(find_Extra([1, 2], [1, 2], 2), 2)

    def test_edge3(self):
        self.assertEqual(find_Extra([], [], 0), 0)

    def test_edge4(self):
        self.assertEqual(find_Extra([1], [1], 1), 1)

    def test_edge5(self):
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5), 5)

    def test_edge6(self):
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 5, 5], 5), 3)

    def test_edge7(self):
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 6], 5), 4)

    def test_edge8(self):
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 7], 5), 4)

    def test_edge9(self):
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 8], 5), 4)

    def test_edge10(self):
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 9], 5), 4)
