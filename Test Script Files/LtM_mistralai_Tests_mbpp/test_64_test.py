import unittest
from mbpp_64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):

    def test_simple_input(self):
        data = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        self.assertEqual(subject_marks(data), data)

    def test_sort_by_marks(self):
        data = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        sorted_data = [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)]
        self.assertEqual(subject_marks(data), sorted_data)

    def test_empty_list(self):
        self.assertEqual(subject_marks([]), [])

    def test_single_entry(self):
        data = [('English', 88)]
        self.assertEqual(subject_marks(data), data)

    def test_duplicate_entries(self):
        data = [('English', 88), ('English', 88)]
        self.assertEqual(subject_marks(data), [('English', 88)])

    def test_negative_marks(self):
        data = [('English', -10), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        self.assertEqual(subject_marks(data), [('Science', 90), ('Maths', 97), ('English', -10), ('Social sciences', 82)])

    def test_max_marks(self):
        data = [('English', 100), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        self.assertEqual(subject_marks(data), [('English', 100), ('Maths', 97), ('Science', 90), ('Social sciences', 82)])
