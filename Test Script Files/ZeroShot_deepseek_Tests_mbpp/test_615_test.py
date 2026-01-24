import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):

    def test_average_tuple(self):
        self.assertEqual(average_tuple([(1, 2, 3), (4, 5, 6)]), [2.5, 3.5, 4.5])
        self.assertEqual(average_tuple([(10, 20, 30), (40, 50, 60)]), [25.0, 35.0, 45.0])
        self.assertEqual(average_tuple([(1, 1, 1), (2, 2, 2)]), [1.5, 1.5, 1.5])
        self.assertEqual(average_tuple([(100, 200, 300), (400, 500, 600)]), [250.0, 350.0, 450.0])
