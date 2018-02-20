from django.db import models

# Create your models here.

class Resume(models.Model):
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)

	def get_full_name(self):
		"""
		Returns full name in the following order: First name, Last Name.
		"""
		return "{} {}".format(self.first_name, self.last_name)

	def get_last_first_name(self):
		"""
		Returns the full name in the following order: Last Name, First Name.
		"""
		return "{} {}".format(self.last_name, self.first_name)

	def get_education(self):
		"""
		Returns all education related to the resume based on a foreign key to education model.
		"""
		return self.education_set.all()

	def get_experience(self):
		"""
		Returns all experience related to the resume based on a foreign key to experience model.
		"""
		return self.experience_set.all()

class Experience(models.Model):
	parent_resume = models.ForeignKey('Resume', on_delete=models.CASCADE, default=1)
	title = models.CharField(max_length=64, null=False, blank=False)
	location = models.CharField(max_length=64, null=False, blank=False)
	start_date = models.DateField(max_length=9, null=False, blank=False)
	end_date = models.DateField(max_length=9, null=False, blank=False)
	description = models.TextField(max_length=150, null=False, blank=False)

class Education(models.Model):
	parent_resume = models.ForeignKey('Resume', on_delete=models.CASCADE, default=1)
	institution_name = models.CharField(max_length=64, null=False, blank=False)
	location = models.CharField(max_length=64, null=False, blank=False)
	degree = models.CharField(max_length=64, null=False, blank=False)
	major = models.CharField(max_length=64, null=False, blank=False)
	gpa = models.FloatField(max_length=5, null=False, blank=False)

	def __str__(self):
		return self.title
