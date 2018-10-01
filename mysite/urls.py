from django.contrib import admin
from django.conf.urls import url, include
#from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("mainApp.urls")),     #new line
    url(r'^news/', include("news.urls")),   #new line
]
