from django.conf.urls import url
from .views import HomeView,CareerView,CateringView,MenuView,ReservationView,AboutView,ContactView,ClubView,EstimateView
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^club/$', ClubView.as_view(), name='club'),
    url(r'^careers/$', CareerView.as_view(), name='career'),
    url(r'^catering/$', CateringView.as_view(), name='catering'),
    url(r'^catering/estimate$', EstimateView.as_view(), name='estimate'),
    url(r'^menu/$', MenuView.as_view(), name='menu'),
    url(r'^reservations/$', ReservationView.as_view(), name='reservations'),
    url(r'^login/$', login, {'template_name':'home/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    # url(r'^home/$', views.HomeView.as_view(), name='home'),
    # url(r'^home/comments/$', views.PostView.as_view(), name='comments'),
    # url(r'^register/$', views.register, name='register'),
]
