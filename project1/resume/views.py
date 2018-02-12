from django.shortcuts import render
from .models import Education, Experience

# Create your views here.


def education(request):
	"""
	Renders home page
	"""
	qs = Education.objects.all()
	context = {'Education' : qs}
	return render(request, 'resume/templates/education.html', context)

def experience(request):
	"""
	Renders home page
	"""
	qs = experience.objects.all()
	context = {'Experience' : qs}
	return render(request, 'resume/templates/experience.html', context)
