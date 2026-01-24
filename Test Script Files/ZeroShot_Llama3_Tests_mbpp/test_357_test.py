import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):

    def test_find_max(self):
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)
        self.assertEqual(find_max([[10, 20, 30], [40, 50, 60], [70, 80, 90]]), 90)
        self.assertEqual(find_max([[100, 200, 300], [400, 500, 600], [700, 800, 900]]), 900)
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6]]), 6)
        self.assertEqual(find_max([[10, 20, 30], [40, 50, 60]]), 60)
        self.assertEqual(find_max([[100, 200, 300], [400, 500, 600]]), 600)
        self.assertEqual(find_max([[1, 2, 3]]), 3)
        self.assertEqual(find_max([[10, 20, 30]]), 30)
        self.assertEqual(find_max([[100, 200, 300]]), 300)
        self.assertEqual(find_max([[1]]), 1)
        self.assertEqual(find_max([[10]]), 10)
        self.assertEqual(find_max([[100]]), 100)
        self.assertEqual(find_max([]), None)
        self.assertEqual(find_max([[]]), None)
