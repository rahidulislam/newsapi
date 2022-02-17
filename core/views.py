from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
import requests
# Create your views here.

class HomeView(View):
    template_name = 'core/index.html'
    def get(self, request):
        api_key = settings.NEWS_API_KEY
        r = requests.get("https://newsapi.org/v2/top-headlines/sources?apiKey={}".format(api_key))
        json_data = r.json()
        #print("json data: ",json_data)
        top_headlines = json_data['sources']
        print('sources: ', top_headlines)
        context={
            'top_headlines': top_headlines
        }
        return render(request,self.template_name, context)