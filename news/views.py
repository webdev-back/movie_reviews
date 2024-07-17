from django.shortcuts import render
from .models import News

# Create your views here.
def news(request):
    some_news = News.objects.all().order_by('-date')
    return render(request, "news.html", {'some_news': some_news})
