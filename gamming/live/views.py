from django.shortcuts import render
from .models import Live

# Create your views here.


def live(request):

    qs = Live.objects.by_name('links')
    if qs == {}:
        qs = None
    q = qs.first()

    context = {'link': q}
    return render(request, 'live/youtube.html', context)



def account(request):

    qs = Live.objects.by_name('links')
    if qs == {}:
        qs = None
    q = qs.first()

    context = {'link': q}
    return render(request, 'marble/base/account.html', context)
