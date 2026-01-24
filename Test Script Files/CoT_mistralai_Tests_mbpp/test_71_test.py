import unittest
from71_code import comb_sort

class TestCombSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(comb_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(comb_sort([1]), [1])

    def test_simple_list(self):
        self.assertEqual(comb_sort([3, 2, 4, 1]), [1, 2, 3, 4])

    def test_reverse_list(self):
        self.assertEqual(comb_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_duplicates(self):
        self.assertEqual(comb_sort([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])

    def test_large_list(self):
        nums = [i for i in range(100)]
        random.shuffle(nums)
        sorted_nums = sorted(nums)
        self.assertEqual(comb_sort(nums), sorted_nums)

    def test_negative_numbers(self):
        self.assertEqual(comb_sort([-1, -2, -3]), [-3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(comb_sort([-1, 0, 1, -2, 2]), [-1, 0, 1, -2, 2])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            comb_sort(1.5)
