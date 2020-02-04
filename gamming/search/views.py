from django.shortcuts import render
from django.views.generic import ListView
from home.models import Registration
from live.models import Live


class SearchTeamView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchTeamView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        qs = Live.objects.by_name('links')
        if qs == {}:
            qs = None
        obj = qs.first()
        context['link'] = obj

        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        if query is not None:
            return Registration.objects.search(query)
        return Registration.objects.verified()