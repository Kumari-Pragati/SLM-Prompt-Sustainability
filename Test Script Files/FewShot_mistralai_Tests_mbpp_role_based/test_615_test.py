import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):
    def test_average_single_list(self):
        self.assertEqual(average_tuple([(1,), (2,), (3,)]), [1.0, 2.0, 3.0])

    def test_average_empty_list(self):
        self.assertListEqual(average_tuple([]), [])

    def test_average_single_element_list(self):
        self.assertEqual(average_tuple([[(1,)]]), [1.0])

    def test_average_mixed_length_lists(self):
        self.assertListEqual(average_tuple([[(1,), (2,), (3,)], [(4,), (5,)]]), [(1.0 + 2.0 + 3.0) / 3, 4.0])

    def test_average_negative_numbers(self):
        self.assertListEqual(average_tuple([[(1,), (-2,), (3,)]]), [(1.0 - 2.0 + 3.0) / 3, -2.0])
