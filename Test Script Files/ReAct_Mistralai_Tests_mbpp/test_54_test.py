import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(counting_sort([]), [])

    def test_single_element_list(self):
        for element in range(10):
            self.assertEqual(counting_sort([element]), [element])

    def test_duplicate_elements(self):
        for element in range(10):
            test_list = [element] * 5 + [random.randint(0, 10) for _ in range(5)]
            sorted_list = sorted(test_list)
            self.assertEqual(counting_sort(test_list), sorted_list)

    def test_negative_numbers(self):
        test_list = [-5, -3, -1, 0, 1, 3, 5]
        sorted_list = sorted(test_list)
        self.assertEqual(counting_sort(test_list), sorted_list)

    def test_large_numbers(self):
        test_list = [random.randint(0, 1000000) for _ in range(10)]
        sorted_list = sorted(test_list)
        self.assertEqual(counting_sort(test_list), sorted_list)

    def test_empty_bucket(self):
        test_list = []
        buckets = [0] * (max(test_list) + 1)
        self.assertEqual(buckets, [0] * (max(test_list) + 1))

    def test_all_zeroes(self):
        test_list = [0] * 10
        self.assertEqual(counting_sort(test_list), [0] * 10)

    def test_all_max_value(self):
        max_value = 100
        test_list = [max_value] * 10
        self.assertEqual(counting_sort(test_list), [0] * 10)
