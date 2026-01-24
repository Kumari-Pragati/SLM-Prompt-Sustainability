import unittest
from mbpp_836_code import maxsize
from your_module_name import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_single_element(self):
        self.assertEqual(max_sub_array_sum([1], 1), 1)

    def test_negative_numbers(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 0)

    def test_positive_and_negative_numbers(self):
        self.assertEqual(max_sub_array_sum([-1, 2, -3, 4, -5], 5), 3)

    def test_large_positive_numbers(self):
        self.assertEqual(max_sub_array_sum([1000000001, 1000000002, 1000000003], 3), 3)

    def test_large_array(self):
        a = [random.randint(-1000000, 1000000) for _ in range(1000)]
        self.assertEqual(max_sub_array_sum(a, len(a)), max(a))
