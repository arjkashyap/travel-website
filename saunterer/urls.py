from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'saunterer'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'about/', views.about, name = 'about'),
    url(r'offers/', views.offer, name = 'offer'),
    url(r'gallery/', views.galary, name = 'gallery'),
    url(r'contact/', views.contact, name = 'contact'),
    url(r'^book-tour/$', views.TourForm.as_view(), name = 'tour_form'),
    url(r'^preferences/$', views.PreferenceForm.as_view(), name = 'pref_form'),
]   