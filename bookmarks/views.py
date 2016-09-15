from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

# Create your views here.
class Index(View):
    def get(self, request):
        params = {}
        params["name"]= "Django!"
        return render(request, 'base.html', params)

    def post(self, request):
        return HttpResponse('I am called from a post Request')
