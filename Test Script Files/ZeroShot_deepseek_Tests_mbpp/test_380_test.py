import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):

    def test_multi_list(self):
        self.assertEqual(multi_list(3, 3), [[0, 0, 0], [0, 1, 2], [0, 2, 4]])
        self.assertEqual(multi_list(2, 2), [[0, 0], [0, 1]])
        self.assertEqual(multi_list(1, 1), [[0]])
        self.assertEqual(multi_list(0, 0), [])
