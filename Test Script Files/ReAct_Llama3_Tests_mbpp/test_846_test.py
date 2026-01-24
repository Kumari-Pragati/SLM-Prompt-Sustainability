import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):

    def test_typical_case(self):
        arr = [10, 20, 30, 40, 50]
        dep = [40, 50, 60, 70, 80]
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 3)

    def test_edge_case1(self):
        arr = [10, 20, 30]
        dep = [30, 40, 50]
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 2)

    def test_edge_case2(self):
        arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        dep = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 1)

    def test_edge_case3(self):
        arr = [10, 20, 30, 40, 50]
        dep = [50, 60, 70, 80, 90]
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 2)

    def test_edge_case4(self):
        arr = [10, 20, 30, 40, 50]
        dep = [10, 20, 30, 40, 50]
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 1)

    def test_edge_case5(self):
        arr = [10, 20, 30, 40, 50]
        dep = [40, 50, 60, 70, 80, 90]
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 3)
