import django.conf.urls
import django.contrib
from .views import ChatterBotView

urlpatterns = [ django.conf.urls.url(r'^$' , ChatterBotView.as_view() , name='chatterbot' , ) , ]
