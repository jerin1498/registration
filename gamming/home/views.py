from django.shortcuts import render
from django.views.generic import CreateView, FormView, DetailView, View, TemplateView
from django.views.generic.list import ListView
from .forms import Registration_form
from .models import Registration
from django.utils import timezone
from django.views.generic.detail import DetailView
from live.models import Live
from recent_match.models import RecentMatch
from django.urls import reverse_lazy
# Create your views here.


def maps(request):
    return render(request, 'maps.html')


class Home(ListView):
    model = RecentMatch
    template_name = "marble/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_match'] = RecentMatch.objects.all()
        context['registration'] = 'open'
        qs = Live.objects.by_name('links')
        if qs == {}:
            qs = None
        obj = qs.first()
        context['link'] = obj
        return context



def about(request):

    qs = Live.objects.by_name('links')
    if qs == {}:
        qs = None
    q = qs.first()

    context = {'link': q}
    return render(request, "marble/about.html", context)


class ContactPage(TemplateView):
    template_name = "marble/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Live.objects.by_name('links')
        if qs == {}:
            qs = None
        obj = qs.first()
        context['link'] = obj
        return context


class RegisterVew(CreateView):
    form_class = Registration_form
    success_url = reverse_lazy('home:registered-teams')
    template_name = 'marble/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Live.objects.by_name('links')
        if qs == {}:
            qs = None
        obj = qs.first()
        context['link'] = obj
        return context


class TeamList(ListView):
    model = Registration

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        qs = Live.objects.by_name('links')
        if qs == {}:
            qs = None
        obj = qs.first()
        context['link'] = obj
        return context


class TeamDetail(DetailView):
    queryset = Registration.objects.all()
    template_name = "marble/registration_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        qs = Live.objects.by_name('links')
        if qs == {}:
            qs = None
        obj = qs.first()
        context['link'] = obj

        return context


class MatchDate(ListView):
    model = Registration
    template_name = "marble/match_date.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['day_1'] = Registration.objects.match_day_1()
        context['day_2'] = Registration.objects.match_day_2()
        context['day_3'] = Registration.objects.match_day_3()
        context['day_4'] = Registration.objects.match_day_4()
        context['day_5'] = Registration.objects.match_day_5()
        context['day_6'] = Registration.objects.match_day_6()
        context['day_7'] = Registration.objects.match_day_7()
        context['day_8'] = Registration.objects.match_day_8()
        context['day_9'] = Registration.objects.match_day_9()
        context['day_10'] = Registration.objects.match_day_10()
        context['semi_final'] = Registration.objects.semi_final_match()
        context['final'] = Registration.objects.final_match()
        context['now'] = timezone.now()
        qs = Live.objects.by_name('links')
        if qs == {}:
            qs = None
        obj = qs.first()
        context['link'] = obj

        return context


class VerifiedTeams(ListView):
    model = Registration
    template_name = 'marble/verified_team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verified'] = Registration.objects.verified()
        context['now'] = timezone.now()
        qs = Live.objects.by_name('links')
        if qs == {}:
            qs = None
        obj = qs.first()
        context['link'] = obj
        return context


class RegisteredTeams(ListView):
    model = Registration
    template_name = 'marble/registered_team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registered'] = Registration.objects.all()
        context['now'] = timezone.now()
        qs = Live.objects.by_name('links')
        if qs == {}:
            qs = None
        obj = qs.first()
        context['link'] = obj
        return context


class QualifiedTeams(ListView):
    model = Registration
    template_name = 'marble/qualified_team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qualified'] = Registration.objects.qualified()
        context['now'] = timezone.now()
        qs = Live.objects.by_name('links')
        if qs == {}:
            qs = None
        obj = qs.first()
        context['link'] = obj
        return context


class PortFolio(ListView):
    model = Registration
    template_name = 'marble/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verified'] = Registration.objects.verified()
        context['now'] = timezone.now()
        qs = Live.objects.by_name('links')
        if qs == {}:
            qs = None
        obj = qs.first()
        context['link'] = obj
        return context