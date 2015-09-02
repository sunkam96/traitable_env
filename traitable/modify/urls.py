from django.conf.urls import include, url
from . import views

urlpatterns = [
    
    url(r'^enter/',views.enter),
    url(r'^enter/individual',views.individual),
    url(r'^enter/upload',views.upload),

]
