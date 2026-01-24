import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):

    def test_typical_case(self):
        arr = [900, 940, 950, 1100, 1500, 1800]
        dep = [910, 1200, 1120, 1130, 1900, 2000]
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 3)

    def test_edge_case_single_train(self):
        arr = [900]
        dep = [1000]
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 1)

    def test_edge_case_no_trains(self):
        arr = []
        dep = []
        n = 0
        self.assertEqual(find_platform(arr, dep, n), 0)

    def test_edge_case_same_time_arrival_departure(self):
        arr = [900, 1000]
        dep = [1000, 900]
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 2)

    def test_explicitly_handled_error_case_invalid_input(self):
        arr = [900, 940, 950, 1100, 1500, 1800]
        dep = [910, 1200, 1120, 1130, 1900, 2000]
        n = -1
        with self.assertRaises(Exception):
            find_platform(arr, dep, n)
