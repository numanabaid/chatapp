from django.shortcuts import render
from .models import Message
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    if request.method == 'POST':
        if request.POST['message'] != '':
            message = Message(text=request.POST['message'])
            message.save()
        messages_list = Message.objects.all()
        context = {'messages_list': messages_list}
        return HttpResponseRedirect(reverse('chats:index'))
    messages_list = Message.objects.all()
    context = {'messages_list': messages_list}
    return render(request, 'chats/index.html', context)

