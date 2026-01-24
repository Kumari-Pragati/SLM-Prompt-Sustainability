import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_elim([]), 1)

    def test_single_element(self):
        self.assertEqual(count_elim([1]), 1)
        self.assertEqual(count_elim([1.0]), 1)
        self.assertEqual(count_elim([True]), 1)
        self.assertEqual(count_elim([None]), 1)
        self.assertEqual(count_elim([str(1)]), 1)

    def test_multiple_elements(self):
        self.assertEqual(count_elim([1, 2, 3]), 3)
        self.assertEqual(count_elim([1.0, 2.0, 3.0]), 3)
        self.assertEqual(count_elim([True, False, True]), 2)
        self.assertEqual(count_elim([None, None, None]), 1)
        self.assertEqual(count_elim([str(1), str(2), str(3)]), 3)

    def test_list_with_tuple(self):
        self.assertEqual(count_elim([(1, 2), 3]), 1)

    def test_list_with_empty_tuple(self):
        self.assertEqual(count_elim([(), 3]), 1)

    def test_list_with_nested_tuples(self):
        self.assertEqual(count_elim([(1, (2, 3)), 4]), 1)

    def test_list_with_mixed_types(self):
        self.assertEqual(count_elim([1, (2, 3), 4]), 2)
