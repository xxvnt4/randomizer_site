from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from .forms import LearningForm
from .models import Learning

from random import choice


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
            return show_all_topics(request)
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
    all_topics = Learning.objects.all()
    random_topic = choice(all_topics)

    random_topic.date_watched = datetime.now()
    random_topic.save()

    context = {
        'random_topic': random_topic
    }
    return render(request, 'rand/random.html', context)


def get_topic_info(request, id):
    topic = Learning.objects.get(id=id)

    context = {
        'topic': topic
    }
    return render(request, 'rand/topic_info.html', context)


def confirm_remove(request, id):
    context = {
        'id': id
    }
    return render(request, 'rand/confirm_to_delete.html', context)


def remove_topic(request, id):
    topic = Learning.objects.get(id=id)
    topic.delete()

    return render(request, 'rand/topic_removed.html')


def edit_topic(request, id):
    instance = Learning.objects.get(id=id)

    if request.method == 'POST':
        form = LearningForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            instance.date_updated = datetime.now()
            instance.save()

            return get_topic_info(request, id)

    form = LearningForm(instance=instance)
    context = {
        'form': form
    }
    return render(request, 'rand/edit_topic.html', context)


def just_edited(request):
    return HttpResponse('Done!')
