from datetime import datetime

from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse

from notes.models import Note

def index(request):
    app = settings.INSTANCE_NAME
    context = dict(app=settings.INSTANCE_NAME)
    if request.POST:
        text = request.POST['note']
        message = 'Got {} at {}'.format(text, datetime.now())
        context.update(message=message)
        Note.objects.create(text=text)
        return redirect('notes:index')
    context['notes'] = Note.objects.order_by('-created_at')[:10]
    return render(request, 'notes/index.html', context)

def detail(request, note_id):
    return HttpResponse("You're looking at note %s." % note_id)

def results(request, note_id):
    response = "You're looking at the results of note %s."
    return HttpResponse(response % note_id)

def vote(request, note_id):
    return HttpResponse("You're voting on note %s." % note_id)
