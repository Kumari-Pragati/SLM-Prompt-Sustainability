import unittest
from mbpp_827_code import sum_column

class TestSumColumn(unittest.TestCase):

    def test_sum_column(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(sum_column(list1, 1), 12)

        list2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
        self.assertEqual(sum_column(list2, 1), 120)

        list3 = [[100, 200, 300], [400, 500, 600], [700, 800, 900]]
        self.assertEqual(sum_column(list3, 1), 1500)

        list4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(sum_column(list4, 0), 21)

        list5 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
        self.assertEqual(sum_column(list5, 0), 210)

        list6 = [[100, 200, 300], [400, 500, 600], [700, 800, 900]]
        self.assertEqual(sum_column(list6, 0), 2100)

    def test_invalid_column(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(IndexError):
            sum_column(list1, 3)
