from django.db import models

# Create your models here.

class Resume(models.Model):
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)

	def last_name_first(self):
		return "{} {}".format(self.last_name, self.first_name)

class Experience(models.Model):
	parent_resume = models.ForeignKey('Resume', on_delete=models.CASCADE, default=1)
	title = models.CharField(max_length=64, null=False, blank=False)
	location = models.CharField(max_length=64, null=False, blank=False)
	start_date = models.DateField(max_length=9, null=False, blank=False)
	end_date = models.DateField(max_length=9, null=False, blank=False)
	description = models.TextField(max_length=150, null=False, blank=False)

class Education(models.Model):
	institution_name = models.CharField(max_length=64, null=False, blank=False)
	location = models.CharField(max_length=64, null=False, blank=False)
	degree = models.CharField(max_length=64, null=False, blank=False)
	major = models.CharField(max_length=64, null=False, blank=False)
	gpa = models.FloatField(max_length=5, null=False, blank=False)

	def __str__(self):
		return self.title
