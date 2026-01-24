import unittest
from mbpp_64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(subject_marks([]), [])

    def test_single_element_list(self):
        self.assertEqual(subject_marks([('English', 88)]), [('English', 88)])

    def test_multiple_elements_list(self):
        subjectmarks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        sorted_subjectmarks = subject_marks(subjectmarks)
        self.assertEqual(sorted_subjectmarks, sorted(subjectmarks, key=lambda x: x[1]))

    def test_list_with_duplicates(self):
        subjectmarks = [('English', 88), ('Science', 88), ('Maths', 97), ('Social sciences', 82)]
        sorted_subjectmarks = subject_marks(subjectmarks)
        self.assertEqual(sorted_subjectmarks, sorted(subjectmarks, key=lambda x: x[1]))
