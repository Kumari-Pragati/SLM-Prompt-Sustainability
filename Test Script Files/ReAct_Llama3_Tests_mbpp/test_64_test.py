import unittest
from mbpp_64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(subject_marks([]), [])

    def test_single_element(self):
        self.assertEqual(subject_marks([('English', 88)]), [('English', 88)])

    def test_multiple_elements(self):
        self.assertEqual(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]), 
                         [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])

    def test_sorted_by_marks(self):
        self.assertEqual(subject_marks([('English', 88), ('Maths', 97), ('Science', 90), ('Social sciences', 82)]), 
                         [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)])

    def test_marks_duplicates(self):
        self.assertEqual(subject_marks([('English', 88), ('English', 88), ('Maths', 97), ('Maths', 97)]), 
                         [('Maths', 97), ('English', 88)])

    def test_marks_empty(self):
        self.assertEqual(subject_marks([('English', 0), ('Maths', 0), ('Science', 0), ('Social sciences', 0)]), 
                         [('English', 0), ('Maths', 0), ('Science', 0), ('Social sciences', 0)])
