from django.http import HttpResponse
from django.shortcuts import render

from .forms import LearningForm
from .models import Learning


def index(request):
    return render(request, 'rand/index.html')


def show_all_topics(request):
    topics = Learning.objects.all()
    context = {
        'topics': topics
    }
    return render(request, 'rand/all_topics.html', context)


def add_topic(request):
    if request.method == 'POST':
        form = LearningForm(request.POST)
        if form.is_valid():
            form.save()
            return just_added(request)
        else:
            error = 'Error!'

    form = LearningForm()
    context = {
        'form': form
    }
    return render(request, 'rand/add_topic.html', context)


def just_added(request):
    return HttpResponse('Done!')


def random(request):
    return render(request, 'rand/random.html')
