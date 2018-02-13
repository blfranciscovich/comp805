from django.shortcuts import render
from .models import Education, Experience

# Create your views here.

def resume(request):
	"""
	This function returns education and experience objects in the URL resume/.
	request: URL request resume/ from user
	return: the URL resume/ with all education and experience objects
	"""
	query_set = Education.objects.all()
	query_set2 = Experience.objects.all()
	context = {'Education' : query_set, 'Experience': query_set2}
	return render(request, 'resume.html', context)