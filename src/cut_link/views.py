from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import CutURL
from .forms import URLForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = URLForm()
        context = {
            'title': 'Cut your URL',
            'form': form,
        }
        return render(request, 'content.html', context=context)

    def post(self, request, *args, **kwargs):
        co = CutURL.objects.filter(pub_date__month=2).count()
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            obj, created = CutURL.objects.get_or_create(url=url)
            context = {
                'co': co,
                'title': 'Cut your URL',
                'form': form,
                'obj': obj,
            }
            if not created:
                context['created'] = 'Already exists in DataBase.'
        else:
            context = {
                'title': 'Cut your URL',
                'form': form,
            }
        return render(request, 'content.html', context=context)


class URLRedirectView(View):
    def get(self, request, shortlink=None, *args, **kwargs):
        obj = get_object_or_404(CutURL, shortlink=shortlink)
        return HttpResponseRedirect(obj.url)
