import unittest
from mbpp_64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):

    def test_sort_marks_in_descending_order(self):
        subject_marks_data = [
            ('English', 88),
            ('Science', 90),
            ('Maths', 97),
            ('Social sciences', 82)
        ]
        expected_sorted_data = [
            ('Maths', 97),
            ('Science', 90),
            ('English', 88),
            ('Social sciences', 82)
        ]
        self.assertEqual(subject_marks(subject_marks_data), expected_sorted_data)

    def test_empty_list(self):
        self.assertEqual(subject_marks([]), [])

    def test_single_item_list(self):
        self.assertEqual(subject_marks([('Subject', 100)]), [('Subject', 100)])

    def test_sort_marks_with_same_marks(self):
        subject_marks_data = [
            ('Subject1', 90),
            ('Subject2', 90),
            ('Subject3', 89)
        ]
        expected_sorted_data = [
            ('Subject1', 90),
            ('Subject2', 90),
            ('Subject3', 89)
        ]
        self.assertEqual(subject_marks(subject_marks_data), expected_sorted_data)
