from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from django.urls import path #для третьей версии
from news.models import Articles

# отображаем некоторый список, чтобы работать с ними

urlpatterns = [
    url
    (r'^$', 
    ListView.as_view(queryset = Articles.objects.all().order_by("-date")[:20],
    template_name="news/posts.html")),  #обработчик ссылок, чтобы обрабатывать все статьи которые будут отображаться все новости
    #проверяем на число, какая статься у нас
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Articles, template_name= "news/post.html")),
]
 