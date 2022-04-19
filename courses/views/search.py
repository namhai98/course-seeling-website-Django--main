from django.shortcuts import render
from courses.models import Course, course
from django.views.generic import ListView


def SearchView(request):
    if request.method == "POST":
        searched = request.POST[('searched')]
        courses = Course.objects.filter(name__contain=searched)
        return render(request, 'courses/search.html',{'searched':searched, 'course':courses})
    else:
        return render(request, 'courses/search.html',{})