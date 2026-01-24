import unittest
from mbpp_342_code import heappop, heappush
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):
    def test_find_minimum_range(self):
        list1 = [[1, 5, 8], [4, 12], [7, 8, 10, 12]]
        self.assertEqual(find_minimum_range(list1), (4, 7))

        list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(find_minimum_range(list2), (1, 7))

        list3 = [[10, 15, 20], [11, 16, 21], [12, 17, 22]]
        self.assertEqual(find_minimum_range(list3), (10, 11))

        list4 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        self.assertEqual(find_minimum_range(list4), (1, 6))

        list5 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
        self.assertEqual(find_minimum_range(list5), (1, 1))
