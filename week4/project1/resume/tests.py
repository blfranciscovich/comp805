from django.test import TestCase
from .models import Resume, Education, Experience

# Create your tests here.
class TestResume (TestCase):
    test_resume = Resume.objects.create(first_name = 'Bridget',
        last_name = 'Franciscovich')
    test_education = Education.objects.create(parent_resume = test_resume,
        institution_name = 'UNH', location = 'New Hampshire',
        degree = 'Master of Science', major = 'IT', gpa = 4.0)
    test_experience = Experience.objects.create(parent_resume = test_resume,
        title = 'Marketing Manager', location = 'New Hampshire',
        start_date = '2011-01-01',end_date = '2022-02-02', description = 'Marketing is fun!')

    def setUp(self):
        self.test_resume.save()
        self.test_education.save()
        self.test_experience.save()

    def test_get_full_name(self):
        """
        Tests models.get_full_name(self):
        """
        expected = 'Bridget Franciscovich'
        resume = Resume.objects.first()
        self.assertEqual(resume.get_full_name(), expected)

    def test_get_last_first_name(self):
        """
        Tests models.get_last_first_name(self):
        """
        expected = 'Franciscovich Bridget'
        resume = Resume.objects.first()
        self.assertEqual(resume.get_last_first_name(), expected)

    def test_get_education(self):
        """
        Tests models.get_education(self):
        """
        self.assertEqual(self.test_resume.get_education().first(), self.test_education)

    def test_get_experience(self):
        """
        Tests models.get_experience(self):
        """
        self.assertEqual(self.test_resume.get_experience().first(), self.test_experience)
