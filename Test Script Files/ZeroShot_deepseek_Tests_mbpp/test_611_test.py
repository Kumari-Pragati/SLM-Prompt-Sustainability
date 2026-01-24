import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):

    def test_max_of_nth(self):
        self.assertEqual(max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2), 8)
        self.assertEqual(max_of_nth([[10, 20, 30], [40, 50, 60], [70, 80, 90]], 1), 90)
        self.assertEqual(max_of_nth([[100, 200, 300], [400, 500, 600], [700, 800, 900]], 0), 900)
        self.assertEqual(max_of_nth([[1000, 2000, 3000], [4000, 5000, 6000], [7000, 8000, 9000]], 2), 9000)
        self.assertEqual(max_of_nth([[10000, 20000, 30000], [40000, 50000, 60000], [70000, 80000, 90000]], 1), 90000)
