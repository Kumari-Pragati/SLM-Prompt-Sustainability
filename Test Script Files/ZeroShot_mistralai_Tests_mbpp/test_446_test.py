import unittest
from mbpp_446_code import Counter
from your_module import count_Occurrence  # assuming the function is in a module named 'your_module'

class TestCountOccurrence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_Occurrence((), []), 0)

    def test_single_item(self):
        self.assertEqual(count_Occurrence((1,), [1]), 1)
        self.assertEqual(count_Occurrence((2,), [1]), 0)

    def test_multiple_items(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [1, 2, 3, 4]), 3)
        self.assertEqual(count_Occurrence((1, 2, 3), [4, 5, 6]), 0)

    def test_duplicates(self):
        self.assertEqual(count_Occurrence((1, 1, 2, 2, 3), [1, 2, 3]), 4)

    def test_counter(self):
        counter = Counter([1, 2, 3, 1, 2, 3])
        self.assertEqual(count_Occurrence(counter.elements(), counter.elements()), sum(counter.values()))
