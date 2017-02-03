from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import CutURL


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {})


class CutRedirectView(View):
    def get(self, request, shortlink=None, *args, **kwargs):
        obj = get_object_or_404(CutURL, shortlink=shortlink)
        return HttpResponse('{}'.format(obj.url))

    def post(self, request, shortlink=None, *args, **kwargs):
        return HttpResponse('hey')