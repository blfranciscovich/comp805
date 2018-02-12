from django.shortcuts import render
from .models import Education, Experience

# Create your views here.

def resume(request):
	"""
	This function returns education and experience objects in the resume/ URL.
	request: URL request resume/ from user
	return: the URL resume/ with all education and experience objects
	"""
	qs = Education.objects.all()
	qs2 = Experience.objects.all()
	context = {'Education' : qs, 'Experience': qs2}
	return render(request, 'resume.html', context)