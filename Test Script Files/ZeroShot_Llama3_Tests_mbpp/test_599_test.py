import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):

    def test_sum_average(self):
        self.assertEqual(sum_average(1), (1, 1.0))
        self.assertEqual(sum_average(2), (3, 1.5))
        self.assertEqual(sum_average(3), (6, 2.0))
        self.assertEqual(sum_average(4), (10, 2.5))
        self.assertEqual(sum_average(5), (15, 3.0))
        self.assertEqual(sum_average(10), (55, 5.5))
        self.assertEqual(sum_average(20), (210, 10.5))
        self.assertEqual(sum_average(30), (465, 15.5))
        self.assertEqual(sum_average(40), (820, 20.5))
        self.assertEqual(sum_average(50), 1275, 25.5)
        self.assertEqual(sum_average(100), 5050, 50.5)
        self.assertEqual(sum_average(200), 21020, 105.0)
        self.assertEqual(sum_average(300), 45030, 150.1)
        self.assertEqual(sum_average(400), 80080, 200.2)
        self.assertEqual(sum_average(500), 125750, 251.5)
