from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
# Create your views here.

class HomeView(View):
    template_name = 'core/index.html'
    def get(self, request):
        
        return render(request,self.template_name)